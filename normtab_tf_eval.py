import sqlite3
from utils.preprocess import *
from utils.normalizer import *
from utils.llm_agent import *
from utils.all_prompts import *
import time
import csv


# ---------------------------------------------------------------

def get_ans_sql(prompt):
    response = None
    while response is None:
        try:
            response = get_completion(prompt, temperature=0)
        except:
            time.sleep(2)
            pass
    return response
# ---------------------------------------------------------------

if __name__ == "__main__":

    norm_table_path = "analysis/normtab_unique_output_tf.csv"
    tab_group_path = "datasets/table_group_tf.json"

    with open(tab_group_path, "r") as file:
        table_qa_group = json.load(file)

    # print(table_qa_group)

    df = pd.read_csv(norm_table_path)

    number_of_tables = df.shape[0]
    print()

    tf_path = "datasets/tabfact_small_test.jsonl"

    unique_tabs = [x for x in range(0, number_of_tables)]

    conn = sqlite3.connect('table.db')

    start = 5
    end = 20

    # ---------------------------------------Write outputs---------------------------
    fw = open(f'outputs_C/normtab_t_eval_june10_tf_a.jsonl', 'a')
    # fw.write(json.dumps(tmp) + '\n')
    # ---------------------------------------------------------------
    f = open('outputs_C/normtab_t_eval_june10_tf_a.csv', 'a')
    writer = csv.writer(f)
    # header = ['id', 'statemet', 'answer', 'prediction', 'sql', 'response']
    # writer.writerow(header)
    # -------------------------------------------------------------------------------

    t_correct = 0
    gt_samples = 0


    for index, row in df.iterrows():
        if index in unique_tabs[start:end]:
            id = row['id']
            norm_tab = row['norm_table']
            norm_tab = str(norm_tab).strip().split('=')[1]

            try:
                df = parse_table(norm_tab)
                print('ids: ', id, '\nTable:\n', df.to_markdown(index=False))

                df.to_sql('T', conn, if_exists='replace', index=False)

                col = df.columns

                tab_col = ""
                for c in col:
                    tab_col += c + ", "
                tab_col = tab_col.strip().strip(',')
                print('Table Column: ', tab_col)

                # Execute select query
                query = "SELECT * FROM T limit 3"
                three_rows = pd.read_sql_query(query, conn)
                three_rows = table_linearization(three_rows, style='pipe')
            except:
                print("error\n")
                continue

            # Display the result
            print("DataFrame from database (3 rows) :\n")
            print(three_rows)

            table_ids = table_qa_group[id]
            # table_ids = [int(item.replace('nu-', '')) for item in table_ids]
            print("table_ids: ", table_ids)

            print('\nmain_table:', id, 'table_qa_group: ', table_ids, 'number of questions: ', len(table_ids))
            # table_ids = [0,1]
            correct = 0
            t_samples = 0

            with open(tf_path, encoding='utf-8') as f1:
                for i, l in enumerate(f1):
                    if i in table_ids:
                        dic = json.loads(l)
                        ids = dic['table_id']
                        title = dic['table_caption']
                        # table = dic['table_text']
                        statement = dic['statement']
                        label = dic['label']

                        print('\n\nid: ', ids, ' S: ', statement, ' label: ', label)

                        prompt = generate_sql_prompt_tf(title, tab_col, statement, three_rows)

                        response = ""
                        output_ans = ""

                        try:
                            answer_sql = get_ans_sql(prompt)
                            print("answer_sql; ", answer_sql)

                            prediction = pd.read_sql_query(answer_sql, conn)
                            print("\n\nprediction: ", prediction, '\nGold answer: ', label)

                            if prediction.shape == (1, 1):
                                result_list = prediction.values.tolist()

                                output_ans = ""
                                for row in result_list:
                                    for coll in row:
                                        output_ans += str(coll) + " "
                                        # print(coll)
                                response = "direct ans"
                                output_ans = output_ans.lower()
                                print('\nDirect ans: ', output_ans, 'Gold: ', label)


                            output_ans = output_ans.lower()
                            print('\nGen output: ', output_ans, 'Gold: ', label)

                            if output_ans.strip() == str(label):
                                correct += 1
                                t_correct += 1
                                print("correct: ", correct)

                            t_samples += 1
                            gt_samples += 1

                            print('Correcet: ', correct, 'total: ', t_samples, "Accuracy: ", correct / (t_samples + 0.0001))
                            print("\n-----------------------------------------------\n")

                        except:
                            print("error: ", ids)
                            continue

                        tmp = {'key': ids, 'statement': statement, 'prediction': output_ans,
                               'answer': label}
                        fw.write(json.dumps(tmp) + '\n')
                        # #
                        data = [ids, statement, label, output_ans.strip(), answer_sql, prediction.to_markdown(index=False)]
                        writer.writerow(data)


                print("***********************************************************\n")

                print('Tablewise: Correcet: ', correct, 'total: ', t_samples, "Accuracy: ", correct / (t_samples + 0.0001))
                print("\n-----------------------------------------------\n")

            print('Cumilitive: Correcet: ', t_correct, 'total: ', gt_samples, "Accuracy: ", t_correct / (gt_samples + 0.0001))
            print("\n-----------------------------------------------\n")

            print("***********************************************************\n")

    f.close()
    fw.close()
    conn.close()







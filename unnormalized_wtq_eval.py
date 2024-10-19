import sqlite3
from utils.preprocess import *
from utils.normalizer import *
from utils.all_prompts import *
from utils.llm_agent import *
import time
# ----------------------------------------------------------------

def generate_prompt(title, tab_col, question, examples):
    prompt = "" + p_sql_three_wtq
    prompt += "\nSQLite table properties:\n\n"
    prompt += "Table: " + title + " (" + str(tab_col) + ")" + "\n\n"
    prompt += "3 example rows: \n select * from T limit 3;\n"
    prompt += examples + "\n\n"
    prompt += "Q: " + question + "\n"
    prompt += "SQL:"
    return prompt

def get_ans_sql(prompt):
    response = None
    while response is None:
        try:
            response = get_completion(prompt, temperature=0.5, max_tokens=100)
        except:
            time.sleep(2)
            pass
    return response

def eval_unnormalized_wtq():

    path = 'datasets/wtq_test3.jsonl'

    start = 0
    end = 10

    unique_tab_ids = UNIQUE_TAB_IDS_WTQ[start:end]

    # --------------------------------------------------------------
    # fw = open(f'outputs_B/unnorm_tab_eval_may25.jsonl', 'a')
    # fw.write(json.dumps(tmp) + '\n')
    # f = open('outputs_B/unnorm_tab_eval_may25.csv', 'a')
    # writer = csv.writer(f)
    # header = ['id', 'question', 'answer', 'prediction', 'sql', 'response']
    # writer.writerow(header)
    # ---------------------------------------------------------------
    conn = sqlite3.connect('table.db')

    counter = start - 1

    with open(path, encoding='utf-8') as f1:
        for i, l in enumerate(f1):
            if i in unique_tab_ids:
                dic = json.loads(l)
                ids = dic['ids']
                title = dic['title']
                table = dic['table_text']
                question = dic['statement']
                answer = dic['answer']
                answer = ','.join(answer)
                answer = answer.lower()
                print('\n\nid: ', ids, ' Q: ', question, ' ans: ', answer)

                T = dict2df(table)
                T = T.assign(row_number=range(len(T)))
                row_number = T.pop('row_number')
                T.insert(0, 'row_number', row_number)
                col = T.columns

                # print('Table Coll: ', col)
                tab_col = ""
                for c in col:
                    tab_col += c + ", "
                tab_col = tab_col.strip().strip(',')
                print('Table Column: ', tab_col)

                # --------------------------------------------------------------------------------------
                try:
                    T.to_sql('T', conn, if_exists='replace', index=False)

                    # linear_table = table_linearization(T, style='pipe')

                    print('Original Table:\n\n', T.to_markdown(index=False))

                    # Execute select query
                    query = "SELECT * FROM T limit 3"
                    three_rows = pd.read_sql_query(query, conn)
                    three_rows = table_linearization(three_rows, style='pipe')

                    print("DataFrame from database (3 rows) :\n")
                    print(three_rows)
                except:
                    print("error.")
                    continue

                table_ids = table_qa_group[ids]
                table_ids = [int(item.replace('nu-', '')) for item in table_ids]

                print('\nmain_table:', ids, 'table_qa_group: ', table_ids, 'number of questions: ', len(table_ids))
                # table_ids = [0,1]
                correct = 0
                t_samples = 0

                counter += 1
                print('counter: ', counter)
                with open(wikitq_path, encoding='utf-8') as f1:
                    for i, l in enumerate(f1):
                        if i in table_ids:
                            dic = json.loads(l)
                            ids = dic['ids']
                            title = dic['title']
                            table = dic['table_text']
                            question = dic['statement']
                            answer = dic['answer']
                            answer = ','.join(answer)
                            answer = answer.lower()
                            print('\n\nid: ', ids, ' Q: ', question, ' ans: ', answer)

                            prompt = generate_sql_prompt_wtq(title, tab_col, question, three_rows, mode="original")

                            response = ""
                            output_ans = ""

                            try:
                                answer_sql = get_ans_sql(prompt)
                                print("answer_sql; ", answer_sql)

                                prediction = pd.read_sql_query(answer_sql, conn)
                                print("\n\nprediction: ", prediction.to_markdown(index=False), '\nGold answer: ', answer)

                                if prediction.shape == (1, 1):
                                    result_list = prediction.values.tolist()
                                    # print('M1 - Result List: ', result_list, type(result_list))

                                    output_ans = ""
                                    for row in result_list:
                                        for coll in row:
                                            output_ans += str(coll) + " "
                                            # print(coll)

                                    output_ans = output_ans.lower()
                                    print('\nDirect ans: ', output_ans, 'Gold: ', answer)

                                elif not prediction.empty:
                                    result_list = prediction.values.tolist()

                                    output_ans = ""
                                    for row in result_list:
                                        for coll in row:
                                            output_ans += str(coll) + " "
                                        output_ans += ","
                                    if output_ans.endswith(','):
                                        output_ans = output_ans.rstrip(',')

                                    output_ans = output_ans.lower()

                                output_ans = output_ans.lower()
                                print('\nGen output: ', output_ans, 'Gold: ', answer)
                                if output_ans.strip() == answer or output_ans.strip().find(answer) != -1 \
                                        or answer.strip().find(output_ans.strip()) != -1:
                                    correct += 1
                                    print("correct: ", correct)

                                t_samples += 1

                                print('Correcet: ', correct, 'total: ', t_samples, "Accuracy: ",
                                      correct / (t_samples + 0.0001))
                                print("\n-----------------------------------------------\n")

                            except:
                                print("error: ", ids)
                                continue

                            # ------------ ------------- ---------------------- ------------- -----
                            # tmp = {'key': ids, 'question': question, 'prediction': output_ans,
                            #        'answer': answer}
                            # fw.write(json.dumps(tmp) + '\n')
                            # # #
                            # data = [ids, question, answer, output_ans.strip(), answer_sql,
                            #         prediction.to_markdown(index=False)]
                            # writer.writerow(data)

                print("***********************************************************\n")

    # f.close()
    # fw.close()

    conn.close()


if __name__ == "__main__":

    norm_table_path = "analysis/norm_tab_unique_output_wtq.csv"
    tab_group_path = "datasets/table_group_wtq.json"

    with open(tab_group_path, "r") as file:
        table_qa_group = json.load(file)

    # print(table_qa_group)

    df = pd.read_csv(norm_table_path)
    number_of_tables = df.shape[0]
    print()

    wikitq_path = 'datasets/wtq_test3.jsonl'
    unique_tabs = [x for x in range(0, number_of_tables)]

    eval_unnormalized_wtq()



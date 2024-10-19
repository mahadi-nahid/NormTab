import json
import pandas as pd
import sqlite3
import csv
import os
from utils.preprocess import *
from utils.normalizer import *
from utils.all_prompts import *
from utils.llm_agent import *
import time

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

def run_unnormalied_tf():

    path = 'datasets/tabfact_small_test.jsonl'


    start = 5
    end = 6
    unique_tab_ids = UNIQUE_TAB_IDS_TF[start:end]

    # -------------------------
    # f = open('analysis/norm_tab_unique_output_wtq.csv', 'a')
    # writer = csv.writer(f)
    # header = ['id', 'question', 'gold answer', 'table title',
    #   'original_tab', 'norm_table']
    # writer.writerow(header)
    # -------------------------
    conn = sqlite3.connect('table.db')

    with open(path, encoding='utf-8') as f1:
        for i, l in enumerate(f1):
            if i in unique_tab_ids:
                dic = json.loads(l)
                ids = dic['table_id']
                title = dic['table_caption']
                table = dic['table_text']
                statement = dic['statement']
                label = dic['label']
                # answer = ','.join(answer)
                # answer = answer.lower()
                print('\n\nid: ', ids, ' S: ', statement, ' label: ', label)

                T = dict2df(table)
                # T = T.assign(row_number=range(len(T)))
                # row_number = T.pop('row_number')
                # T.insert(0, 'row_number', row_number)
                col = T.columns

                # print('Table Coll: ', col)
                tab_col = ""
                for c in col:
                    tab_col += c + ", "
                tab_col = tab_col.strip().strip(',')
                print('Table Column: ', tab_col)

                # --------------------------------------------------------------------------------------
                T.to_sql('T', conn, if_exists='replace', index=False)

                print('Original Table:\n\n', T.to_markdown(index=False))

                # Execute select query
                query = "SELECT * FROM T limit 3"
                three_rows = pd.read_sql_query(query, conn)
                three_rows = table_linearization(three_rows, style='pipe')

                print("DataFrame from database (3 rows) :\n")
                print(three_rows)

                table_ids = table_qa_group[ids]
                # table_ids = [int(item.replace('nu-', '')) for item in table_ids]

                print('\nmain_table:', ids, 'table_qa_group: ', table_ids, 'number of questions: ', len(table_ids))
                # table_ids = [0,1]
                correct = 0
                t_samples = 0

                with open(tf_path, encoding='utf-8') as f1:
                    for i, l in enumerate(f1):
                        if i in table_ids:
                            dic = json.loads(l)
                            ids = dic['table_id']
                            title = dic['table_caption']
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
                                    # print('M1 - Result List: ', result_list, type(result_list))

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
                                    print("correct: ", correct)

                                t_samples += 1

                                print('Correcet: ', correct, 'total: ', t_samples, "Accuracy: ",
                                      correct / (t_samples + 0.0001))
                                print("\n-----------------------------------------------\n")

                            except:
                                print("error: ", ids)
                                continue

                print("***********************************************************\n")


                # data = [ids, question, answer, title, linear_table, norm_tab]
                # writer.writerow(data)
    # f.close()

    conn.close()


if __name__ == "__main__":

    norm_table_path = "analysis/normtab_unique_output_tf.csv"
    tab_group_path = "datasets/table_group_tf.json"

    with open(tab_group_path, "r") as file:
        table_qa_group = json.load(file)

    print(table_qa_group)
    df = pd.read_csv(norm_table_path)
    number_of_tables = df.shape[0]

    tf_path = "datasets/tabfact_small_test.jsonl"
    unique_tabs = [x for x in range(0, number_of_tables)]

    run_unnormalied_tf()



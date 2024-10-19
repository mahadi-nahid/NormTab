import csv
import pandas as pd
from pandasql import sqldf
from sqlalchemy import create_engine
from utils.preprocess import *
from utils.normalizer import *
from utils.prompt_wtq import *


def tabsqlify_wtq(T, title, tab_col, question, three_row, selection='rc'):
    # ----------------------------------------------------------------------------------------------
    # selection = ['col', 'row', 'rc', 'sql']
    prompt = gen_table_decom_prompt(title, tab_col, question, three_row, selection=selection)
    # print(prompt)
    sql = get_sql_3(prompt)
    # sql = sql.split('where')[0]
    print('\nM1: ', sql, '\n')

    response = ""
    output_ans = ""
    linear_table = ""

    result = pd.DataFrame()
    try:
        result = sqldf(sql, locals())
    except:
        # print('error --> id: ', i, ids)
        # empty_error_ids.append(i)
        output_ans = "error"
        # continue

    if result.shape == (1, 1):
        result_list = result.values.tolist()
        # print('M1 - Result List: ', result_list, type(result_list))

        output_ans = ""
        for row in result_list:
            for coll in row:
                output_ans += str(coll) + " "
                # print(coll)
        response = "direct ans"
        output_ans = output_ans.lower()
        print('Direct ans: ', output_ans, 'Gold: ', answer)
        # continue
    elif not result.empty:
        # result_list = [result.columns.values.tolist()] + result.values.tolist()
        # print('M1 - Result List: ', result_list, type(result_list))

        linear_table = table_linearization(result, style='pipe')
        # print('M1 - Linear Table: \n', linear_table)

        prompt_ans = generate_sql_answer_prompt(title, sql, linear_table, question)
        # print('promt_ans:\n', prompt_ans)
        response = get_answer(prompt_ans)
        print('response: ', response)
        try:
            output_ans = response.split("Answer:")[1]
            # print('Output answer: ', output_ans)
        except:
            print("Error: Answer generation.")
            output_ans = "" + response
        match = re.search(r'(The|the) answer is ([^\.]+)\.$', output_ans)
        if match:
            output_ans = match.group(2).strip('"')
        print('\nAnswer gen output: ', output_ans, 'Gold: ', answer)

    else:
        print('empty. id --> ', i, id)
        empty_error_ids.append(i)
        prompt = gen_table_decom_prompt(title, tab_col, question, three_row, selection='col')
        sql = get_sql_3(prompt)
        # sql = sql.split('where')[0]
        print('col sql: ', sql)
        try:
            result = sqldf(sql, locals())
        except:
            print('col selection - empty/error')
        if not result.empty and result is not None:
            linear_table = table_linearization(result, style='pipe')
        else:
            sql = "select * from T"
            result = sqldf(sql, locals())
            linear_table = table_linearization(result, style='pipe')

        prompt_ans = generate_sql_answer_prompt(title, sql, linear_table, question)
        # print('promt_ans:\n', prompt_ans)
        response = get_answer(prompt_ans)
        print('response: ', response)
        try:
            output_ans = response.split("Answer:")[1]
            # print('Output answer: ', output_ans)
        except:
            print("Error: Answer generation.")
            output_ans = "" + response
        match = re.search(r'(The|the) answer is ([^\.]+)\.$', output_ans)
        if match:
            output_ans = match.group(2).strip('"')
        print('\nAnswer gen output: ', output_ans, 'Gold: ', answer)


    return sql, result, response, output_ans, linear_table


if __name__ == "__main__":

    # path = 'wtq_cut_more_than_50_percent.jsonl'
    # path = 'wtq_cut_25_to_50_percent.jsonl'
    # path = 'wtq_cut_10_to_25_percent.jsonl'
    # path = 'wtq_cut_0_to_10_percent.jsonl'
    # path = 'datasets/wtq_test3.jsonl'
    path = 'datasets/normtab_tabsqlify_data_C.jsonl'

    start = 271
    end = start + 10

    table_ids = list(range(start, end))
    # 70-80
    # large_table_ids = [30, 44, 141, 158, 208, 237, 263, 279, 348, 367, 395, 401, 441, 444, 514, 546, 553, 573, 575, 642, 659, 690, 699, 718, 766, 904, 919, 936, 973, 999, 1004, 1008, 1014, 1041, 1073, 1084, 1109, 1140, 1166, 1185, 1259, 1330, 1365, 1382, 1406, 1430, 1453, 1596, 1617, 1624, 1627, 1671, 1707, 1844, 1873, 1877, 1895, 1899, 1918, 1945, 1955, 1969, 2019, 2047, 2100, 2160, 2191, 2212, 2219, 2235, 2243, 2292, 2293, 2323, 2355, 2359, 2439, 2443, 2504, 2552, 2565, 2630, 2633, 2650, 2673, 2696, 2729, 2797, 2816, 2819, 2900, 2906, 2908, 3040, 3092, 3139, 3158, 3203, 3228, 3253, 3290, 3294, 3419, 3434, 3469, 3487, 3573, 3624, 3662, 3663, 3679, 3693, 3706, 3709, 3711, 3732, 3750, 3941, 3990, 4004, 4007, 4068, 4085, 4188, 4194, 4196, 4222, 4299]
    # print(len(large_table_ids))
    # large_table_ids = large_table_ids[126:129]

    correct = 0
    t_samples = 0
    empty_error_ids = []

    tabsqlify = True
    # tabsqlify = False

    with open(path, encoding='utf-8') as f1:
        # --------------------------------------------------------------
        fw = open(f'outputs_NormTabSQLify/wtq_normtabsqlify.jsonl', 'a')
        # fw.write(json.dumps(tmp) + '\n')
        # ---------------------------------------------------------------
        f = open('outputs_NormTabSQLify/wtq_normtabsqlify.csv', 'a')
        writer = csv.writer(f)
        # header = ['id', 'question', 'answer', 'prediction', 'sql', 'response',  'r_num_cell', 't_num_cell']
        # writer.writerow(header)
        # ---------------------------------------------------------------

        for i, l in enumerate(f1):
            if i in table_ids:
                dic = json.loads(l)
                ids = dic['ids']
                title = dic['title']
                table = dic['norm_table']
                question = dic['statement']
                answer = dic['answer']
                answer = ','.join(answer)
                answer = answer.lower()
                print('\n\nid: ', ids, ' Q: ', question, ' ans: ', answer)

                # T = dict2df(table)
                T = parse_table(table)
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
                engine = create_engine('sqlite:///database.db')
                # T = prepare_df_for_neuraldb_from_table(table)
                T = convert_df_type(T) # normalization


                if tabsqlify == True:
                    sql_3 = """select * from T limit 3"""
                    three_row = sqldf(sql_3, locals())
                    three_row = table_linearization(three_row, style='pipe')
                    # print('\nThree example rows: \n', str(three_row))

                    sql, result, response, output_ans, linear_table = tabsqlify_wtq(T, title, tab_col, question, three_row, selection='rc')

                    t_num_cell = T.size
                    r_num_cell = result.size
                    print('R num_cell: ', r_num_cell, 'T num_cell: ', t_num_cell)

                else:
                    linear_table = table_linearization(T, style='pipe')
                    prompt_ans = gen_full_table_prompt(title, tab_col, linear_table, question)
                    # print(prompt_ans)
                    response = get_answer(prompt_ans)

                    try:
                        output_ans = response.split("Answer:")[1]
                        # print('Output answer: ', output_ans)
                    except:
                        print("Error: Answer generation.")
                        output_ans = "" + response
                    match = re.search(r'(The|the) answer is ([^\.]+)\.$', output_ans)
                    if match:
                        output_ans = match.group(2).strip('"')
                    t_num_cell = T.size
                    r_num_cell = T.size
                    sql = 'select * from T;'


                output_ans = output_ans.lower()
                print('\nResponse: ', response, '\nGen output: ', output_ans, 'Gold: ', answer)
                if output_ans.strip() == answer or output_ans.strip().find(answer) != -1 \
                        or answer.strip().find(output_ans.strip()) != -1:
                    correct += 1
                    print("correct: ", correct)

                t_samples += 1

                print('Correcet: ', correct, 'total: ', t_samples, "Accuracy: ", correct / (t_samples + 0.0001))

                # ---------------------------------------------------------------------------------------------------------
                tmp = {'key': ids, 'question': question, 'response': response, 'prediction': output_ans, 'answer': answer}
                fw.write(json.dumps(tmp) + '\n')
                # #
                data = [ids, question, answer, output_ans.strip(), sql, response,  r_num_cell, t_num_cell]
                writer.writerow(data)

                # tmp = {'statement': dic['statement'], 'table_text': output_table_text, 'answer': dic['answer'], 'id': id, 'title': title}
                # fw.write(json.dumps(tmp) + '\n')
                # ---------------------------------------------------------------------------------------------------------

    f.close()
    fw.close()
    print('Final: Correcet: ', correct, 'total: ', t_samples, "Accuracy: ", correct / (t_samples + 0.0001))
    print('empty_error_ids: ', empty_error_ids)
# ----------------------------------------------------------------------------------------------

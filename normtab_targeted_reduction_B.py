
# Calculate table cells reduction


import sqlite3
from utils.preprocess import *
from utils.normalizer import *
from utils.all_prompts import *
from utils.llm_agent import *
import time
import csv

# ---------------------------------------------------------------
def get_ans_sql(prompt):
    response = None
    while response is None:
        try:
            response = get_completion(prompt, temperature=0.7, max_tokens = 200)
        except:
            time.sleep(2)
            pass
    return response

# ---------------------------------------------------------------
if __name__ == "__main__":

    # norm_table_path = "outputs_B/normTab_wtq_basic_may25.csv"
    # norm_table_path = "outputs_GPT4/normTab_basic_wtq_gpt4.csv"

    # norm_table_path = 'outputs_C/normTab_targeted_wtq_june10_f.csv'

    norm_table_path = "outputs_reduction_cells/normTab_targeted_tf_jul_a.csv"

    # norm_table_path = "analysis/normTab_wtq_apr21.csv"
    # -----------------------------------------------------------------------------------------------------------
    tab_group_path = "datasets/table_group_wtq.json"
    with open(tab_group_path, "r") as file:
        table_qa_group = json.load(file)

    # print(table_qa_group)

    df = pd.read_csv(norm_table_path)
    number_of_tables = df.shape[0]

    wikitq_path = 'datasets/wtq_test3.jsonl'
    unique_tabs = [x for x in range(0, number_of_tables)]

    conn = sqlite3.connect('table.db')


    # ----------------------------------------------------------------------------------------------------------
    start = 0
    end = 400

    # f = open('outputs_reduction_cells/normtab_t_reduction_wtq_jul29.csv', 'a')
    f = open('outputs_reduction_cells/normtab_t_reduction_tf_jul29.csv', 'a')
    writer = csv.writer(f)

    header = ['id', 'norm_tab', 'num_rows', 'num_columns', 'total_cells', 'columns', 'num_column_items', 'total_column_cells']
    writer.writerow(header)
    # ---------------------------------------------------------------
    counter = start - 1

    # print('Counter: ', counter)

    for index, row in df.iterrows():
        if index in unique_tabs[start:end]:
            id = row['id']
            norm_tab = row['norm_table']

            columns = row['columns']

            print('Columns: ', columns)

            # print(norm_tab)
            # norm_tab = str(norm_tab).strip().split('=')[1]
            print('ID: ', id)
            # df = parse_table(norm_tab)
            # print("\n Markdown Table (NormTab):\n", df.to_markdown(index=False))

            counter += 1
            print('Counter: ', counter)

            try:
                df = parse_table(norm_tab)
                # print("\n Markdown Table (NormTab):\n", df.to_markdown(index=False))

                num_rows = df.shape[0]
                num_columns = df.shape[1]

                print('num_row: ', num_rows, 'num_col: ', num_columns)

                total_cells = num_rows * num_columns
                print('total_cells: ', total_cells)

                # Convert 'column' string to a list
                column_list = ast.literal_eval(columns)

                # Count the number of items in 'column'
                num_column_items = len(column_list)

                print('num_col_items: ', num_column_items)
                # Calculate the number of cells for 'column'
                total_column_cells = num_rows * num_column_items

                print('Total cells: ', total_cells, 't_cells: ', total_column_cells)

                # col = df.columns
                # print('Table Coll: ', col)
                #
                # tab_col = ""
                # for c in col:
                #     tab_col += c + ", "
                # tab_col = tab_col.strip().strip(',')
                # print('\nTable Column: ', tab_col)
                print('-----------------------------------\n')
            except:
                print("error\n")
                continue

            data = [id, norm_tab, num_rows, num_columns, total_cells, columns, num_column_items, total_column_cells]
            writer.writerow(data)

    f.close()
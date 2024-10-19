import csv

from pandasql import sqldf
from sqlalchemy import create_engine
from utils.preprocess import *
from utils.normalizer import *
from utils.all_prompts import *
from utils.llm_agent import *
import json
import time
from ast import literal_eval
# ---------------------------------------------------------------

def get_normtab_response(title, table, mode = "targeted"):

    if mode == "basic":
        prompt = generate_normtab_prompt_basic(title, table)
    elif mode == "targeted":
        prompt = generate_normtab_prompt_targeted(title, table)

    response = None
    while response is None:
        try:
            response = get_completion(prompt, temperature=0.7, max_tokens=4000)
        except:
            time.sleep(2)
            pass
    return response

def select_columns(title, three_rows, tab_col):
    prompt = generate_col_prompt(title, three_rows, tab_col)
    # print('\n\nCol Selection prompt: \n', prompt)
    response = None
    while response is None:
        try:
            response = get_completion(prompt, temperature=0.5, max_tokens=100)
        except:
            time.sleep(2)
            pass
    return response

def run_normtab_basic(table):
    # ----------------- NormTab -------------------------------------
    original_table_markdown = table.to_markdown(index=False)
    print('Table Markdown:\n', original_table_markdown)
    norm_table = pd.DataFrame()

    try:
        norm_table = get_normtab_response(title,original_table_markdown, mode="basic")
        # norm_table = get_response_normtab_basic(title, original_table_markdown)
        # print('response: \n', norm_tab)
        norm_table = str(norm_table).strip().split('=')[1]
        # print(ids, norm_table)

        norm_table_df = parse_table(norm_table)
        # norm_table_markdown = norm_table_df.to_markdown(index=False)
        # print("\nNormalized Table (NormTab):\n", norm_table_markdown)
    except:
        print("NormTab Error.")

    return norm_table_df

def run_normtab_targeted(table):
    # ----------------- Col Selection and Extract Table == Step 1-------------------------------
    T = table
    col = T.columns

    tab_col = ""
    for c in col:
        tab_col += c + ", "
    tab_col = tab_col.strip().strip(',')
    print('Table Columns: ', tab_col)

    # ------------------------------- Three Sample Rows -----------------------------------------------
    engine = create_engine('sqlite:///normtab_tf.db')

    query = "SELECT * FROM T limit 3"
    three_rows = sqldf(query, locals())
    three_rows = table_linearization(three_rows, style='pipe')
    # print("\nThree Rows:\n", three_rows)
    # print('----------------------------------------\n')

    norm_tab_col = select_columns(title, three_rows, tab_col)
    norm_tab_col = str(norm_tab_col).strip().split('=')[1]

    print('\nColumn Selection (Step 1): ', norm_tab_col, type(norm_tab_col))

    extracted_subtable = pd.DataFrame()
    remaining_subtable = pd.DataFrame()

    try:
        extracted_subtable, remaining_subtable = split_table(T, norm_tab_col)
        # print("Extracted subtable: \n", extracted_subtable.to_markdown(index=False))
    except:
        print("Col Extraction Error")
        return

    print('-------------------------\n')

    # -------------------------------------------- NormTab = Step 2-----------------------------------------------
    extracted_subtable_markdown = extracted_subtable.to_markdown(index=False)

    print('\nExtracted Table Markdown:\n', extracted_subtable_markdown)
    print("\nRemaining subtable: \n", remaining_subtable.to_markdown(index=False))

    norm_subtable = pd.DataFrame()
    if not extracted_subtable.empty:
        print("not empty.")
        try:
            norm_subtable = get_normtab_response(title, extracted_subtable_markdown,mode="targeted")
            # print('response: \n', norm_subtable)
            norm_subtable = str(norm_subtable).strip().split('=')[1]
            # print(ids, norm_tab)

            norm_subtable = parse_table(norm_subtable)
            print("\nNormalized Subtable (NormTab) Step 2:\n", norm_subtable.to_markdown(index=False))
        except:
            print("NormTab Error.")

    # ---------------------- Merge------------------------------------

    merged_norm_table_df = pd.concat([remaining_subtable, norm_subtable], axis=1)
    merged_norm_table_markdown = merged_norm_table_df.to_markdown(index=False)
    print("\nMerged Table (Normalized) Step 2::\n", merged_norm_table_markdown)

    print('\n*****************************************\n')

    # ---------------------- Postprocessing == Step 3 Last Row and Transpose -------------------------------

    last_row = merged_norm_table_df.iloc[-1].tolist()

    ignore_last_row = detect_ignore_last_row(str(last_row))

    if ignore_last_row:
        merged_norm_table_df = merged_norm_table_df.iloc[:-1]

        print('Ignored last row: ', merged_norm_table_df.to_markdown(index=False))

    print('\n*****************************************\n')

    # -------------------------------- Transposition -------------------------------
    need_transposition = transpose_table_detector(merged_norm_table_df, title)

    # need_transposition = False
    print("Need transposition: ", need_transposition)
    if need_transposition:
        transposed_table = transpose_table_df(merged_norm_table_df)
        modified_merged_norm_table_df = transposed_table
    else:
        modified_merged_norm_table_df = merged_norm_table_df
    # -------------------------------------------------------------------------------

    return norm_tab_col, merged_norm_table_df, modified_merged_norm_table_df
# ---------------------------------------------------------------

def split_table(table, column_string):
    column_list = literal_eval(column_string)

    extracted_subtable = table.loc[:, column_list]

    remaining_columns = [col for col in table.columns if col not in column_list]

    remaining_subtable = table[remaining_columns]

    return extracted_subtable, remaining_subtable

def df_to_list_of_lists(df):
    header = df.columns.tolist()
    data = df.values.tolist()
    return [header] + data

# ---------------------------------------------------------------

if __name__ == "__main__":

    tf_path = "datasets/tabfact_small_test.jsonl"
    # total number of unique table:  298

    start = 0
    end = start + 10

    table_ids = UNIQUE_TAB_IDS_TF[start:end]
    # -------------------------Read/Write File--------------------------------
    
    f = open('sample_outputs/normTab_basic_tf_gpt3.5_turbo.csv', 'a')
    writer = csv.writer(f)

    # header = ['id', 'table title', 'original_tab', 'norm_table_markdown', 'norm_table']
    header = ['id', 'table title', 'original_tab', 'norm_table_markdown', 'norm_table', 'columns'] # for targeted 
    writer.writerow(header)
    # ----------------------------------------------------------------------------------------------------------------
    counter = start

    # normtab_mode = "basic"
    normtab_mode = "targeted"


    with open(tf_path, encoding='utf-8') as f1:
        for i, l in enumerate(f1):
            if i in table_ids:
                dic = json.loads(l)
                ids = dic['table_id']
                title = dic['table_caption']
                table = dic['table_text']
                statement = dic['statement']
                label = dic['label']

                print('\n\nid: ', ids, ' Title: ', title)

                # ----------------- ------------------- ------------------------------------------
                T = dict2df(table)

                original_table_markdown = T.to_markdown(index=False)

                counter += 1
                print('\ncounter : ', counter)

                if normtab_mode == "basic":

                    try:
                        norm_table_df = run_normtab_basic(T)

                        norm_table_markdown = norm_table_df.to_markdown(index=False)
                        print("norm_tab_markdown: \n", norm_table_markdown)

                        norm_table = df_to_list_of_lists(norm_table_df)
                        print("norm_tab_list: \n", norm_table)
                        print('\n*****************************************\n')

                        data = [ids, title, original_table_markdown, norm_table_markdown, norm_table]
                    except:
                        print("NormTba Error.")
                        continue

                elif normtab_mode == "targeted":

                    try:
                        norm_tab_col, merged_norm_table_df, modified_merged_norm_table_df = run_normtab_targeted(T)

                        print("norm tab col: ", norm_tab_col)

                        merged_norm_table = df_to_list_of_lists(merged_norm_table_df)
                        print("Final merged norm_tab: \n", merged_norm_table)

                        merged_norm_table_markdown = merged_norm_table_df.to_markdown(index=False)
                        print("merged_norm_table_markdown: \n", merged_norm_table_markdown)

                        modified_merged_norm_table = df_to_list_of_lists(merged_norm_table_df)
                        print("Final merged norm_tab: \n", modified_merged_norm_table)

                        modified_merged_norm_table_markdown = modified_merged_norm_table_df.to_markdown(index=False)
                        print("\nModified Merged table (Step 3): \n", modified_merged_norm_table_markdown)
                        print('\n*****************************************\n')
                        data = [ids, title, original_table_markdown, merged_norm_table_markdown, merged_norm_table,
                                norm_tab_col]

                    except:
                        print("NormTab Error.")
                        continue

                # ---------------------- write responses --------------------------

                writer.writerow(data)

    f.close()


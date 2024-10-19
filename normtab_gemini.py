from utils.llm_agent import *

prompt = """ You are an advanced AI capable of analyzing and understanding information within tables. Read the first row and first column of table reagradingFigure skating at the Asian Winter GamesHeadings of a table are labels or titles given to rows or columns to provide a brief description of the data they contain. Based on the given table, the headings of the table are more likely to be:
(A): (rank, nation, gold, silver, bronze, total)
(B): (rank, 1, 2, 3, 4, 5, 6)

Directly give your choice. Ensure the format is only "(A) or (B)" form, no other form, without any explanation.
response:"""

prompt_select_col_1 = """
You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize a web table so that it can be converted as a relational database table. 

### Instructions:
Identify the columns based on the following instruction 
1. identify the columns If some of the values of a column needed to be splitted or extracted then extract the string and add it in new columns.
2. identify the columns that has date type value and the numerical value. 
3. identify the columns that has numerical values containing extra string such as ‘$’ or units.
4. indetify the columns that has ‘N/A’,  blank or null.
5. Identify the columns that contain ranges  such as (20-2), 2010/11, 2015-2018 etc.

### Task: Your task is to identify which columns needed to be  normalized to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table.

### Table: 
Read the table below regarding "2008 Clásica de San Sebastián" 

rank | cyclist | team | time | uci_protour_points
1 | alejandro valverde (esp) | caisse d'epargne | 5h 29' 10" | 40
2 | alexandr kolobnev (rus) | team csc saxo bank | s.t. | 30
3 | davide rebellin (ita) | gerolsteiner | s.t. | 25

Table Coll: (rank, cyclist, team, time, uci_protour_points)

### Response: normalize_coll = ['cyclist']

### Table:
Read the table below regarding "Sky Track Cycling"

date | competition | location | country | event | placing | rider | nationality
31 october 2008 | 2008–09 world cup | manchester | united kingdom | sprint | 1 | victoria pendleton | gbr
31 october 2008 | 2008–09 world cup | manchester | united kingdom | keirin | 2 | jason kenny | gbr
1 november 2008 | 2008–09 world cup | manchester | united kingdom | sprint | 1 | jason kenny | gbr

Table Coll: (date, competition, location, country, event, placing, rider, nationality)

### Response: normalize_coll = ['date', 'competition']

### Table:
Read the table below regarding "1981 Houston Oilers season

row_number | week | date | opponent | result | attendance
0 | 1 | september 6, 1981 | at los angeles rams | w 27–20 | 63,198
1 | 2 | september 13, 1981 | at cleveland browns | w 9–3 | 79,483
2 | 3 | september 20, 1981 | miami dolphins | l 16–10 | 47,379

Table Coll: (week, date, opponent, result, attendance)

### Response: normalize_coll = 
"""

prompt_normtab = """### Task: 
You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize the structure and the values of each cell to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table.

### Instructions:
1. If the last row has any information like aggregated rows such as ‘total’, ‘sum’ or average’, ignore this row.
2. If some of the values needed to be splitted or extracted then extract the string and add it in new columns.
3. Make sure the dateType and the numerical value is normalized to a uniform format (YYYY-MM-DD). Be cautious of numerical values that contain any extra string such as ‘$’ or units.
4. Normalize the ‘N/A’ values to blank or null.
5. Handle the columns that contain ranges  such as (20-2), 2010/11, 2015-2018 etc  to  two separate columns.
6. Never delete any columns or rows.
7. Never add any aditional row. 

### Input Table: 
Table Markdown:
 | tie_no   | home_team               | score   | away_team            | date            | attendance   |
|:---------|:------------------------|:--------|:---------------------|:----------------|:-------------|
| 1        | rochdale                | 2 – 0   | coventry city        | 25 january 2003 |              |
| 2        | southampton             | 1 – 1   | millwall             | 25 january 2003 | 23,809       |
| replay   | millwall                | 1 – 2   | southampton          | 5 february 2003 | 10,197       |
| 3        | watford                 | 1 – 0   | west bromwich albion | 25 january 2003 | 16,975       |
| 4        | walsall                 | 2 – 0   | wimbledon            | 25 january 2003 | 6,693        |
| 5        | gillingham              | 1 – 1   | leeds united         | 25 january 2003 | 11,093       |
| replay   | leeds united            | 2 – 1   | gillingham           | 4 february 2003 | 29,359       |
| 6        | blackburn rovers        | 3 – 3   | sunderland           | 25 january 2003 | 14,315       |
| replay   | sunderland              | 2 – 2   | blackburn rovers     | 5 february 2003 | 15,745       |
| 7        | wolverhampton wanderers | 4 – 1   | leicester city       | 25 january 2003 | 28,164       |
| 8        | shrewsbury town         | 0 – 4   | chelsea              | 26 january 2003 | 7,950        |
| 9        | sheffield united        | 4 – 3   | ipswich town         | 25 january 2003 | 12,757       |
| 10       | fulham                  | 3 – 0   | charlton athletic    | 26 january 2003 | 12,203       |
| 11       | brentford               | 0 – 3   | burnley              | 25 january 2003 | 9,563        |
| 12       | manchester united       | 6 – 0   | west ham united      | 26 january 2003 | 67,181       |
| 13       | norwich city            | 1 – 0   | dagenham & redbridge | 25 january 2003 | 21,164       |
| 14       | crystal palace          | 0 – 0   | liverpool            | 26 january 2003 | 26,054       |
| replay   | liverpool               | 0 – 2   | crystal palace       | 5 february 2003 | 35,109       |
| 15       | farnborough town        | 1 – 5   | arsenal              | 25 january 2003 | 35,108       |
| 16       | stoke city              | 3 – 0   | bournemouth          | 26 january 2003 | 12,004       |

### Output: Let's think step by step, and generate the final output table based on the instructions without any explanation. Ensure the final output is only “normalized_table = [[col1, col2, col3,…], [row11, row 12, row13,.....],....]” form, no other form.
### Response: normalized_table = 
"""


response = get_completion_gemmini(prompt_select_col_1)
print(response)

response = get_completion_gemmini(prompt_normtab)
print(response)

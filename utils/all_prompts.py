from utils.llm_agent import *


# Unique table ids - wtq
UNIQUE_TAB_IDS_WTQ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54,
                      55, 57, 58, 59, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                      86, 87, 88, 89, 90, 92, 94, 95, 97, 98, 99, 100, 101, 104, 106, 107, 108, 110, 111, 112, 114, 115,
                      116, 117, 118, 119, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 132, 133, 134, 135, 136,
                      137, 139, 140, 142, 143, 145, 146, 147, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
                      160, 161, 164, 166, 168, 170, 172, 173, 174, 175, 177, 178, 179, 180, 182, 187, 188, 190, 191,
                      193, 194, 195, 197, 198, 199, 200, 202, 203, 204, 205, 206, 208, 209, 210, 212, 213, 214, 215,
                      216, 217, 218, 221, 222, 224, 225, 226, 228, 231, 239, 240, 241, 242, 247, 250, 252, 254, 256,
                      258, 259, 260, 261, 262, 264, 266, 267, 268, 269, 273, 277, 279, 280, 281, 286, 291, 292, 297,
                      300, 301, 304, 307, 310, 313, 316, 319, 320, 324, 325, 326, 327, 332, 334, 335, 340, 341, 342,
                      343, 345, 346, 347, 348, 349, 352, 357, 358, 363, 366, 367, 368, 375, 380, 382, 387, 389, 396,
                      398, 403, 410, 412, 413, 417, 418, 420, 421, 423, 425, 431, 432, 434, 438, 441, 443, 444, 450,
                      455, 457, 462, 463, 469, 473, 474, 476, 478, 479, 481, 484, 485, 490, 492, 494, 497, 499, 504,
                      515, 516, 519, 523, 525, 530, 533, 535, 538, 539, 545, 546, 547, 552, 553, 555, 557, 560, 564,
                      571, 572, 582, 600, 602, 613, 620, 625, 628, 634, 635, 638, 639, 651, 659, 662, 666, 668, 673,
                      675, 676, 683, 685, 688, 689, 691, 711, 713, 714, 717, 718, 723, 737, 750, 759, 767, 768, 769,
                      772, 775, 801, 810, 824, 836, 848, 850, 857, 859, 861, 866, 868, 878, 884, 887, 899, 920, 921,
                      975, 982, 996, 999, 1011, 1043, 1054, 1056, 1078, 1098, 1100, 1103, 1136, 1138, 1157, 1172, 1189,
                      1199, 1226, 1273, 1278, 1283, 1285, 1298, 1304, 1338, 1416, 1435, 1487, 1500, 1507, 1520, 1559,
                      1572, 1575, 1606, 1636, 1652, 1834, 1979, 2019, 2076, 2167, 2345, 2388, 2540, 2556, 2834, 2844,
                      2901, 2935, 3112, 3523]
# ---------------------------------------------------------------------------------------------------------------------
# Unique table ids - tf
UNIQUE_TAB_IDS_TF = [0, 10, 11, 15, 25, 35, 45, 47, 57, 61, 66, 78, 82, 91, 101, 106, 114, 124, 135, 139, 143, 153,
                        163, 173, 181, 183, 186, 195, 205, 213, 214, 225, 229, 231, 241, 244, 254, 264, 274, 284, 294,
                        298, 303, 312, 322, 328, 331, 341, 351, 357, 359, 369, 376, 383, 385, 390, 400, 410, 414, 416,
                        426, 433, 443, 453, 462, 476, 480, 490, 498, 500, 503, 510, 512, 516, 526, 536, 540, 544, 548,
                        551, 561, 581, 591, 601, 604, 614, 623, 626, 643, 653, 660, 661, 671, 675, 690, 697, 699, 704,
                        714, 724, 729, 730, 740, 744, 754, 766, 770, 774, 780, 785, 796, 806, 816, 826, 836, 845, 855,
                        865, 875, 885, 889, 891, 892, 895, 904, 914, 923, 927, 939, 941, 942, 949, 951, 954, 958, 962,
                        966, 970, 980, 988, 998, 1004, 1012, 1018, 1020, 1026, 1033, 1035, 1037, 1047, 1052, 1055, 1063,
                        1066, 1076, 1086, 1088, 1098, 1108, 1119, 1128, 1138, 1145, 1148, 1149, 1155, 1165, 1167, 1173,
                        1180, 1183, 1187, 1197, 1201, 1204, 1211, 1217, 1227, 1237, 1245, 1247, 1250, 1260, 1270, 1280,
                        1288, 1292, 1302, 1307, 1315, 1330, 1340, 1349, 1350, 1352, 1354, 1362, 1372, 1381, 1384, 1394,
                        1399, 1400, 1410, 1414, 1417, 1427, 1437, 1445, 1449, 1455, 1465, 1474, 1479, 1481, 1491, 1493,
                        1503, 1513, 1523, 1524, 1529, 1531, 1535, 1540, 1550, 1559, 1567, 1577, 1580, 1587, 1597, 1601,
                        1611, 1613, 1617, 1622, 1632, 1642, 1644, 1654, 1656, 1658, 1661, 1671, 1681, 1690, 1693, 1700,
                        1709, 1715, 1722, 1730, 1734, 1738, 1750, 1760, 1763, 1773, 1785, 1796, 1798, 1805, 1815, 1821,
                        1825, 1829, 1834, 1835, 1843, 1848, 1857, 1867, 1877, 1879, 1881, 1885, 1886, 1890, 1892, 1894,
                        1904, 1914, 1922, 1926, 1936, 1943, 1948, 1958, 1962, 1970, 1972, 1982, 1992, 1999, 2000, 2005,
                        2015]
# ---------------------------------------------------------------------------------------------------------------------

prompt_select_col= """
You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize a web table so that it can be converted as a relational database table. Read the table below regarding "Sky Track Cycling"
### Table:
date | competition | location | country | event | placing | rider | nationality
31 october 2008 | 2008–09 world cup | manchester | united kingdom | sprint | 1 | victoria pendleton | gbr
31 october 2008 | 2008–09 world cup | manchester | united kingdom | keirin | 2 | jason kenny | gbr
1 november 2008 | 2008–09 world cup | manchester | united kingdom | sprint | 1 | jason kenny | gbr
Table Coll: (date, competition, location, country, event, placing, rider, nationality)

 Task: Your task is to identify which columns needed to be  normalized to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table.

### Instructions:
Identify the columns based on the following instruction 
1. identify the columns If some of the values of a column needed to be splitted or extracted then extract the string and add it in new columns.
2. identify the columns that has date type value and the numerical value. 
3. identify the columns that has numerical values containing extra string such as ‘$’ or units.
4. indetify the columns that has ‘N/A’,  blank or null.
5. Identify the columns that contain ranges  such as (20-2), 2010/11, 2015-2018 etc.
### Output: Let's think step by step, and generate the final output based on the instructions without any explanation. Ensure the final output is only “normalize_coll = [col1, col2, col3,…]”form, no other form.
### Response: normalize_coll = ['date', 'competition']

You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize a web table so that it can be converted as a relational database table. Read the table below regarding "My Brother and Me"
### Table:
series__ | season__ | title | notes | original_air_date
1 | 1 | "the charity" | alfie, dee dee, and melanie are supposed to be helping their parents at a carnival by working the dunking booth. when goo arrives and announces their favorite basketball player, kendall gill, is at the comic book store signing autographs, the boys decide to ditch the carnival. this leaves melanie and jennifer to work the booth and both end up soaked. but the comic book store is packed and much to alfie and dee dee's surprise their father has to interview kendall gill. goo comes up with a plan to get alfie and dee dee, gill's signature before getting them back at the local carnival, but are caught by roger. all ends well for everyone except alfie and goo, who must endure being soaked at the dunking booth. | october 15, 1994
2 | 1 | "the practical joke war" | alfie and goo unleash harsh practical jokes on dee dee and his friends. dee dee, harry and donnel retaliate by pulling a practical joke on alfie with the trick gum. after alfie and goo get even with dee dee and his friends, melanie and deonne help them get even. soon, alfie and goo declare a practical joke war on melanie, dee dee and their friends. this eventually stops when roger and jennifer end up on the wrong end of the practical joke war after being announced as the winner of a magazine contest for best family of the year. they set their children straight for their behavior and will have a talk with their friends' parents as well. | october 22, 1994
3 | 1 | "the weekend aunt helen came" | the boy's mother, jennifer, leaves for the weekend and she leaves the father, roger, in charge. however, he lets the kids run wild. alfie and dee dee's aunt helen then comes to oversee the house until jennifer gets back. meanwhile, alfie throws a basketball at goo, which hits him in the head, giving him temporary amnesia. in this case of memory loss, goo acts like a nerd, does homework on a weekend, wants to be called milton instead of goo, and he even calls alfie alfred. he is much nicer to deonne and dee dee, but is somewhat rude to melanie. the only thing that will reverse this is another hit in the head. | november 1, 1994
Table Coll: (series__, season__, title, notes, original_air_date)

 Task: Your task is to identify which columns needed to be  normalized to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table.

### Instructions:
Identify the columns based on the following instruction 
1. identify the columns If some of the values of a column needed to be splitted or extracted then extract the string and add it in new columns.
2. identify the columns that has date type value and the numerical value. 
3. identify the columns that has numerical values containing extra string such as ‘$’ or units.
4. indetify the columns that has ‘N/A’,  blank or null.
5. Identify the columns that contain ranges  such as (20-2), 2010/11, 2015-2018 etc.
### Output: Let's think step by step, and generate the final output based on the instructions without any explanation. Ensure the final output is only “normalized_coll = [col1, col2, col3,…]”form, no other form.
### Response: normalize_coll = ['original_air_date']

You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize a web table so that it can be converted as a relational database table. Read the table below regarding "Britain's Got Talent"
### Table:
series | premiere | finale | winner | runner_up | third_place | hosts | judging_panel | guest_judges
one | 9 june 2007 | 17 june 2007 | paul potts | damon scott | connie talbot | ant & dec | simon cowell\namanda holden\npiers morgan | n/a
two | 12 april 2008 | 31 may 2008 | george sampson | signature | andrew johnston | ant & dec | simon cowell\namanda holden\npiers morgan | n/a
three | 11 april 2009 | 30 may 2009 | diversity | susan boyle | julian smith | ant & dec | simon cowell\namanda holden\npiers morgan | kelly brook
Table Coll: (series, premiere, finale, winner, runner_up, third_place, hosts, judging_panel, guest_judges)

 Task: Your task is to identify which columns needed to be  normalized to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table.

### Instructions:
Identify the columns based on the following instruction 
1. identify the columns If some of the values of a column needed to be splitted or extracted then extract the string and add it in new columns.
2. identify the columns that has date type value and the numerical value. 
3. identify the columns that has numerical values containing extra string such as ‘$’ or units.
4. indetify the columns that has ‘N/A’,  blank or null.
5. Identify the columns that contain ranges  such as (20-2), 2010/11, 2015-2018 etc.
### Output: Let's think step by step, and generate the final output based on the instructions without any explanation. Ensure the final output is only “normalize_coll = [col1, col2, col3,…]”form, no other form.
### Response: normalize_coll = ['premiere', 'finale', 'guest_judges']
"""

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

### Response: normalize_coll = [date, 'result', 'attendance']
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

"""

prompt_normtab_2 = """ You are an expert in data normalization and cleaning. Below is a table in Markdown format. Your task is to clean and normalize the table data to ensure uniformity and accuracy. Follow these steps:

1. **Identify Noise and Inconsistencies**:
    - Detect and remove any extraneous characters or symbols.
    - Identify and correct inconsistent data formats (e.g., dates, numbers).

2. **Normalize Values**:
    - Standardize date formats to `YYYY-MM-DD`.
    - Ensure all numeric values are free of commas and formatted correctly.
    - Convert textual data to a consistent case (e.g., all lowercase).

3. **Uniformity**:
    - Ensure all similar categories have a single consistent representation.
    - Handle any missing values appropriately, using placeholders or inferred values if necessary.

**Example 1:**

**Original Table:**

```
| Institution        | Location      | Endowment   |
|--------------------|---------------|-------------|
| Harvard University | Cambridge, MA | $32.3 billion |
| Yale University    | New Haven, CT | $20.8 billion |
| Princeton University| Princeton, NJ | $18.2 billion |
```

**Normalized Table:**

```
| Institution          | Location                | Endowment       |
|----------------------|-------------------------|-----------------|
| Harvard University   | Cambridge, Massachusetts| 32300000000     |
| Yale University      | New Haven, Connecticut  | 20800000000     |
| Princeton University | Princeton, New Jersey   | 18200000000     |
```

**Example 2:**

**Original Table:**

```
| Date         | Revenue    |
|--------------|------------|
| 01/15/2023   | $1,000.50  |
| 2023-02-15   | $2,000.75  |
| March 3, 2023| $3,500.25  |
```

**Normalized Table:**

```
| Date       | Revenue    |
|------------|------------|
| 2023-01-15 | 1000.50    |
| 2023-02-15 | 2000.75    |
| 2023-03-03 | 3500.25    |
```

**Your Task:**

Below is another table that requires cleaning and normalization. Follow the steps mentioned above and provide the cleaned and normalized table.

"""

p_sql_three_wtq = """Generate SQL with no explanation given the question and table to answer the question correctly.

SQLite table properties:

Table: Marek Plawgo(row_number,year,competition,venue,position,event,notes)

3 example rows: 
 select * from T limit 3;
row_number | year | competition | venue | position | event | notes
0 | 1999 | european junior championships | riga, latvia | 4th | 400 m hurdles | 52.17
1 | 2000 | world junior championships | santiago, chile | 1st | 400 m hurdles | 49.23
2 | 2001 | world championships | edmonton, canada | 18th (sf) | 400 m hurdles | 49.8

Q: when was his first 1st place record?
SQL: select year from T where position = '1st' order by year asc limit 1

SQLite table properties:

Table: 2013\u201314 Toros Mexico season(row_number,game,day,date,kickoff,opponent,results_score,results_record,location,attendance)

3 example rows: 
 select * from T limit 3;
row_number | game | day | date | kickoff | opponent | results_score | results_record | location | attendance
0 | 1 | sunday | november 10 | t15:5 | at las vegas legends | l 3–7 | 0–1 | orleans arena | 1836
1 | 2 | sunday | november 17 | t13:5 | monterrey flash | l 6–10 | 0–2 | unisantos park | 363
2 | 3 | saturday | november 23 | t19:5 | at bay area rosal | w 10–7 | 1–2 | cabernet indoor sports | 652

Q: what was the number of people attending the toros mexico vs. monterrey flash game?
SQL: select attendance from T where opponent like '%monterrey flash%'

SQLite table properties:

Table: Radhika Pandit(row_number,year,film,role,language,notes)

3 example rows: 
 select * from T limit 3;
row_number | year | film | role | language | notes
0 | 2008 | moggina manasu | chanchala | kannada | filmfare award for best actress - kannada; karnataka state film award for best actress
1 | 2009 | olave jeevana lekkachaara | rukmini | kannada | innovative film award for best actress
2 | 2009 | love guru | kushi | kannada | filmfare award for best actress - kannada

Q: what is the total number of films with the language of kannada listed?
SQL: select count(film) from T where language like '%kannada%'

SQLite table properties:

Table: List of storms on the Great Lakes(row_number,ship,type_of_vessel,lake,location,lives_lost)

3 example rows: 
 select * from T limit 3;
row_number | ship | type_of_vessel | lake | location | lives_lost
0 | argus | steamer | lake huron | 25 miles off kincardine, ontario | 25 lost
1 | james carruthers | steamer | lake huron | near kincardine | 18 lost
2 | hydrus | steamer | lake huron | near lexington, michigan | 28 lost

Q: how many more ships were wrecked in lake huron than in erie?
SQL: select ((select count(ship) from T where lake like '%lake huron%') - (select count(ship) from T where lake like '%lake erie%'))

SQLite table properties:

Table: Vidant Bertie Hospital(row_number,name,city,hospital_beds,operating_rooms,total,trauma_designation,affiliation,notes)

3 example rows: 
 select * from T limit 3;
row_number | name | city | hospital_beds | operating_rooms | total | trauma_designation | affiliation | notes
0 | alamance regional medical center | burlington | 238 | 15 | 253 | none | cone | none
1 | albemarle hospital | elizabeth city | 182 | 13 | 195 | none | vidant | none
2 | alexander hospital | hickory | 25 | 3 | 28 | none | none | none

Q: what is the only hospital to have 6 hospital beds?
SQL: select name from T where hospital_beds = 6

SQLite table properties:

Table: Churnet Valley Railway(row_number,number,name,type,livery,status,notes)

3 example rows: 
 select * from T limit 3;
row_number | number | name | type | livery | status | notes
0 | none | brightside | yorkshire engine company 0-4-0 | black | under repair | currently dismantled for overhaul
1 | 6 | roger h. bennett | yorkshire engine company "janus" 0-6-0 | ncb blue | operational | ~
2 | d2334 | none | class 4 | green | under repair | stopped at 2012-9 diesel gala after failure

Q: how many locomotives are currently operational?
SQL: select count(*) from T where status = 'operational'

SQLite table properties:

Table: 2012\u201313 Exeter City F.C. season(row_number,name,league,fa_cup,league_cup,jp_trophy,total)

3 example rows: 
 select * from T limit 3;
row_number | name | league | fa_cup | league_cup | jp_trophy | total
0 | scot bennett | 5 | 0 | 0 | 0 | 5
1 | danny coles | 3 | 0 | 0 | 0 | 3
2 | liam sercombe | 1 | 0 | 0 | 0 | 1

Q: does pat or john have the highest total?
SQL: select name from T where name like '%pat%' or name like '%john%' order by total desc limit 1

SQLite table properties:

Table: The Harvest (Boondox album)(row_number, _, title, time, lyrics, music, producers, performers)

3 example rows: 
 select * from T limit 3;
row_number | _ | title | time | lyrics | music | producers | performers
0 | 1 | "intro" | 1:16 | none | none | none | none
1 | 2 | "7" | 3:30 | boondox | mike e. clark | boondox | boondox
2 | 3 | "out here" | 3:18 | boondox | mike e. clark; tino grosse | boondox | boondox

Q: how many song come after "rollin hard"?
SQL: select count(*) from T where row_number > (select row_number from T where title like '%rollin hard%')

SQLite table properties:

Table: GameStorm.org(row_number, iteration, dates, location, attendance, notes)

3 example rows: 
 select * from T limit 3;
row_number | iteration | dates | location | attendance | notes
0 | gamestorm 10 | 2008-3 | red lion - vancouver, wa | 750 | none
1 | gamestorm 11 | (2009-3-262009-3-29,p3d) | hilton - vancouver, wa | 736 | debut of video games, first-ever artist guest of honor, rob alexander
2 | gamestorm 12 | (2010-3-252010-3-28,p3d) | hilton - vancouver, wa | 802 | board games guest of honor: tom lehmann

Q: what's the total attendance for gamestorm 11?
SQL: select attendance from T where iteration = 'gamestorm 11'


SQLite table properties:

Table: 1981 Iowa Hawkeyes football team(row_number, date, opponent_, rank_, site, tv, result, attendance)

3 example rows: 
 select * from T limit 3;
row_number | date | opponent_ | rank_ | site | tv | result | attendance
0 | september 12 | #7 nebraska* | none | kinnick stadium • iowa city, ia | none | w 10-7 | 60160
1 | september 19 | at iowa state* | none | cyclone stadium • ames, ia (cy-hawk trophy) | none | l 12-23 | 53922
2 | september 26 | #6 ucla* | none | kinnick stadium • iowa city, ia | none | w 20-7 | 60004

Q: which date had the most attendance?
SQL: select date from T order by attendance desc limit 1

"""

p_sql_three_norm_wtq = """
Generate SQL with no explanation given the question and table to answer the question correctly.

### SQLite table properties:

Table: Marek Plawgo(row_number,year,competition,venue,position,event,notes)

3 example rows: 
 select * from T limit 3;
row_number | year | competition | venue | position | event | notes
0 | 1999 | european junior championships | riga, latvia | 4th | 400 m hurdles | 52.17
1 | 2000 | world junior championships | santiago, chile | 1st | 400 m hurdles | 49.23
2 | 2001 | world championships | edmonton, canada | 18th | 400 m hurdles | 49.8

Q: when was his first 1st place record?
SQL: select year from T where position = '1st' order by year asc limit 1

### SQLite table properties:

Table: 1981 Houston Oilers season(row_number, week, opponent, date, result_type, result_score, attendance)

3 example rows: 
 select * from T limit 3;
 row_number | week | opponent | date | result_type | result_score | attendance
0 | 1 | at los angeles rams | 1981-09-06 | w | 27-20 | 63198
1 | 2 | at cleveland browns | 1981-09-13 | w | 9-3 | 79483
2 | 3 | miami dolphins | 1981-09-20 | l | 16-10 | 47379

Q: how may away games did they win?
SQL: select count(*) from T where result_type = 'w'

Q: what was the next opponent after the game against the new england patriots?
SQL: select opponent from T where row_number = (select row_number + 1 from T where opponent like '%new england patriots%')

Q: how many points did they beat the bengals by in week 5? 
SQL: select abs(cast(substr(result_score, 1, 2) as integer) - cast(substr(result_score, 4, 2) as integer)) as point_difference 
from T 
where opponent like '%cincinnati bengals%' and week = 5

Q: how many times did the oilers have consecutive wins?
SQL:  select count(*) from T where result_type = 'w' and row_number in (select row_number + 1 from T where result_type = 'w')

### SQLite table properties:

Table: Figure skating at the Asian Winter Games(row_number, rank, nation, gold, silver, bronze, total)

3 example rows: 
 select * from T limit 3;
 row_number | rank | nation | gold | silver | bronze | total
0 | 1 | china | 13 | 9 | 13 | 35
1 | 2 | japan | 7 | 10 | 7 | 24
2 | 3 | uzbekistan | 1 | 2 | 3 | 6

Q: what is the average number of gold medals won by china, japan, and north korea?
SQL: select avg(gold) from T where nation in ('china', 'japan', 'north korea')

### SQLite table properties:

Table: 1994 Alabama Crimson Tide football team (row_number, opponent, rank, site, tv, date, result_type, result_score, attendance)

3 example rows: 
 select * from T limit 3;
 row_number | opponent | rank | site | tv | date | result_type | result_score | attendance
0 | tennessee–chattanooga* | #11 | legion field • birmingham, al |  | 1994-09-03 | w | 42-13 | 82109
1 | vanderbilt | #11 | bryant–denny stadium • tuscaloosa, al | jps | 1994-09-10 | w | 17-7 | 70123
2 | at arkansas | #12 | razorback stadium • fayetteville, ar | abc | 1994-09-17 | w | 13-6 | 52089

Q: how many games where won with a score of below 20 for the 1994 alabama crimson tide football team?
SQL: select count(*) from T where result_type = 'w' and result_score < 20


"""
# --------------------------------------------------------------------------------------------------------------------

p_sql_three_tabfact = """Generate SQL given the statement and table to verify the statement correctly.

SQLite table properties:

Table: 1947 kentucky wildcats football team(row_number, game, date, opponent, result, wildcats_points, opponents, record)

3 example rows: 
 select * from T limit 3;
row_number | game | date | opponent | result | wildcats_points | opponents | record
0 | 1 | sept 20 | ole miss | loss | 7 | 14 | 0 - 1
1 | 2 | sept 27 | cincinnati | win | 20 | 0 | 1 - 1
2 | 3 | oct 4 | xavier | win | 20 | 7 | 2 - 1

Q: the wildcats kept the opposing team scoreless in four games
SQL: SELECT (SELECT COUNT(*) FROM T WHERE opponents = 0) = 4

SQLite table properties:

Table: césar ramos(row_number, season, series, team, races, wins, poles, f___laps, podiums, points, position)

3 example rows: 
 select * from T limit 3;
row_number | season | series | team | races | wins | poles | f___laps | podiums | points | position
0 | 2007 | formula renault 2 italy | bvm minardi team | 14 | 0 | 0 | 0 | 1 | 106 | 14th
1 | 2007 | eurocup formula renault 2 | bvm minardi team | 6 | 0 | 0 | 0 | 0 | n / a | nc
2 | 2007 | formula renault 2 italy - wi series | bvm minardi team | 4 | 4 | 4 | 4 | 4 | 144 | 1st

Q: every team had several wins
SQL: SELECT (SELECT COUNT(*) FROM T WHERE wins > 0) = (SELECT COUNT(DISTINCT team) FROM T);

SQLite table properties:

Table: katsuya inoue(row_number, res, record, opponent, method, event, round, time, location)

3 example rows: 
 select * from T limit 3;
row_number | res | record | opponent | method | event | round | time | location
0 | loss | 19 - 9 - 4 | naoyuki kotani | submission (armbar) | pancrase - impressive tour 9 | 1 | 1:44 | tokyo , japan
1 | loss | 19 - 8 - 4 | kota okazawa | ko (punch) | pancrase - impressive tour 4 | 1 | 2:42 | tokyo , japan
2 | win | 19 - 7 - 4 | katsuhiko nagata | decision (unanimous) | gcm - cage force 17 | 3 | 5:0 | tokyo , japan

Q: in tokyo , japan , hikaru sato 's match ended before round 2
SQL: SELECT (SELECT COUNT(*) FROM T WHERE location = 'tokyo , japan' AND round < 2) > 0;

SQLite table properties:

Table: 2010 vuelta a colombia(row_number, stage, winner, general_classification, points_classification, mountains_classification, sprints_classification, team_classification)

3 example rows: 
 select * from T limit 3;
row_number | stage | winner | general_classification | points_classification | mountains_classification | sprints_classification | team_classification
0 | 1 | ind ant - idea - fla - lot de medellín | sergio luis henao | no award | no award | no award | ind ant - idea - fla - lot de medellín
1 | 2 | jaime castañeda | óscar sevilla | jaime castañeda | jaime vergara | camilo gómez | ind ant - idea - fla - lot de medellín
2 | 3 | jairo pérez | jairo pérez | jaime castañeda | jaime vergara | julian lopez | ind ant - idea - fla - lot de medellín

Q: sergio luis henao was given the general classification award and the points classification award
SQL: SELECT (SELECT COUNT(*) FROM T WHERE general_classification = 'sergio luis henao' AND points_classification = 'sergio luis henao') > 0;

SQLite table properties:

Table: 1947 kentucky wildcats football team(row_number, game, date, opponent, result, wildcats_points, opponents, record)

3 example rows: 
 select * from T limit 3;
row_number | game | date | opponent | result | wildcats_points | opponents | record
0 | 1 | sept 20 | ole miss | loss | 7 | 14 | 0 - 1
1 | 2 | sept 27 | cincinnati | win | 20 | 0 | 1 - 1
2 | 3 | oct 4 | xavier | win | 20 | 7 | 2 - 1

Q: the wildcats played two games in september , four games in october , and four games in november
SQL: SELECT (SELECT COUNT(*) FROM T WHERE date LIKE 'sept%') = 2 AND (SELECT COUNT(*) FROM T WHERE date LIKE 'oct%') = 4 AND (SELECT COUNT(*) FROM T WHERE date LIKE 'nov%') = 4;

SQLite table properties:

Table: leanne baker(row_number, outcome, date, location, surface, opponent_in_final, score)

3 example rows: 
 select * from T limit 3;
row_number | outcome | date | location | surface | opponent_in_final | score
0 | winner | 1999-5-2 | coatzacoalcos , mexico | hard | candice jairala | 3 - 6 6 - 3 7 - 5
1 | winner | 1999-7-11 | felixstowe , england | grass | karen nugent | 6 - 4 6 - 4
2 | runner - up | 2000-2-6 | wellington , new zealand | hard | mirielle dittmann | 6 - 7 (5) 6 - 1 6 - 7 (5)

Q: mirielle dittmann was the opponent in the final on hard surface on 6 february 2000 in wellington new zealand
SQL: SELECT (SELECT COUNT(*) FROM T WHERE opponent_in_final = 'mirielle dittmann' AND surface = 'hard' AND date = '2000-2-6' AND location = 'wellington , new zealand') > 0;

SQLite table properties:

Table: leanne baker(row_number, outcome, date, location, surface, opponent_in_final, score)

3 example rows: 
 select * from T limit 3;
row_number | outcome | date | location | surface | opponent_in_final | score
0 | winner | 1999-5-2 | coatzacoalcos , mexico | hard | candice jairala | 3 - 6 6 - 3 7 - 5
1 | winner | 1999-7-11 | felixstowe , england | grass | karen nugent | 6 - 4 6 - 4
2 | runner - up | 2000-2-6 | wellington , new zealand | hard | mirielle dittmann | 6 - 7 (5) 6 - 1 6 - 7 (5)

Q: on 2 may 1999 , the surface was hard
SQL: SELECT (SELECT COUNT(*) FROM T WHERE date = '1999-5-2' AND surface = 'hard') > 0;

SQLite table properties:

Table: leanne baker(row_number, outcome, date, location, surface, opponent_in_final, score)

3 example rows: 
 select * from T limit 3;
row_number | outcome | date | location | surface | opponent_in_final | score
0 | winner | 1999-5-2 | coatzacoalcos , mexico | hard | candice jairala | 3 - 6 6 - 3 7 - 5
1 | winner | 1999-7-11 | felixstowe , england | grass | karen nugent | 6 - 4 6 - 4
2 | runner - up | 2000-2-6 | wellington , new zealand | hard | mirielle dittmann | 6 - 7 (5) 6 - 1 6 - 7 (5)

Q: the opponent in final on 6 february 2000 in wellington new zealand on hard surface was katerina kramperová
SQL: SELECT (SELECT COUNT(*) FROM T WHERE date = '2000-2-6' AND location = 'wellington , new zealand' AND surface = 'hard' AND opponent_in_final = 'katerina kramperová') > 0;

"""

# --------------------------------------------------------------------------------------------------------------------
def detect_ignore_last_row(last_row):
    prompt = "You are an advanced AI capable of analyzing and understanding information within tables." \
             "\nYou are given the last row of a table. Your task is to detect if the last row has any information like aggregated rows such as ‘total’, ‘sum’ or 'average’."
    prompt += "\nLast row: "+last_row
    prompt +="\nDirectly give your choice. Ensure the format is only \"YES or NO\" form, no other form, without any explanation."
    # print(prompt)

    response = get_completion(prompt, temperature=0.5, max_tokens=10)
    print('response: ', response)

    ignore_last_row = False
    if response.strip() == 'YES':
        ignore_last_row = True

    return ignore_last_row

def transpose_table_detector(table, title):
    first_row = table.columns.tolist()
    # print('first_row: ', first_row)
    first_row = ', '.join(first_row)
    # first_col = ""+table[table.columns[0]].totlist()
    # print('first_col: ', first_col)

    first_column_name = table.columns[0]

    first_column_values = table[first_column_name].tolist()
    first_column_values = ', '.join(first_column_values)
    # print("First column name:", first_column_name)
    # print("First column values:", first_column_values)
    first_three_rows = table.head(3).to_markdown(index=False)

    tranpose_tab_prompt = "You are an advanced AI capable of analyzing and understanding information within tables. Read the first 3 rows of the table reagrading \""+title +"\""
    tranpose_tab_prompt += "\n\n## Table: \n"+first_three_rows
    tranpose_tab_prompt += "\n\nHeadings of a table are labels or titles given to rows or columns to provide a brief description of the data they contain. " \
                           "Based on the given table, the headings of the table are more likely to be: "
    tranpose_tab_prompt += "\n(A): ("+first_row+")"
    tranpose_tab_prompt += "\n(B): ("+first_column_name+", "+first_column_values+")\n"
    tranpose_tab_prompt += "\nDirectly give your choice. Ensure the format is only \"(A) or (B)\" form, no other form, without any explanation."

    need_transposision = False
    # print('Transpose_promt: \n', tranpose_tab_prompt)

    response = get_completion(tranpose_tab_prompt,temperature=0.7, max_tokens=10)
    print('response: ', response)

    if response.strip() =='(B)':
        need_transposision = True

    return need_transposision

def detect_ignore_last_row_gemini(last_row):
    prompt = "You are an advanced AI capable of analyzing and understanding information within tables." \
             "\nYou are given the last row of a table. Your task is to detect if the last row has any information like aggregated rows such as ‘total’, ‘sum’ or 'average’."
    prompt += "\nLast row: "+last_row
    prompt +="\nDirectly give your choice. Ensure the format is only \"YES or NO\" form, no other form, without any explanation."
    # print(prompt)

    response = get_completion_gemmini(prompt, temperature=0.5, max_tokens=10)
    print('response: ', response)

    ignore_last_row = False
    if response.strip() == 'YES':
        ignore_last_row = True

    return ignore_last_row

def transpose_table_detector_gemini(table, title):
    first_row = table.columns.tolist()
    # print('first_row: ', first_row)
    first_row = ', '.join(first_row)
    # first_col = ""+table[table.columns[0]].totlist()
    # print('first_col: ', first_col)

    first_column_name = table.columns[0]

    first_column_values = table[first_column_name].tolist()
    first_column_values = ', '.join(first_column_values)
    # print("First column name:", first_column_name)
    # print("First column values:", first_column_values)
    first_three_rows = table.head(3).to_markdown(index=False)

    tranpose_tab_prompt = "You are an advanced AI capable of analyzing and understanding information within tables. Read the first 3 rows of the table reagrading \""+title +"\""
    tranpose_tab_prompt += "\n\n## Table: \n"+first_three_rows
    tranpose_tab_prompt += "\n\nHeadings of a table are labels or titles given to rows or columns to provide a brief description of the data they contain. " \
                           "Based on the given table, the headings of the table are more likely to be: "
    tranpose_tab_prompt += "\n(A): ("+first_row+")"
    tranpose_tab_prompt += "\n(B): ("+first_column_name+", "+first_column_values+")\n"
    tranpose_tab_prompt += "\nDirectly give your choice. Ensure the format is only \"(A) or (B)\" form, no other form, without any explanation."

    need_transposision = False
    # print('Transpose_promt: \n', tranpose_tab_prompt)

    response = get_completion_gemmini(tranpose_tab_prompt,temperature=0.7, max_tokens=10)
    print('response: ', response)

    if response.strip() =='(B)':
        need_transposision = True
    # print(response)
    return need_transposision

# --------------------------------------------------------------------------------------------------------------------

def generate_col_prompt(title, table, tab_col):
    prompt = prompt_select_col_1
    prompt += "\n### Table:\n" +"Read the table below regarding " + "\"" + title + "\"\n\n"+ table
    prompt += "\n\nTable Coll: " + "(" + tab_col + ")"
    prompt += """\n\n### Output: Let's think step by step, and generate the final output based on the instructions without any explanation. Ensure the final output is only “normalize_coll = [col1, col2, col3,…]”form, no other form."""
    prompt += """\n### Response: """
    return prompt

def generate_normtab_prompt_basic(title, table):
    prompt = "You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize a web table so that it can be converted as a relational database table. Read the table below regarding " + "\"" + title + "\""
    prompt += "\n### Table:\n" + table
    prompt += "\n\n### Task: Headings of a table are labels or titles given to rows or columns to provide a brief description of the data they contain.\nYour task is to normalize the structure and the values of each cell to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table."
    prompt += """\n\n### Instructions:
    
1. If some of the values needed to be splitted or extracted then extract the string and add it in new columns. i.e from 'alejandro valverde (esp)' country 'esp' can be extracted and added to the new column.
2. Make sure the date and the numerical value is normalized to a uniform format. The date format should be (YYYY-MM-DD). Be cautious of numerical values that contain comma or any extra string such as ‘$’, units.
3. Convert the ‘N/A’ or null values to blank.
4. Handle the columns that contain ranges such as 2010/11, 2015-2018 etc to  two separate columns.
5. Never delete any columns or rows.
6. Do not split the value to add it to an additional row.
7. If the last row has any information like aggregated rows such as ‘total’, ‘sum’ or 'average’, then ignore it. 
7. Carefully look into the table if the first row looks like the header you do not need to change the structure. If the first column looks like a header, then transpose the table to normalize the structure."""
    prompt += """\n\n### Output: Let's think step by step, and generate the final output table based on the instructions without any explanation. Ensure the final output is only “normalized_table = [[col1, col2, col3,…], [row11, row 12, row13,.....],....]”form, no other form."""

    return prompt

def generate_normtab_prompt_targeted(title, table):
    prompt = "You are an advanced AI capable of analyzing and understanding information within tables. Your task is to normalize a web table and convert it into a relational database table, enabling the execution of SQL queries on the data.. Read the table below regarding " + "\"" + title +"\""
    prompt += "\n### Table:\n"+table
    prompt += "\n\n### Task: Your task is to normalize the structure and the values of each cell to convert this table as a regular normalized relational database table so that we can run sqlite sql query over this table."
    prompt += """\n\n### Instructions:
1. If some of the values needed to be splitted or extracted then extract the string and add it in new columns. i.e. from 'alejandro valverde (esp)' country 'esp' can be extracted and added to the new column.
2. Make sure the date and the numerical value is normalized to a uniform format. The date format should be (YYYY-MM-DD). 
3. Be cautious of numerical values that contain comma or any extra string such as '$', '%' or units.
4. Convert the ‘N/A’ or null values to blank.
5. Handle the columns that contain ranges such as 2010/11, 2015-2018 etc to  two separate columns.
6. Never delete any columns or rows.
7. Carefully remove extraneous characters if needed. """
    prompt += """\n\n### Output: Let's think step by step, and generate the final output table based on the instructions without any explanation. Ensure the final output is only “normalized_table = [[col1, col2, col3,…], [row11, row 12, row13,.....],....]”form, no other form."""

    return prompt
# --------------------------------------------------------------------------------------------------------------------

def generate_normtab_prompt_2(title, table):
    prompt = prompt_normtab_2
    prompt += "\nTitle: "+title +"\nTable: \n"+table
    prompt += """\n\n### Output: Let's think step by step, and generate the final output table based on the instructions without any explanation. Ensure the final output is only “normalized_table = [[col1, col2, col3,…], [row11, row 12, row13,.....],....]”form, no other form."""

    return prompt

def generate_sql_prompt_wtq(title, tab_col, question, examples, mode = "normtab"):
    promt = ""

    if mode == "normtab":
        prompt = "" + p_sql_three_norm_wtq
    else:
        prompt = "" + p_sql_three_wtq

    prompt += "\n### SQLite table properties:\n\n"
    prompt += "Table: " + title + " (" + str(tab_col) + ")" + "\n\n"
    prompt += "3 example rows: \n select * from T limit 3;\n"
    prompt += examples + "\n\n"
    prompt += "Q: " + question + "\n"
    prompt += "SQL:"
    return prompt

def generate_sql_prompt_wtq_zero_shot(title, tab_col, question, examples):
    prompt = "Generate SQL with no explanation given the question and table to answer the question correctly."
    prompt += "\nSQLite table properties:\n\n"
    prompt += "Table Title: " + title
    prompt += "Tabe: T (" + str(tab_col) + ")" + "\n\n"
    prompt += "3 example rows: \n select * from T limit 3;\n"
    prompt += examples + "\n\n"
    prompt += "Q: " + question + "\n"
    prompt += "SQL:"
    return prompt

# --------------------------------------------------------------------------------------------------------------------
def generate_sql_prompt_tf(title, tab_col, question, examples):
    prompt = "" + p_sql_three_tabfact
    prompt += "\nSQLite table properties:\n\n"
    prompt += "Table: " + title + " (" + str(tab_col) + ")" + "\n\n"
    prompt += "3 example rows: \n select * from T limit 3;\n"
    prompt += examples + "\n\n"
    prompt += "Q: " + question + "\n"
    prompt += "SQL:"
    return prompt


analogous_prompt_wtq = """Your task is to tackle text-to-sql generation problems where we generate a sql query to get the answer from the table. When presented with a table question answering problem , recall relevant problems as examples . Afterward , proceed to solve the initial problem.

# Initial Problem: 
SQLite table properties:

Table: Vidant Bertie Hospital(row_number,name,city,hospital_beds,operating_rooms,total,trauma_designation,affiliation,notes)

3 example rows: 
 select * from T limit 3;
row_number | name | city | hospital_beds | operating_rooms | total | trauma_designation | affiliation | notes
0 | alamance regional medical center | burlington | 238 | 15 | 253 | none | cone | none
1 | albemarle hospital | elizabeth city | 182 | 13 | 195 | none | vidant | none
2 | alexander hospital | hickory | 25 | 3 | 28 | none | none | none

Q: what is the only hospital to have 6 hospital beds?
SQL: select name from T where hospital_beds = 6

# Instructions:
Make sure that your response follows the instructions below.
## Analogous Problems:
Offer five diverse examples of math problems that are relevant or
analogous to the initial problem . For each problem , elaborate on the solution and conclude with the ultimate answer (enclosed in \boxed{}) . For each problem :
- After "Q: ", describe the problem
- After "A: ", explain the solution and enclose the ultimate answer in \
boxed {}.
## Solve the Initial Problem :
Q: Copy and paste the initial problem here.
A: Explain the solution and enclose the ultimate answer in \boxed{} here.


"""

def generate_sql_prompt_wtq_analogous(title, tab_col, question, examples):
    prompt = "Your task is to tackle table question answering problems where we generate a sql query to get the answer from the table. When presented with a table question answering problem , recall relevant problems as examples . Afterward , proceed to solve the initial problem. " \
             "\n# Initial Problem: "
    prompt += "\nSQLite table properties:\n\n"
    prompt += "Table: " + title + " (" + str(tab_col) + ")" + "\n\n"
    prompt += "3 example rows: \n select * from T limit 3;\n"
    prompt += examples + "\n\n"
    prompt += "Q: " + question + "\n"
    prompt += "SQL:"
    prompt += """# Instructions:
Make sure that your response follows the instructions below.
## Analogous Problems:
Offer five diverse examples of math problems that are relevant or
analogous to the initial problem . For each problem , elaborate on the solution and conclude with the ultimate answer (enclosed in \boxed{}) . For each problem :
- After "Q: ", describe the problem
- After "A: ", explain the solution and enclose the ultimate answer in \
boxed {}.
## Solve the Initial Problem :
Q: Copy and paste the initial problem here.
A: Explain the solution and enclose the ultimate answer in \boxed{} here.
    """
    return prompt

# --------------------------------------------------------------------------------------------------------------------

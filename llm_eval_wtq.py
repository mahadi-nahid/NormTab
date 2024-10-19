from utils.llm_agent import *


prompt = """
Table:
|   row_number |   week | date               | opponent                | result   | attendance   |
|-------------:|-------:|:-------------------|:------------------------|:---------|:-------------|
|            0 |      1 | september 6, 1981  | at los angeles rams     | w 27–20  | 63,198       |
|            1 |      2 | september 13, 1981 | at cleveland browns     | w 9–3    | 79,483       |
|            2 |      3 | september 20, 1981 | miami dolphins          | l 16–10  | 47,379       |
|            3 |      4 | september 27, 1981 | at new york jets        | l 33–17  | 50,309       |
|            4 |      5 | october 4, 1981    | cincinnati bengals      | w 17–10  | 44,350       |
|            5 |      6 | october 11, 1981   | seattle seahawks        | w 35–17  | 42,671       |
|            6 |      7 | october 18, 1981   | at new england patriots | l 38–10  | 60,474       |
|            7 |      8 | october 26, 1981   | at pittsburgh steelers  | l 26–13  | 52,732       |
|            8 |      9 | november 1, 1981   | at cincinnati bengals   | l 34–21  | 54,736       |
|            9 |     10 | november 8, 1981   | oakland raiders         | w 17–16  | 45,519       |
|           10 |     11 | november 15, 1981  | at kansas city chiefs   | l 23–10  | 73,984       |
|           11 |     12 | november 22, 1981  | new orleans saints      | l 27–24  | 49,581       |
|           12 |     13 | november 29, 1981  | atlanta falcons         | l 31–27  | 40,201       |
|           13 |     14 | december 3, 1981   | cleveland browns        | w 17–13  | 44,502       |
|           14 |     15 | december 13, 1981  | at san francisco 49ers  | l 28–6   | 55,707       |
|           15 |     16 | december 20, 1981  | pittsburgh steelers     | w 21–20  | 41,056       | 

Q: how many times did the oilers have consecutive wins? 
Answer: 
"""

response = get_completion(prompt, temperature= 0.7, max_tokens=100)

print("Response: ", response)
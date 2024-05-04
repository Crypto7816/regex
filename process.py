import pandas as pd

df1 = pd.read_csv('csv_file/telegram_history_bug.csv')
df2 = pd.read_csv('csv_file/telegram_history_match.csv')

df = pd.concat([df1, df2], ignore_index=True)
df.to_csv('csv_file/data.csv', index=False)
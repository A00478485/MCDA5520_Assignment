import pandas as pd
import numpy as np

df_raw = pd.read_csv('titles.csv')

cols = df_raw.columns
cols_new = {x: x.lower().strip() for x in cols}
df_raw.rename(columns=cols_new, inplace=True)

df_out = df_raw.copy(deep=True)

df_out['vowels'] = df_out.title.fillna("").str.lower().str.count(r'[aeiou]').astype(int)

print(df_out.head())

ans = input("Enter Y to write file (Anything else will skip the file) : ")

if ans.strip().lower() == 'y':
    df_out.to_csv("titles_output.csv")
    print("File written successfully ...")
    print("Exiting the program ...")
else:
    print("Exiting the program without writing file ...")
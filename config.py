import pandas as pd
import random
df = df = pd.read_csv('NBA_Player_Stats_Regular.csv', delimiter=";", encoding="latin-1", index_col=0)
df.columns = df.columns.str.replace(' ', '_')
sample_team = df["Tm"].sample(n=1).unique()
sample_Pos = df["Pos"].sample(n=1).unique()
del df
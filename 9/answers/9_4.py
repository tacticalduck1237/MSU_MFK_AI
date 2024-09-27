import pandas as pd
df = pd.read_csv('input.csv')
print(int(df.sum().sum() >= 8e6), df.sum().idxmax())

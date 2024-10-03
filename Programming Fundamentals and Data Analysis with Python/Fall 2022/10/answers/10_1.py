import numpy as np
import pandas as pd
df = pd.read_csv('input.csv')
df.dropna(subset=['name'], inplace=True)
df.fillna(value={'score': df['score'].mean()}, inplace=True)
df.to_csv('output.csv')

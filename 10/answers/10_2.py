import numpy as np
import pandas as pd
df = pd.read_csv('input.csv')
temperature_f=df['temperature_c'].tolist()
for d in  range(len(temperature_f)):
    temperature_f[d]=round(float(temperature_f[d])*9/5+32)
df['temperature_f'] = temperature_f
df.to_csv('output.csv')

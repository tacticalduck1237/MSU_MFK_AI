import numpy as np
import pandas as pd
df = pd.read_csv('input.csv')
df['Уникальных маршрутов'] = df['Город отправления'] + df['Город прибытия']
a=df.groupby('Номер борта')['Уникальных маршрутов'].nunique ()
a=a.to_frame()
b=a.sort_values(by=['Уникальных маршрутов','Номер борта'], ascending=[False, True])
b.to_csv('output.csv', encoding="utf8")

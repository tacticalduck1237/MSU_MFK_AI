#это самая сложная задача, пиздец просто
import pandas as pd
df= pd.read_csv('input.csv', encoding='utf-8')
df= df.drop(columns='ID')
df['Тип операции']= df['Тип операции'].apply(lambda x: 1 if x == 'Привоз' else -1)
df['Объем груза']= df['Объем груза'] * df['Тип операции']
df= df.drop(columns='Тип операции')
df= df.groupby ('Фамилия водителя').sum()
df.sort_values(by=['Объем груза', 'Фамилия водителя'], ascending= [False, True], inplace=True)
df.to_csv('output.csv')

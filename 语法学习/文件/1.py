import pandas as pd

df = pd.read_excel('任务一主生产计划表.xlsx')
df.sort_values('生产数量',ascending=False, inplace=True)
print(df.head())
df.to_csv('生产计划.csv',index = False)

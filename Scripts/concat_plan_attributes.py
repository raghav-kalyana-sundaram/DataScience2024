import pandas as pd

rate_puf_1 = '../../Data/2023/Plan_Attributes_PUF.csv'
rate_puf_2 = '../../Data/2022/Plan_Attributes_PUF.csv'
rate_puf_3 = '../../Data/2021/Plan_Attributes_PUF.csv'
rate_puf_4 = '../../Data/2020/Plan_Attributes_PUF.csv'
rate_puf_5 = '../../Data/2019/Plan_Attributes_PUF.csv'
rate_puf_6 = '../../Data/2018/Plan_Attributes_PUF.csv'
rate_puf_7 = '../../Data/2017/Plan_Attributes_PUF.csv'
rate_puf_8 = '../../Data/2016/Plan_Attributes_PUF.csv'
rate_puf_9 = '../../Data/2015/Plan_Attributes_PUF.csv'
rate_puf_10 = '../../Data/2014/Plan_Attributes_PUF_2014_2015-03-09.csv'

df1 = pd.read_csv(rate_puf_1)
df2 = pd.read_csv(rate_puf_2)
df3 = pd.read_csv(rate_puf_3)
df4 = pd.read_csv(rate_puf_4)
df5 = pd.read_csv(rate_puf_5)
df6 = pd.read_csv(rate_puf_6) 
df7 = pd.read_csv(rate_puf_7) 
df8 = pd.read_csv(rate_puf_8)
df9 = pd.read_csv(rate_puf_9)
df10 = pd.read_csv(rate_puf_10)


BigD = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0) 
BigD.to_csv('../../Data/ConcatedData/Plan_Attributes_PUF.csv')
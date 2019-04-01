import pandas as pd
import tkinter as tk
from tkinter import messagebox


def dataClean(df):
    # 空值处理
    # print(df)
    try:
        dfres = df.fillna(0)
        # 负值处理
        columns_data = list(dfres)
        rows_data = len(dfres)
        for i in range(0, rows_data):
            for j in columns_data:
                value_file = dfres.loc[i, j]
                if isinstance(value_file,str):
                    dfres.loc[i,j]=0
                elif value_file<0:
                    dfres.loc[i, j] =-1* dfres.loc[i,j]
        return dfres
    except TypeError as e:
        print(e)

df_byrkgw=pd.read_excel('C:/Users/lenovo/Desktop/test.xlsx')
print(df_byrkgw)


df_res=dataClean(df_byrkgw)
print(df_res)
# df1=df_byrkgw.sort_index(axis=1)
# print(df1)
# df2=df_byrkgw.sort_values(by='xqrk')
# print(len(df2))
# print(list(df2))

# df2.columns=list('abcdefgjkl')
# print(df2)

#对df对象的列名进行判断
# print(df2.columns)
# columnList=[]
# if 'a' in ['a','b','c']:
#     print('ok')
#
# def dataClean(df,colindex):
#     if list(df )==colindex:
#         print('ok')
#     else:
#         print('wrong!')

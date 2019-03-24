import pandas as pd
import json
from tkinter import messagebox
import tkinter as tk

'''
数据处理（清洗与过滤）
针对负值与空值
对于dataFrame对象，dropna默认丢弃任何含有缺失值的行
对于第一个读取函数，该函数的作用是清洗数据（函数）,返回清洗后的数据
低于存放函数，该函数的作用是读取清洗后的数据，将数据写入希望存放的位置
'''
# file1=pd.read_excel('c:/users/lenovo/desktop/test.xlsx', 'Sheet1')
# # print(file1)

df1=pd.read_excel('C:/Users/lenovo/Desktop/软件所需数据/2008人口岗位数据.xlsx','Sheet1')
# print(df1)
# print(df1.loc[:, 'xqrk'])

with open('Param.json','r',encoding='utf-8') as f:
    SCR=json.load(f)
    print(SCR)
    print(SCR['居住'],type(SCR['居住']))



#把df2根据df1计算出来
columnList=['小区编号','居住','居住岗位','行政办公','商业金融','教育科研','工业仓储','其他公建','其他用地建筑']
for each in columnList:
    # print(each,type(each))

    if each=="小区编号":
        print('ok')
    else:
        print(SCR[each],type(SCR[each]))

df2=df1
df2.columns=['小区编号','居住','居住岗位','行政办公','商业金融','教育科研','工业仓储','其他公建','其他用地建筑']
# print(df2)
# print(df2)
for each in columnList:
    if each=="小区编号":
        print('xqbh')
    else:
        df2[each]=df2[each]*SCR[each]
# print(df2)
#存放基准年建筑面积数据
# df2.to_excel('C:/Users/lenovo/Desktop/软件所需数据/2008建筑数据.xlsx','建筑面积')


df_pdyjzmj=pd.read_excel('C:/Users/lenovo/Desktop/软件所需数据/2013建筑面积.xlsx')
print(df_pdyjzmj)
df3=df_pdyjzmj
try:
    for each in columnList:
        if each=="小区编号":
            print('ok')
        else:
            df3[each]=df_pdyjzmj[each]-df2[each]

except KeyError as e:
    tk.messagebox.showinfo(message='请把表标题按空间系数顺序排列！')


# df_jzmjzj=df_pdyjzmj-df2
# print(df_jzmjzj,type(df_pdyjzmj))


# df2['居住面积']
# c =df2['居住面积']*SCR['居住']
# print(c)
# df2.loc[:,'居住面积']=c
# print(df2.loc[:,'居住面积'])
# df2['居住面积']=c
# print(df2)


# print(data)
# print(list(df1))

# print(file1.dropna(how='all'))
# print(file1.fillna(0))
# print(file1.size)
# row=len(file1.loc[:,'xqbh'])
# print(row)
# column=len(file1.loc[0,:])

#单个值的修改
# for i in range(0,3):
#     print(i)
# for i in range(0,row):
#     for j in list_file1:
#         data1=file1.loc[i,j]
#         if data1<4:
#             file1.loc[i,j]=10

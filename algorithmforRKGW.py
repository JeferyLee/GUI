from tkinter import  ttk
from tkinter import *
import  tkinter as tk
from tkinter import  filedialog
import  pandas as pd

# root=tk.Tk()
# root.geometry('400x300')
#
#
# def openfile():
#     file = filedialog.askopenfilename(title='打开基准年建筑面积数据', filetypes=[('Excel', '*.xlsx '), ('All Files', '*')])
#     print(file)
#     table1=pd.read_excel(file)
#     print(table1)
#     print(table1.loc[0])
#     # return table1
#
# btn1=ttk.Button(root,text='excel',command=openfile).place(x=50,y=50)
#
# # table2=openfile()
# # print(table2[0])
#
# root.mainloop()

'''
计算思路：
1.计算出人口增量
2.计算出各交通小区面积增量
3.添加一个list,把对应小区的比例算出来
4.计算小区面积时，获取其index
5.设置一个list，专门用来放用地类型
6.分成两个词典dict计算
'''
table1=pd.read_excel('c:/users/lenovo/desktop/test.xlsx', 'Sheet1')
table2=pd.read_excel('c:/users/lenovo/desktop/test.xlsx', 'Sheet2')
jzbl=[]
#定义一个人口（待分配）
pop=300
#居住消费系数
jzscr=20

# 这个list专门用来放用地类型
landtype=[]
# print(type(pop))
print(table1)
print('----------------')
print(table2)
# a=table1.loc[0][0]
# print(a, type(a))
# print(table1.loc[0][0])

# table1.loc[val]   选取单行
# table1.loc[:,val]   选择单列
# jzyd=table1.loc[:, 'jzyd']
# # print(jzyd)
# # print(len(jzyd))
# jzyd08=table1.loc[:, 'jzyd']
# jzyd13=table2.loc[:, 'jzyd']
# print(jzyd08)
# print('---------')
# print(jzyd13)
# jzydxj=jzyd13-jzyd08
# print(jzydxj)
# for i in jzydxj:
#     jzbl.append(int(i))
# print(jzbl)
# print(jzbl[0])
# #求出列表中大于0的数之和
# s=0
# for i in range(0,3):
#     if jzbl[i]>0:
#         s=s+jzbl[i]
# print(s)
# # 定义一个人口增减变量
# popzj=[]
# for i in range(0,3):
#     if jzbl[i]>0:
#         rate=jzbl[i]/s
#         popzj.append(rate*pop)
#     else:
#         # 计算建筑面积为负的交通小区
#         popzj.append(jzbl[i]/20)
# print(popzj)

# 定义就业岗位总的增量
EMP=350

tablex=table2-table1
print(tablex)
#确定行和列的长度
c=table1.loc[:,'xqbh']
print(c,len(c))
b=table1.loc[0]
print(b,len(b))
#定义一个变量用来放每个小区的就业增减量
s_emp=[]
# 就业空间消费系数
scr=[10,11]
list_yd=['syyd','xzbg']
#遍历小区
print(tablex.loc[0][0])
print('abc')
for j in range(0,len(c)):
    s_ep=0
    # 遍历小区内的用地
    for i in range(0, len(list_yd)):
        s_ep=s_ep+tablex.loc[j][i+2]/scr[i]
    print(s_ep)
    s_emp.append(s_ep)
#计算各小区的就业增减量
print(s_emp)


#计算08小区就业岗位
jygw08=[]
for i in range(0,len(c)):
    s_gw=0
    for j in range(2,len(b)):
        s_gw=s_gw+table1.loc[i][j]/scr[j-2]
    jygw08.append(s_gw)
print(jygw08)

#就业的增量分配
jyzj=[]
s_2=0
for each in s_emp:
    if each>0:
        s_2+=each
print(s_2)
for i in s_emp:
    rate=0
    if i>0:
        rate=i/s_2
        jyzj.append(rate*EMP)
    else:
        jyzj.append(i)
print(jyzj)
jygw12=[]
for i in range(0,len(c)):
    jygw12.append(jygw08[i]+jyzj[i])
print(jygw12)

# 把计算结果写入excel
series_gw=pd.Series(jygw12,index=table1.loc[:,'xqbh'])
print(series_gw)
# index1=table1.loc[:,'xqbh']
#
#
# series_gw1=pd.Series(series_gw,index=)

data_jygw=pd.DataFrame(series_gw,
                       columns=['jygw12'])
print(data_jygw)

#把就业岗位写入excel
data_jygw.to_excel('c:/users/lenovo/desktop/test1.xlsx','Sheet3')
# 需要记住正负值及它们对应的index

# dataFrame中的列可以直接计算，与list不同
# print(jzyd*0.1)


#创建新的dict


#list 类型不能直接计算
#这个函数的功能就是计算给定的dataFrame
#分为两个词典dict计算。
#相减为负和正的各设一个dict
def calc(df):
    pass







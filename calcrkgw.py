import pandas as pd
import numpy as np
import json

df_byrkgw=pd.read_excel('C:/Users/lenovo/Desktop/软件所需数据/1.xlsx','基准年人口岗位')
# print(df_byrkgw)
df_byjzmj=pd.read_excel('C:/Users/lenovo/Desktop/软件所需数据/1.xlsx','基准年建筑面积')
# print(df_byjzmj)
df_pdyjzmj=pd.read_excel('C:/Users/lenovo/Desktop/软件所需数据/1.xlsx','规划年建筑面积')
# print(df_pdyrkgw)

df_kdx=pd.read_excel('C:/Users/lenovo/Desktop/软件所需数据/1.xlsx','可达性')
# print(df_kdx)

#计算基准年人口
#计算每一列的人口岗位之和
sum_col=df_byrkgw.apply(sum)
byrk=sum_col[1]
s=0
for i in range(2,9):
    s=s+sum_col[i]
#计算基准年岗位
bygw=s

# print(bygw)
# print(byrk)
#将基准年人口单独作为一个dataFrame,赋值编号
df_byrk=df_byrkgw.loc[:,['xqrk']]
# print(df_byrk)
df_byrk.index=df_byjzmj['小区编号']
# print(df_byrk)
#计算规划年相比基准年人口岗位增量
with open('Param.json','r',encoding='utf-8') as f:
    data=json.load(f)

# print(data)
pdyrk=data['规划年总人口']
pdygw=data['规划年总就业']

#计算人口增量
rkzl=pdyrk-byrk
gwzl=pdygw-bygw
print(rkzl,gwzl)


columnList=['小区编号','居住','居住岗位','行政办公','商业金融','教育科研','工业仓储','其他公建','其他用地建筑']
df_jzmjzl=df_pdyjzmj
try:
    for each in columnList:
        if each=='小区编号':
            print('ok')
        else:
            df_jzmjzl[each]=df_pdyjzmj[each]-df_byjzmj[each]
except KeyError as e:
    print('表标题错误！')

#将交通小区建筑面积增加量构建为一个dataFrame对象
df_jzmjzl.columns=columnList
# print(df_rkgwzj)


#把小区中的居住建筑面积单独提出来，作为一个dataFrame对象
df_rk=df_jzmjzl.loc[:,['小区编号','居住']]
# print(df_rk)
df_rk.index=df_pdyjzmj['小区编号']
# print(df_rk)

#将可达性与居住建筑面积表合并起来
df_kdx.index=df_pdyjzmj['小区编号']
df_rkkdx1=df_rk.join(df_kdx)
# print(df_rkkdx1)
# print(df_rkkdx1.loc[1101,:])
#计算分母
s_rkkdx=0
for i in range(1101,1166):
    if df_rkkdx1.loc[i,'居住']>0:
        s_rkkdx=s_rkkdx+data['空置率']*df_rkkdx1.loc[i,'居住']*df_rkkdx1.loc[i,'总可达性']


#构建一个新的dataFrame对象,数值表示人口增量分配权重,
df_rk1=df_rkkdx1
# print(df_rkkdx1)
for i in range(1101,1166):
    if df_rk1.loc[i,'居住']>0:
        #人口增量分配权重
        rk_rate=data['空置率']*df_rk1.loc[i,'居住']*df_rk1.loc[i,'总可达性']/s_rkkdx
        df_rk1.loc[i,'居住']=rk_rate
    else:
        df_rk1.loc[i,'居住']=df_rk1.loc[i,'居住']/data['居住']
# print(df_rk1)

for i in range(1101,1166):
    if df_rk1.loc[i,'居住']>0:
        xqrkzl=rkzl*df_rk1.loc[i,'居住']
        df_rk1.loc[i,'居住']=xqrkzl
# print(df_rk1)
for i in range(1101,1166):
    df_rk1.loc[i,'居住']=df_rk1.loc[i,'居住']+df_byrk.loc[i,'xqrk']

print(df_rk1)


# df3=df_rk.sort_values(by='居住')
# print(df3)
#重置index
# df4=df3.reset_index(drop=True)
# print(df4)

# s=0
# for i in range(0,65):
#     if df4.loc[i,'居住']<0:
#         s=s+1
# print(s)

#dataFrame切片

# df5=df4[s:65][['小区编号','居住']]
# print(df5)

# for i in range(0,65):
#     if df_rk.loc[i,'居住']>0:
#         print(df_rk.loc[i,['小区编号','居住']])
        # df_rkzj.append(df_rk.loc[i,['小区编号','居住']],ignore_index=True)
# print(df_rkzj)

# print(df_rkgwzj)





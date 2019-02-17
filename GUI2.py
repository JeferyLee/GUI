from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import pandas as pd


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()


# 创建一个对象
app=Application()

app.master.title('城市交通小区人口就业分布计算软件 ')
app.master.minsize(1200, 700)
app.master.maxsize(1200, 700)       #画布大小

canvas=tk.Canvas(app, width=1200, height=700)     #窗口设置
imgpath = '3.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(800, 400, image=photo)
canvas.pack()
entry = tk.Entry(app, insertbackground='blue', highlightthickness=2)


def read_data():
    win_rddata = tk.Toplevel(app)
    win_rddata.title("读取数据")
    win_rddata.minsize(900, 700)
    win_rddata.maxsize(900, 800)

    # 设置标签
    lb_baseyear = ttk.Label(win_rddata,text='基准年数据处理', font=('微软雅黑', 16))
    lb_baseyear.place(x=100, y=50 )
    #读取基准年人口就业数据
    lb_baseyearrkjy =ttk.Label(win_rddata,text='基准年人口就业数据 : ',font=('微软雅黑', 13))
    lb_baseyearrkjy.place(x=100,y=105)

    lb_byrkjyinput=ttk.Label(win_rddata,text='输入文件位置：',font=('宋体', 12))
    lb_byrkjyinput.place(x=155,y=150)

    lb_byrkjyoutput=ttk.Label(win_rddata,text='输出文件位置: ',font=('宋体', 12))
    lb_byrkjyoutput.place(x=155,y=190)

    #数据清洗与过滤
    def dataClean(df):
        #空值处理
        try:
            df.fillna(0)
            #负值处理
            columns_data=list(df)
            rows_data=len(df)
            for i in range(0,rows_data):
                for j in columns_data:
                    value_file=df.loc[i,j]
                    if value_file<0:
                        df.loc[i,j]=0
            print(df)
            return df
        except TypeError as e:
            tk.messagebox.showinfo(message='请选择正确的人口就业文件')

    #读取基准年人口就业输入数据
    global file_byrkjyinput
    global var_byrkjyinput
    global df_byrkjyinput
    global df_afterres     #处理后的文件
    df_afterres = 0
    def open_byrkjyinput():
        file_byrkjyinput=filedialog.askopenfilename(title='打开基准年人口就业数据',filetypes=[('Excel', '*.xlsx '), ('All Files', '*')])

        # return df_afterres
        var_byrkjyinput.set(str(file_byrkjyinput))
        # print(file_byrkjyinput)   #返回文件名

    global var_byrkjyoutput
    #保存基准年人口就业输出数据
    def save_byrkjyoutput():

        file_byrkjyoutput=filedialog.asksaveasfilename(title='存放基准年人口就业数据',filetypes=[('Excel', '*.xlsx '), ('All Files', '*')])
        # print(file_byrkjyoutput)
        var_byrkjyoutput.set(str(file_byrkjyoutput)+'.xlsx')
        save_path=str(file_byrkjyoutput)+'.xlsx'
        # print(save_path,type(save_path))
        # df_byrkjyinput = pd.read_excel(file_byrkjyinput)
        # df_afterres = dataClean(df_byrkjyinput)
        # print(df_afterres)
        # if  isinstance(df_afterres,pd.DataFrame):
        #     df_afterres.to_excel(save_path,'Sheet1')
        #     tk.messagebox.showinfo(message='done...')
        # else:
        #     tk.messagebox.showinfo(message='请先选择基准年人口就业数据')


    #基准年人口就业
    var_byrkjyinput=tk.StringVar()
    ety_byrkjyinput=ttk.Entry(win_rddata,textvariable=var_byrkjyinput)
    ety_byrkjyinput .place(x=320, y=150)

    var_byrkjyoutput=tk.StringVar()
    ety_byrkjyoutput=ttk.Entry(win_rddata,textvariable=var_byrkjyoutput)
    ety_byrkjyoutput.place(x=320,y=190)

    btn_byrkjyinput=ttk.Button(win_rddata,text='选择', command=open_byrkjyinput)
    btn_byrkjyinput.place(x=540,y=150)

    btn_byrkjyoutput=ttk.Button(win_rddata,text='选择',command=save_byrkjyoutput)
    btn_byrkjyoutput.place(x=540,y=190)


    #基准年建筑面积数据读取
    lb_baseyearjz=ttk.Label(win_rddata, text='基准年建筑面积数据（如有）: ', font=('微软雅黑', 13))
    lb_baseyearjz.place(x=100, y=230)

    lb_byjzmjinput=ttk.Label(win_rddata,text='输入文件位置：',font=('宋体', 12))
    lb_byjzmjinput.place(x=155,y=275)

    lb_byjzmjoutput=ttk.Label(win_rddata,text='输出文件位置：',font=('宋体', 12))
    lb_byjzmjoutput.place(x=155,y=315)

    # var_rkgw=tk.StringVar()
    #设置为读取的基准年建筑面积数据名称
    # var_rkgw.set(str(file_baseyearjzmj))
    ety_byjzmjinput=ttk.Entry(win_rddata)
    ety_byjzmjinput.place(x=320, y=275)

    ety_byjzmjoutput=ttk.Entry(win_rddata)
    ety_byjzmjoutput.place(x=320,y=315)

    def open_byjzmjinput():
        file_byjzmjinput=filedialog.askopenfilename(title='打开基准年建筑面积数据',filetypes=[('Excel','*.xlsx'),('All Files','*')])
        print(file_byjzmjinput)

    def open_byjzmjoutput():
        file_byjzmjoutput=filedialog.askopenfilename(title='存放基准年建筑面积数据',filetypes=[('Excel','*.xlsx'),('All Files','*')])
        print(file_byjzmjoutput)

    btn_byjzmjinput=ttk.Button(win_rddata, text='选择',command=open_byjzmjinput)
    btn_byjzmjinput.place(x=540, y=275 )

    btn_byjzmjoutput=ttk.Button(win_rddata,text='选择',comman=open_byjzmjoutput)
    btn_byjzmjoutput.place(x=540,y=315)

    # 设置数据清洗子窗口的画布
    cav_rddata=tk.Canvas(win_rddata, width=800, height=10)
    cav_rddata.place(x=0, y=350)

    cav_rddata.create_line(50, 10, 800, 10, fill='black')   #这里需要别的参数去修正？


# '--------------------------------------------------'

    #设置未来年建筑面积与人口就业数据
    lb_predtyear=ttk.Label(win_rddata,text='未来年数据处理',font=('微软雅黑', 16))
    lb_predtyear.place(x=100,y=370)
    #未来年建筑面积标签
    lb_pdyjzmj=ttk.Label(win_rddata,text='未来年分类建筑面积数据 :', font=('微软雅黑', 13 ))
    lb_pdyjzmj.place(x=100,y=420)

    lb_pdyjzmjinput=ttk.Label(win_rddata,text='输入文件位置：',font=('宋体', 12))
    lb_pdyjzmjinput.place(x=155,y=465)

    lb_pdyjzmjoutput=ttk.Label(win_rddata,text='输出文件位置：',font=('宋体', 12))
    lb_pdyjzmjoutput.place(x=155,y=505)
    #输入框
    ety_pdyjzmjinput=ttk.Entry(win_rddata)
    ety_pdyjzmjinput.place(x=320,y=465)

    ety_pdyjzmjoutput=ttk.Entry(win_rddata)
    ety_pdyjzmjoutput.place(x=320,y=505)
    #选择
    btn_pdyjzmjinput=ttk.Button(win_rddata,text='选择')
    btn_pdyjzmjinput.place(x=540,y=465)

    btn_pdyjzmjoutput=ttk.Button(win_rddata,text='选择')
    btn_pdyjzmjoutput.place(x=540,y=505)

    #未来年交通小区可达性
    lb_predtyearkdx=ttk.Label(win_rddata,text='未来年交通小区可达性数据：',font=('微软雅黑', 12 ))
    lb_predtyearkdx.place(x=100,y=540)

    lb_pdykdx=ttk.Label(win_rddata,text='输入文件位置: ',font=('宋体', 12))
    lb_pdykdx.place(x=155,y=585)
    #设置输入框
    entry_predtyearkdx=ttk.Entry(win_rddata)
    entry_predtyearkdx.place(x=320,y=585)
    #选择按钮
    btn_predtyearkdx=ttk.Button(win_rddata,text='选择')
    btn_predtyearkdx.place(x=540,y=585)

    def cancelReaddata():
        win_rddata.destroy()

    def confReaddata():
        tk.messagebox.showinfo(title='',message='数据清洗完成！')
    btn_cancelReaddata=ttk.Button(win_rddata,text='取消',command=cancelReaddata)
    btn_cancelReaddata.place(x=260,y=640)

    btn_confReaddata=ttk.Button(win_rddata,text='确定',command=confReaddata)
    btn_confReaddata.place(x=440,y=640)

def setParam():
    win_setParam = tk.Toplevel(app)
    win_setParam.title("设置相关参数")
    win_setParam.minsize(900, 700)
    win_setParam.maxsize(900, 800)

    #设置空间消费系数标签
    lb_scr=ttk.Label(win_setParam,text='空间消费系数', font=('宋体', 20))
    lb_scr.place(x=50,y=50)

    # 居住消费系数
    lb_resident=ttk.Label(win_setParam,text='居住',font=('宋体', 12))
    lb_resident.place(x=50,y=130)

    ety_resident=ttk.Entry(win_setParam)
    ety_resident.place(x=140,y=130)
    # 范围
    lb_residentCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_residentCstraint.place(x=330,y=130)

    # 居住岗位
    lb_residtEmp=ttk.Label(win_setParam,text='居住岗位',font=('宋体', 12))
    lb_residtEmp.place(x=50,y=170)

    ety_residtEmp=ttk.Entry(win_setParam)
    ety_residtEmp.place(x=140,y=170)
    #范围
    lb_residtEmpCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_residtEmpCstraint.place(x=330,y=170)

    # 行政办公
    lb_administ=ttk.Label(win_setParam,text='行政办公',font=('宋体', 12))
    lb_administ.place(x=50,y=210)

    ety_administ=ttk.Entry(win_setParam)
    ety_administ.place(x=140,y=210)

    lb_administCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_administCstraint.place(x=330,y=210)

    #商业金融
    lb_commercial=ttk.Label(win_setParam,text='商业金融',font=('宋体', 12))
    lb_commercial.place(x=50,y=250)

    ety_commercial=ttk.Entry(win_setParam)
    ety_commercial.place(x=140,y=250)

    lb_commercialCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_commercialCstraint.place(x=330,y=250)

    # 教育科研
    lb_edu=ttk.Label(win_setParam,text='教育科研',font=('宋体', 12))
    lb_edu.place(x=430,y=130)

    ety_edu=ttk.Entry(win_setParam)
    ety_edu.place(x=530,y=130)

    lb_eduCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_eduCstraint.place(x=730,y=130)

    #工业仓储
    lb_industry=ttk.Label(win_setParam,text='工业仓储',font=('宋体', 12))
    lb_industry.place(x=430,y=170)

    ety_industry=ttk.Entry(win_setParam)
    ety_industry.place(x=530,y=170)

    lb_industryCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_industryCstraint.place(x=730,y=170)

    #其他公建
    lb_commIndus=ttk.Label(win_setParam,text='其他公建',font=('宋体', 12))
    lb_commIndus.place(x=430,y=210)

    ety_commIndus=ttk.Entry(win_setParam)
    ety_commIndus.place(x=530,y=210)

    lb_commIndusCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_commIndusCstraint.place(x=730,y=210)

    #其他用地
    lb_otherland=ttk.Label(win_setParam,text='其他用地',font=('宋体', 12))
    lb_otherland.place(x=430,y=250)

    ety_otherland=ttk.Entry(win_setParam)
    ety_otherland.place(x=530,y=251)

    lb_otherlandCstraint=ttk.Label(win_setParam,text='(0~100)',font=('宋体', 12))
    lb_otherlandCstraint.place(x=730,y=251)

    cav_rddata = tk.Canvas(win_setParam, width=800, height=50,bg='gray',relief=RAISED)
    cav_rddata.place(x=0, y=280)
    cav_rddata.create_line(0, 0, 200, 50, fill='red')
    cav_rddata.create_line(0, 50, 400, 50, fill='black')



    #其他重要参数
    lb_otherimptParam=ttk.Label(win_setParam,text='其他重要参数',font=('宋体','20'))
    lb_otherimptParam.place(x=50,y=350)
    #空置率
    lb_kzl=ttk.Label(win_setParam,text='空置率:',font=('宋体', 12))
    lb_kzl.place(x=50,y=430)

    ety_kzl=ttk.Entry(win_setParam)
    ety_kzl.place(x=190,y=430)

    #预测年总人口
    lb_predtyearpop=ttk.Label(win_setParam,text='未来年总人口:',font=('宋体', 12))
    lb_predtyearpop.place(x=50,y=490)

    ety_predtyearpop=ttk.Entry(win_setParam)
    ety_predtyearpop.place(x=190,y=490)

    # 预测年总就业
    lb_predtyearemp=ttk.Label(win_setParam,text='未来年总就业:',font=('宋体', 12))
    lb_predtyearemp.place(x=50,y=550)

    ety_predtyearemp=ttk.Entry(win_setParam)
    ety_predtyearemp.place(x=190,y=550)


    #此函数用来将读取的参数应用到excel中
    def setParamDone():
        tk.messagebox.showinfo(title='ok',message='参数设置完成！')
        win_setParam.destroy()
    def cancelsetParam():
        win_setParam.destroy()

    #取消按钮
    btn_cancelsetParam=ttk.Button(win_setParam,text='取消',command=cancelsetParam)
    btn_cancelsetParam.place(x=300,y=640)
    #确定按钮
    btn_confsetParam=ttk.Button(win_setParam,text='设置完成',command=setParamDone)
    btn_confsetParam.place(x=470,y=640)

def dataCollect():
    pass

def CalcPopemp():
    pass
btn_readData = ttk.Button(app, text='数据清洗、过滤',  command=read_data)
btn_setParam=ttk.Button(app,text='设置参数',command=setParam)
btn_dataCollect=ttk.Button(app,text='交通小区数据整合',command=dataCollect)
btn_CalcPopemp=ttk.Button(app,text='计算小区人口就业',command=CalcPopemp)

canvas.create_window(1000, 140, width=150, height=40,    #这里的长和宽是定义按钮的长和宽,100和150是按钮的位置
                     window=btn_readData)

canvas.create_window(1000, 260, width=150, height=40,
                     window=btn_setParam)

canvas.create_window(1000, 380, width=150, height=40,
                     window=btn_dataCollect)

canvas.create_window(1000, 500, width=150, height=40,
                     window=btn_CalcPopemp)

app.mainloop()
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import pandas as pd
import json


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

# global dict_SCR

# global var_residt
# global var_residtEmp
# global var_administ
# global var_commercial
# global var_edu
# global var_industry
# global var_commIndus
# global var_otherland

def read_data():
    win_rddata = tk.Toplevel(app)
    win_rddata.title("数据处理")
    win_rddata.minsize(900, 700)
    win_rddata.maxsize(900, 800)

    # 设置标签
    lb_baseyear = ttk.Label(win_rddata,text='基准年数据处理', font=('微软雅黑', 16))
    lb_baseyear.place(x=100, y=30 )
    #读取基准年人口就业数据
    lb_baseyearrkjy =ttk.Label(win_rddata,text='基准年人口就业数据 : ',font=('微软雅黑', 13))
    lb_baseyearrkjy.place(x=100,y=85)

    lb_byrkjyinput=ttk.Label(win_rddata,text='输入文件位置：',font=('宋体', 12))
    lb_byrkjyinput.place(x=155,y=130)

    lb_byrkjyoutput=ttk.Label(win_rddata,text='输出文件位置: ',font=('宋体', 12))
    lb_byrkjyoutput.place(x=155,y=170)

    #数据清洗与过滤
    def dataClean(df):
        #空值处理
        print('before res...')
        print(df)
        try:
            dfres=df.fillna(0)
            #负值处理
            columns_data=list(dfres)
            rows_data=len(dfres)
            for i in range(0,rows_data):
                for j in columns_data:
                    value_file=dfres.loc[i,j]
                    if value_file<0:
                        dfres.loc[i,j]=0
            return dfres
        except TypeError as e:
            tk.messagebox.showinfo(message='请选择正确的人口就业文件')


    #读取基准年人口就业输入数据
    global file_byrkjyinput
    global df_byrkjyinput

    def open_byrkjyinput():
        file_byrkjyinput=filedialog.askopenfilename(title='打开基准年人口就业数据',filetypes=[('Excel', '*.xlsx '), ('All Files', '*')])
        var_byrkjyinput.set(str(file_byrkjyinput))

    global var_byrkjyoutput
    #保存基准年人口就业输出数据
    def save_byrkjyoutput():
        try:
            file_byrkjyoutput=filedialog.asksaveasfilename(title='存放基准年人口就业数据', defaultextension='.txt',
                                                           filetypes=[('Excel', '*.xlsx '), ('All Files', '*')])
            # 这里如果不加defaulttextension,则保存的文件名没有后缀名。

            var_byrkjyoutput.set(str(file_byrkjyoutput))
            # print(var_byrkjyinput.get())

            #定义文件存放路径
            save_path=str(var_byrkjyoutput.get())

            #获取人口就业输入框路径
            read_path=str(var_byrkjyinput.get())
            #读取excel表格中Sheet1内数据
            df_byrkjyinput = pd.read_excel(read_path)    #默认读第一个表

            #进行数据处理
            df_afterres = dataClean(df_byrkjyinput)

            if  isinstance(df_afterres,pd.DataFrame):
                df_afterres.to_excel(save_path,'Sheet1')
                tk.messagebox.showinfo(message='done...')
                var_byrkjyoutput.set(file_byrkjyoutput)
            else:
                tk.messagebox.showinfo(message='请先选择基准年人口就业数据')
        except FileNotFoundError as e:
            print('未选择文件!')
        except ValueError as e:
            tk.messagebox.showinfo(message='表格文件中缺少Sheet1')


    #基准年人口就业
    var_byrkjyinput=tk.StringVar()
    ety_byrkjyinput=ttk.Entry(win_rddata,textvariable=var_byrkjyinput)
    ety_byrkjyinput .place(x=320, y=130)

    var_byrkjyoutput=tk.StringVar()
    ety_byrkjyoutput=ttk.Entry(win_rddata,textvariable=var_byrkjyoutput)
    ety_byrkjyoutput.place(x=320,y=170)

    btn_byrkjyinput=ttk.Button(win_rddata,text='选择', command=open_byrkjyinput)
    btn_byrkjyinput.place(x=540,y=130)

    btn_byrkjyoutput=ttk.Button(win_rddata,text='选择',command=save_byrkjyoutput)
    btn_byrkjyoutput.place(x=540,y=170)


    #基准年建筑面积数据读取
    lb_baseyearjz=ttk.Label(win_rddata, text='基准年建筑面积数据（如有）: ', font=('微软雅黑', 13))
    lb_baseyearjz.place(x=100, y=210)

    lb_byjzmjinput=ttk.Label(win_rddata,text='输入文件位置：',font=('宋体', 12))
    lb_byjzmjinput.place(x=155,y=255)

    lb_byjzmjoutput=ttk.Label(win_rddata,text='输出文件位置：',font=('宋体', 12))
    lb_byjzmjoutput.place(x=155,y=295)

    # var_rkgw=tk.StringVar()
    #设置为读取的基准年建筑面积数据名称
    var_byjzmjinput=tk.StringVar()
    ety_byjzmjinput=ttk.Entry(win_rddata,textvariable=var_byjzmjinput)
    ety_byjzmjinput.place(x=320, y=255)

    var_byjzmjoutput=tk.StringVar()
    ety_byjzmjoutput=ttk.Entry(win_rddata,textvariable=var_byjzmjoutput)
    ety_byjzmjoutput.place(x=320,y=295)

    def open_byjzmjinput():
        file_byjzmjinput=filedialog.askopenfilename(title='打开基准年建筑面积数据',filetypes=[('Excel','*.xlsx'),('All Files','*')])
        var_byjzmjinput.set(str(file_byjzmjinput))

    def save_byjzmjoutput():
        try:
            file_byjzmjoutput=filedialog.asksaveasfilename(title='存放基准年建筑面积数据', defaultextension='.xlsx',
                                                           filetypes=[('Excel','*.xlsx'),('All Files','*')])
            var_byjzmjoutput.set(str(file_byjzmjoutput))

            save_path=str(var_byjzmjoutput.get())

            read_path=str(var_byjzmjinput.get())
            #读取表格进行数据处理
            df_byjzmjinput = pd.read_excel(read_path)
            df_afterres = dataClean(df_byjzmjinput)

            if isinstance(df_afterres, pd.DataFrame):
                df_afterres.to_excel(save_path, 'Sheet1')
                tk.messagebox.showinfo(message='done...')
                var_byjzmjoutput.set(str(file_byjzmjoutput))
            else:
                tk.messagebox.showinfo(message='请先选择基准年建筑面积数据')

        except FileNotFoundError as e:
            print('未选择文件!')
        except ValueError as e:
            print('表格文件中缺少Sheet1')

    btn_byjzmjinput=ttk.Button(win_rddata, text='选择',command=open_byjzmjinput)
    btn_byjzmjinput.place(x=540, y=255 )

    btn_byjzmjoutput=ttk.Button(win_rddata,text='选择',comman=save_byjzmjoutput)
    btn_byjzmjoutput.place(x=540,y=295)

    # 设置数据清洗子窗口的画布
    cav_rddata=tk.Canvas(win_rddata, width=800, height=10)
    cav_rddata.place(x=0, y=330)

    cav_rddata.create_line(50, 10, 800, 10, fill='black')   #这里需要别的参数去修正？


# '--------------------------------------------------'

    #设置未来年建筑面积与人口就业数据
    lb_predtyear=ttk.Label(win_rddata,text='规划年数据处理',font=('微软雅黑', 16))
    lb_predtyear.place(x=100,y=350)
    #未来年建筑面积标签
    lb_pdyjzmj=ttk.Label(win_rddata,text='规划年分类建筑面积数据 :', font=('微软雅黑', 13 ))
    lb_pdyjzmj.place(x=100,y=400)

    lb_pdyjzmjinput=ttk.Label(win_rddata,text='输入文件位置：',font=('宋体', 12))
    lb_pdyjzmjinput.place(x=155,y=445)

    lb_pdyjzmjoutput=ttk.Label(win_rddata,text='输出文件位置：',font=('宋体', 12))
    lb_pdyjzmjoutput.place(x=155,y=485)
    #输入框
    var_pdyjzmjinput=tk.StringVar()
    ety_pdyjzmjinput=ttk.Entry(win_rddata,textvariable=var_pdyjzmjinput)
    ety_pdyjzmjinput.place(x=320,y=445)

    var_pdyjzmjoutput=tk.StringVar()
    ety_pdyjzmjoutput=ttk.Entry(win_rddata,textvariable=var_pdyjzmjoutput)
    ety_pdyjzmjoutput.place(x=320,y=485)

    def open_pdyjzmjinput():
        file_pdyjzmjinput=filedialog.askopenfilename(title='打开规划年建筑面积',filetypes=[('Excel','*.xlsx'),('All Files','*')])
        var_pdyjzmjinput.set(str(file_pdyjzmjinput))

    def save_pdyjzmjoutput():
        try:
            file_pdyjzmjoutput = filedialog.asksaveasfilename(title='存放规划年建筑面积数据',defaultextension='.xlsx',
                                                              filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])

            var_pdyjzmjoutput.set(str(file_pdyjzmjoutput))
            #这里对有无后缀进行判断
            save_path = str(var_pdyjzmjoutput.get())

            read_path = str(var_pdyjzmjinput.get())
            df_pdyjzmjinput = pd.read_excel(read_path)
            df_afterres = dataClean(df_pdyjzmjinput)

            if isinstance(df_afterres, pd.DataFrame):
                #默认读取第一个表格
                df_afterres.to_excel(save_path,)
                tk.messagebox.showinfo(message='done...')
            else:
                tk.messagebox.showinfo(message='请先选择规划年建筑面积数据')

        except FileNotFoundError as e:
            print('未选择文件!')
        except ValueError as e:
            tk.messagebox.showinfo(message='表格文件中缺少Sheet1')


    #选择
    btn_pdyjzmjinput=ttk.Button(win_rddata,text='选择',command=open_pdyjzmjinput)
    btn_pdyjzmjinput.place(x=540,y=445)

    btn_pdyjzmjoutput=ttk.Button(win_rddata,text='选择',command=save_pdyjzmjoutput)
    btn_pdyjzmjoutput.place(x=540,y=485)

    #未来年交通小区可达性
    lb_predtyearkdx=ttk.Label(win_rddata,text='规划年交通小区可达性数据：',font=('微软雅黑', 13))
    lb_predtyearkdx.place(x=100,y=520)

    lb_pdykdx=ttk.Label(win_rddata,text='输入文件位置: ',font=('宋体', 12))
    lb_pdykdx.place(x=155,y=565)
    #设置输入框
    var_pdykdx=tk.StringVar()
    entry_predtyearkdx=ttk.Entry(win_rddata,textvariable=var_pdykdx)
    entry_predtyearkdx.place(x=320,y=565)
    #选择按钮

    global df_pdykdx
    #不能声明为全局变量
    # global var_pdykdx
    def  open_pdykdx():
        file_pdykdx=filedialog.askopenfilename(title='打开可达性文件',filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        var_pdykdx.set(str(file_pdykdx))
        df_pdykdx=pd.read_excel(str(file_pdykdx))

    btn_pdykdx=ttk.Button(win_rddata,text='选择',command=open_pdykdx)
    btn_pdykdx.place(x=540,y=565)

    #读取可达性文件
    def getkdx():
        kdxfilename=var_pdykdx.get()
        if kdxfilename is not None:
            df_pdykdx=pd.read_excel(str(kdxfilename))

    def cancelReaddata():
        win_rddata.destroy()

    def confReaddata():
        tk.messagebox.showinfo(title='',message='数据清洗完成！')
        win_rddata.destroy()

    btn_cancelReaddata=ttk.Button(win_rddata,text='取消',command=cancelReaddata)
    btn_cancelReaddata.place(x=260,y=640)

    btn_confReaddata=ttk.Button(win_rddata,text='确定',command=confReaddata)
    btn_confReaddata.place(x=440,y=640)


#设置参数界面
#'----------------------------------------'
global pdypop
global pdyemp

#为空间消费系数定义一个list



def setParam():
    win_setParam = tk.Toplevel(app)
    win_setParam.title("设置相关参数")
    win_setParam.minsize(900, 700)
    win_setParam.maxsize(900, 800)

    #设置空间消费系数标签
    lb_scr=ttk.Label(win_setParam,text='空间消费系数', font=('微软雅黑', 18))
    lb_scr.place(x=50,y=50)

    # 居住消费系数
    lb_resident=ttk.Label(win_setParam,text='居住',font=('宋体', 12))
    lb_resident.place(x=70,y=130)

    #空间消费系数应为double型

    var_residt=tk.StringVar()
    ety_resident=ttk.Entry(win_setParam,textvariable=var_residt)
    ety_resident.place(x=160,y=130)
    # 范围
    lb_residentCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_residentCstraint.place(x=350,y=130)

    # 居住岗位
    lb_residtEmp=ttk.Label(win_setParam,text='居住岗位',font=('宋体', 12))
    lb_residtEmp.place(x=70,y=170)

    var_residtEmp=tk.StringVar()
    ety_residtEmp=ttk.Entry(win_setParam,textvariable=var_residtEmp)
    ety_residtEmp.place(x=160,y=170)
    #范围
    lb_residtEmpCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_residtEmpCstraint.place(x=350,y=170)

    # 行政办公
    lb_administ=ttk.Label(win_setParam,text='行政办公',font=('宋体', 12))
    lb_administ.place(x=70,y=210)

    var_administ=tk.StringVar()
    ety_administ=ttk.Entry(win_setParam,textvariable=var_administ)
    ety_administ.place(x=160,y=210)

    lb_administCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_administCstraint.place(x=350,y=210)

    #商业金融
    lb_commercial=ttk.Label(win_setParam,text='商业金融',font=('宋体', 12))
    lb_commercial.place(x=70,y=250)

    var_commercial=tk.StringVar()
    ety_commercial=ttk.Entry(win_setParam,textvariable=var_commercial)
    ety_commercial.place(x=160,y=250)

    lb_commercialCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_commercialCstraint.place(x=350,y=250)

    # 教育科研
    lb_edu=ttk.Label(win_setParam,text='教育科研',font=('宋体', 12))
    lb_edu.place(x=460,y=130)

    var_edu=tk.StringVar()
    ety_edu=ttk.Entry(win_setParam,textvariable=var_edu)
    ety_edu.place(x=560,y=130)

    lb_eduCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_eduCstraint.place(x=760,y=130)

    #工业仓储
    lb_industry=ttk.Label(win_setParam,text='工业仓储',font=('宋体', 12))
    lb_industry.place(x=460,y=170)

    var_industry=tk.StringVar()
    ety_industry=ttk.Entry(win_setParam,textvariable=var_industry)
    ety_industry.place(x=560,y=170)

    lb_industryCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_industryCstraint.place(x=760,y=170)

    #其他公建
    lb_commIndus=ttk.Label(win_setParam,text='其他公建',font=('宋体', 12))
    lb_commIndus.place(x=460,y=210)

    var_commIndus=tk.StringVar()
    ety_commIndus=ttk.Entry(win_setParam,textvariable=var_commIndus)
    ety_commIndus.place(x=560,y=210)

    lb_commIndusCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_commIndusCstraint.place(x=760,y=210)

    #其他用地建筑
    lb_otherland=ttk.Label(win_setParam,text='其他用地',font=('宋体', 12))
    lb_otherland.place(x=460,y=250)

    var_otherland=tk.StringVar()
    ety_otherland=ttk.Entry(win_setParam,textvariable=var_otherland)
    ety_otherland.place(x=560,y=251)

    lb_otherlandCstraint=ttk.Label(win_setParam,text='(0-150)',font=('宋体', 12))
    lb_otherlandCstraint.place(x=760,y=251)

    cav_rddata = tk.Canvas(win_setParam, width=800, height=10,relief=RAISED)
    cav_rddata.place(x=0, y=290)
    cav_rddata.create_line(50, 10, 800, 10, fill='black')


    #其他重要参数
    lb_otherimptParam=ttk.Label(win_setParam,text='其他重要参数',font=('微软雅黑','16'))
    lb_otherimptParam.place(x=50,y=320)
    #空置率
    lb_kzl=ttk.Label(win_setParam,text='空置率:',font=('宋体', 12))
    lb_kzl.place(x=80,y=380)

    var_kzl=tk.DoubleVar()
    ety_kzl=ttk.Entry(win_setParam,textvariable=var_kzl)
    ety_kzl.place(x=220,y=380)

    lb_kzlCstraint=ttk.Label(win_setParam,text='(0-1)',font=('宋体', 12))
    lb_kzlCstraint.place(x=410,y=380)

    #预测年总人口
    lb_predtyearpop=ttk.Label(win_setParam,text='规划年总人口:',font=('宋体', 12))
    lb_predtyearpop.place(x=80,y=430)

    var_pdypop=tk.StringVar()
    ety_predtyearpop=ttk.Entry(win_setParam,textvariable=var_pdypop)
    ety_predtyearpop.place(x=220,y=430)

    # 预测年总就业
    lb_predtyearemp=ttk.Label(win_setParam,text='规划年总就业:',font=('宋体', 12))
    lb_predtyearemp.place(x=80,y=480)

    var_pdyemp=tk.StringVar()
    ety_predtyearemp=ttk.Entry(win_setParam,textvariable=var_pdyemp)
    ety_predtyearemp.place(x=220,y=480)

    #此函数用来将读取的参数应用到excel中
    def setParamDone():
        # global dict_SCR
        # dict_SCR={}     #定义一个空的dict
        tk.messagebox.showinfo(title='ok',message='参数设置完成！')

        if var_kzl.get()<0:
            tk.messagebox.showinfo(messagae='空置率不能小于0 ！')
        elif var_kzl.get()>1:
            tk.messagebox.showinfo(message='空置率不能大于1 ！')
        else:
            try:
                dict_SCR = {'居住': int(var_residt.get()), '居住岗位': int(var_residtEmp.get()), '行政办公': int(var_administ.get()),
                            '商业金融': int(var_commercial.get()), '教育科研': int(var_edu.get()),
                            '工业仓储': int(var_industry.get()), '其他公建': int(var_commIndus.get()),
                            '其他用地建筑': int(var_otherland.get()),'空置率': var_kzl.get(),
                            '规划年总人口': int(var_pdypop.get()), '规划年总就业': int(var_pdyemp.get())}
                print(dict_SCR)
                for k, v in dict_SCR.items():
                    if v < 0:
                        tk.messagebox.showinfo(message='空间消费系数-%s' % k + '不能小于0 !')
                    else:
                        # 将参数写入json
                        jsonobj = json.dumps(dict_SCR, ensure_ascii=False)
                        with open('Param.json', 'w', encoding='utf-8') as f:
                            f.write(jsonobj)
            except ValueError as e:
                tk.messagebox.showinfo(message='请填完所有参数，参数必须是整数！ ')

        win_setParam.destroy()

    def cancelsetParam():
        win_setParam.destroy()

    #取消按钮
    btn_cancelsetParam=ttk.Button(win_setParam,text='取消',command=cancelsetParam)
    btn_cancelsetParam.place(x=300,y=590)
    #确定按钮
    btn_confsetParam=ttk.Button(win_setParam,text='设置完成',command=setParamDone)
    btn_confsetParam.place(x=470,y=590)




def dataCollect():
    win_dataCollect=tk.Toplevel(app)
    win_dataCollect.title('数据整合')
    win_dataCollect.minsize(900,700)
    win_dataCollect.maxsize(900,800)

    # print(dict_SCR)
    lb_dataCollect=ttk.Label(win_dataCollect,text='处理后的数据选择', font=('微软雅黑', 15))
    lb_dataCollect.place(x=50,y=90)

    #读取清洗后的基准年小区人口岗位数据
    def open_byrkgw_afdc():
        file_byrkgw_afdc=filedialog.askopenfilename(title='打开基准年处理后的人口岗位数据',filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        var_byrkgw_afdc.set(str(file_byrkgw_afdc))

    #处理后的基准年小区人口岗位数据
    lb_byrkgw_afdc=ttk.Label(win_dataCollect,text='基准年小区人口岗位数据',font=('宋体', 12))
    lb_byrkgw_afdc.place(x=80,y=150)

    var_byrkgw_afdc=tk.StringVar()
    ety_byrkgw_afdc=ttk.Entry(win_dataCollect,textvariable=var_byrkgw_afdc)
    ety_byrkgw_afdc.place(x=350,y=150)

    btn_byrkgw_afdc=ttk.Button(win_dataCollect,text='选择',command=open_byrkgw_afdc)
    btn_byrkgw_afdc.place(x=600,y=150)

    #处理后的规划年小区建筑面积数据
    def open_pdyjzmj_afdc():
        file_pdyjzmj_afdc=filedialog.askopenfilename(title='打开基准年处理后的建筑面积数据',filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        var_pdyjzmj_afdc.set(str(file_pdyjzmj_afdc))

    lb_pdyjzmj_afdc=ttk.Label(win_dataCollect,text='规划年小区建筑面积数据',font=('宋体', 12))
    lb_pdyjzmj_afdc.place(x=80,y=210)

    var_pdyjzmj_afdc=tk.StringVar()
    ety_pdyjzmj_afdc=ttk.Entry(win_dataCollect,textvariable=var_pdyjzmj_afdc)
    ety_pdyjzmj_afdc.place(x=350,y=210)

    btn_pdyjzmj_afdcselct=ttk.Button(win_dataCollect,text='选择',command=open_pdyjzmj_afdc)
    btn_pdyjzmj_afdcselct.place(x=600,y=210)

    #交通小区可达性数据

    def open_kdxafdc():
        file_kdxafdc=filedialog.askopenfilename(title='打开处理后的交通小区可达性数据',filetypes=[('Excel','*.xlsx'),('All Files','*')])
        var_kdx_afdc.set(str(file_kdxafdc))
    lb_kdx_afdc=ttk.Label(win_dataCollect,text='交通小区可达性数据',font=('宋体',12))
    lb_kdx_afdc.place(x=80,y=270)

    var_kdx_afdc=tk.StringVar()
    ety_kdx_afdc=ttk.Entry(win_dataCollect,textvariable=var_kdx_afdc)
    ety_kdx_afdc.place(x=350,y=270)


    btn_kdx_afdc=ttk.Button(win_dataCollect,text='选择',command=open_kdxafdc)
    btn_kdx_afdc.place(x=600,y=270)





    #数据整合后存放位置
    def open_afdataCollect():
        file_afdataCollect=filedialog.asksaveasfilename(title='打开数据整合后存放位置',defaultextension='.xlsx',
                                                        filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        var_afdataCollect.set(str(file_afdataCollect))

    lb_afdataCollect=ttk.Label(win_dataCollect,text='数据整合后存放位置',font=('微软雅黑',14))
    lb_afdataCollect.place(x=50,y=350)

    var_afdataCollect=tk.StringVar()
    ety_afdataCollect=ttk.Entry(win_dataCollect,textvariable=var_afdataCollect)
    ety_afdataCollect.place(x=350,y=350)

    btn_afdataCollect=ttk.Button(win_dataCollect,text='选择',command=open_afdataCollect)
    btn_afdataCollect.place(x=600,y=350)


    def cacle_datacollect():
        win_dataCollect.destroy()

    def confm_datacollect():
        try:
            #读取在窗口二中设置的空间消费系数
            with open('Param.json', 'r', encoding='utf-8') as f:
                SCR = json.load(f)
                print(SCR)
                # print(SCR['居住'], type(SCR['居住']))
        except FileNotFoundError as e:
            tk.messagebox.showinfo(message='请先设置相关参数！')

        try:
            df_byrkgw=pd.read_excel(str(var_byrkgw_afdc.get()))

            df_pdyjzmj = pd.read_excel(str(var_pdyjzmj_afdc.get()))

            df_kdxafdc = pd.read_excel(str(var_kdx_afdc.get()))

            columnList = ['小区编号', '居住', '居住岗位', '行政办公', '商业金融', '教育科研', '工业仓储', '其他公建', '其他用地建筑']
            print(df_byrkgw)
            df_temp= df_byrkgw
            print(df_byrkgw)
            writer = pd.ExcelWriter(var_afdataCollect.get())
            df_byrkgw.to_excel(writer, '基准年人口岗位')

            df_temp.columns = ['小区编号', '居住', '居住岗位', '行政办公', '商业金融', '教育科研', '工业仓储', '其他公建', '其他用地建筑']
            # print(df2)
            for each in columnList:
                if each == "小区编号":
                    print('xqbh')
                else:
                    #计算基准年建筑面积数据
                    df_temp[each] = df_temp[each] * SCR[each]

            df_temp.to_excel(writer, '基准年建筑面积')
            df_pdyjzmj.to_excel(writer, '规划年建筑面积')
            df_kdxafdc.to_excel(writer, '可达性')



        except FileNotFoundError as e:
            tk.messagebox.showinfo(message='请先选择文件！')

        tk.messagebox.showinfo(title='确认',message='完成数据整合！')
        win_dataCollect.destroy()
    btn_cancel=ttk.Button(win_dataCollect,text='取消',command=cacle_datacollect)
    btn_cancel.place(x=260,y=560)

    btn_confm=ttk.Button(win_dataCollect,text='确定',command=confm_datacollect)
    btn_confm.place(x=460,y=560)



#计算交通小区人口岗位
def CalcPopemp():
    win_calcpe=tk.Toplevel(app)
    win_calcpe.title('计算人口岗位')
    win_calcpe.minsize(900,700)
    win_calcpe.maxsize(900,800)

    #选择数据整合后的文件

    def open_file_afdc():
        file_afdc=filedialog.askopenfilename(title='打开数据整合后的文件',filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        var_file_afdc.set(str(file_afdc))

    lb_file_afdc=ttk.Label(win_calcpe,text='整合后的数据文件:',font=('宋体',12))
    lb_file_afdc.place(x=90,y=90)

    var_file_afdc=tk.StringVar()
    ety_file_afdc=ttk.Entry(win_calcpe,textvariable=var_file_afdc)
    ety_file_afdc.place(x=390,y=90)

    btn_file_afdc=ttk.Button(win_calcpe,text='选择',command=open_file_afdc)
    btn_file_afdc.place(x=620,y=90)

    #交通小区人口岗位计算保存

    def save_rkgw_afclc():
        file_rkgw_afclc=filedialog.asksaveasfilename(title='交通小区人口岗位计算保存',defaultextension='.xlsx',
                                                        filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        var_rkgw_afclc.set(str(file_rkgw_afclc))


    lb_rkgw_afcalc=ttk.Label(win_calcpe,text='交通小区人口岗位计算结果保存:',font=('宋体',12))
    lb_rkgw_afcalc.place(x=90,y=150)

    var_rkgw_afclc=tk.StringVar()
    ety_rkgw_afcalc=ttk.Entry(win_calcpe,textvariable=var_rkgw_afclc)
    ety_rkgw_afcalc.place(x=390,y=150)

    btn_rkgw_afclc=ttk. Button(win_calcpe,text='选择',command=save_rkgw_afclc)
    btn_rkgw_afclc.place(x=620,y=150)

    def calcpe():
        print(var_file_afdc)
        df_byrkgw = pd.read_excel(str(var_file_afdc.get()), '基准年人口岗位')
        # print(df_byrkgw)
        df_byjzmj = pd.read_excel(str(var_file_afdc.get()), '基准年建筑面积')
        # print(df_byjzmj)
        df_pdyjzmj = pd.read_excel(str(var_file_afdc.get()), '规划年建筑面积')
        # print(df_pdyrkgw)

        df_kdx = pd.read_excel(str(var_file_afdc.get()), '可达性')
        # print(df_kdx)

        # 计算基准年人口
        # 计算每一列的人口岗位之和
        sum_col = df_byrkgw.apply(sum)
        byrk = sum_col[1]
        s = 0
        for i in range(2, 9):
            s = s + sum_col[i]
        # 计算基准年岗位
        bygw = s

        # 将基准年人口单独作为一个dataFrame,赋值编号
        df_byrk = df_byrkgw.loc[:, ['xqrk']]
        # print(df_byrk)
        df_byrk.index = df_byjzmj['小区编号']
        # print(df_byrk)

        # 将基准年岗位作为一个dataFrame
        df_temp = df_byrkgw.iloc[:, 2:9]
        df_bygw = df_temp.copy()
        # print(df_bygw.sum(axis=1))

        df_bygw['gw_sum'] = 0

        # 对每行进行求和
        df_bygw.loc[:, 'gw_sum'] = df_bygw.apply(lambda x: x.sum(), axis=1)
        # df_bygw['gw_sum']=df_bygw.sum(axis=1)
        df_bygw.index = df_byjzmj['小区编号']
        print(df_bygw)

        # 计算规划年相比基准年人口岗位增量
        with open('Param.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # print(data)
        pdyrk = data['规划年总人口']
        pdygw = data['规划年总就业']

        # 计算人口增量
        rkzl = pdyrk - byrk
        gwzl = pdygw - bygw
        print(rkzl, gwzl)

        columnList = ['小区编号', '居住', '居住岗位', '行政办公', '商业金融', '教育科研', '工业仓储', '其他公建', '其他用地建筑']
        df_jzmjzl = df_pdyjzmj
        try:
            for each in columnList:
                if each == '小区编号':
                    print('ok')
                else:
                    df_jzmjzl[each] = df_pdyjzmj[each] - df_byjzmj[each]
        except KeyError as e:
            print('表标题错误！')

        # 将交通小区建筑面积增加量构建为一个dataFrame对象
        df_jzmjzl.columns = columnList
        # print(df_jzmjzl)

        # 把小区中的居住建筑面积单独提出来，作为一个dataFrame对象
        df_rkmj = df_jzmjzl.loc[:, ['小区编号', '居住']]

        df_rkmj.index = df_pdyjzmj['小区编号']
        # print(df_rk)

        # 将可达性与居住建筑面积表合并起来
        df_kdx.index = df_pdyjzmj['小区编号']
        df_rkkdx1 = df_rkmj.join(df_kdx)
        # print(df_rkkdx1)

        # 计算分母
        s_rkkdx = 0
        for i in range(1101, 1166):
            if df_rkkdx1.loc[i, '居住'] > 0:
                s_rkkdx = s_rkkdx + data['空置率'] * df_rkkdx1.loc[i, '居住'] * df_rkkdx1.loc[i, '总可达性']

        # 构建一个新的dataFrame对象,数值表示人口增量分配权重,
        df_rk1 = df_rkkdx1
        # print(df_rkkdx1)
        for i in range(1101, 1166):
            if df_rk1.loc[i, '居住'] > 0:
                # 人口增量分配权重
                rk_rate = data['空置率'] * df_rk1.loc[i, '居住'] * df_rk1.loc[i, '总可达性'] / s_rkkdx
                df_rk1.loc[i, '居住'] = rk_rate
            else:
                df_rk1.loc[i, '居住'] = df_rk1.loc[i, '居住'] / data['居住']
        # print(df_rk1)

        for i in range(1101, 1166):
            if df_rk1.loc[i, '居住'] > 0:
                xqrkzl = rkzl * df_rk1.loc[i, '居住']
                df_rk1.loc[i, '居住'] = xqrkzl
        # print(df_rk1)
        for i in range(1101, 1166):
            df_rk1.loc[i, '居住'] = df_rk1.loc[i, '居住'] + df_byrk.loc[i, 'xqrk']

        # print(df_rk1)

        # 计算岗位
        df_temp1 = df_jzmjzl
        for each in columnList:
            if each == '小区编号' or each == '居住':
                print('ok')
            else:
                df_temp1[each] = df_jzmjzl[each] / data[each]

        # 把岗位增量单独提出来赋值给df
        df_gwzl = df_temp1.loc[:, ['居住岗位', '行政办公', '商业金融', '教育科研', '工业仓储', '其他公建', '其他用地建筑']]
        # print(df_gwzl)
        # 对就业岗位求和
        df_gwzl['gw_sum'] = df_gwzl.apply(lambda x: x.sum(), axis=1)
        df_gwzl.index = df_pdyjzmj['小区编号']
        # print(df_gwzl)
        df_gwkdx = df_gwzl.join(df_kdx)
        # print(df_gwkdx)

        # 对岗位增量与可达性之积进行求和
        s_gwkdx = 0
        for i in range(1101, 1166):
            if df_gwkdx.loc[i, 'gw_sum'] > 0:
                s_gwkdx = s_gwkdx + df_gwkdx.loc[i, 'gw_sum'] * df_gwkdx.loc[i, '总可达性']

        # 求岗位增量权重
        for i in range(1101, 1166):
            if df_gwkdx.loc[i, 'gw_sum'] > 0:
                gw_rate = df_gwkdx.loc[i, 'gw_sum'] * df_gwkdx.loc[i, '总可达性'] / s_gwkdx
                df_gwkdx.loc[i, 'gw_sum'] = gw_rate
        df_gwkdx1 = df_gwkdx.loc[:, ['gw_sum']]
        # print(df_gwkdx1)

        for i in range(1101, 1166):
            if df_gwkdx1.loc[i, 'gw_sum'] > 0:
                df_gwkdx1.loc[i, 'gw_sum'] = df_gwkdx1.loc[i, 'gw_sum'] * gwzl
        # print(df_gwkdx1)
        df_temp2 = df_gwkdx1.copy()
        for i in range(1101, 1166):
            df_temp2.loc[i, '岗位'] = df_gwkdx1.loc[i, 'gw_sum'] + df_bygw.loc[i, 'gw_sum']
        df_pdygw = df_temp2.loc[:, ['岗位']]
        print(df_pdygw)

        df_pdyrkgw = df_rk1.join(df_pdygw)
        print(df_pdyrkgw)
        df_pdyrkgw1 = df_pdyrkgw.loc[:, ['居住', '岗位']]
        df_pdyrkgw1.columns = ['人口', '岗位']
        print(df_pdyrkgw1)
        df_pdyrkgw1.to_excel(str(var_rkgw_afclc.get()))
        tk.messagebox.showinfo(message='计算完成！')

    btn_calcpe=tk.Button(win_calcpe,text='计算人口岗位',width=12,height=2,bg='#E6E6E6',fg='black',command=calcpe)

    # btn_calcpe=ttk.Button(win_calcpe ,text='计算位')
    btn_calcpe.place(x=620,y=220)

    #添加画布
    cav_rddata = tk.Canvas(win_calcpe, width=800, height=10, relief=RAISED)
    cav_rddata.place(x=0, y=290)
    cav_rddata.create_line(50, 10, 800, 10, fill='black')



    #查询计算后的人口岗位
    def rkgw_query():
        df_rkgw_query=pd.read_excel(str(var_rkgw_afclc.get()))
        index1=int(var_rkgw_search.get())-1101

        print(df_rkgw_query.loc[index1,'人口'])
        rk=df_rkgw_query.loc[index1,'人口']
        gw=df_rkgw_query.loc[index1,'岗位']
        var_pop.set(int(rk))
        var_emp.set(int(gw))

    lb_rkgw_query=ttk.Label(win_calcpe,text='查询交通小区人口岗位',font=('微软雅黑',14))
    lb_rkgw_query.place(x=90,y=350)

    lb_rkgw_search=ttk.Label(win_calcpe,text='输入交通小区编号',font=('宋体',12))
    lb_rkgw_search.place(x=130,y=420)

    var_rkgw_search=tk.StringVar()
    ety_rkgw_search=ttk.Entry(win_calcpe,textvariable=var_rkgw_search)
    ety_rkgw_search.place(x=390,y=420)

    btn_query=ttk.Button(win_calcpe,text='查询',command=rkgw_query)
    btn_query.place(x=620,y=420)

    lb_pop=ttk.Label(win_calcpe,text='小区人口:',font=('宋体',12))
    lb_pop.place(x=160,y=510)

    var_pop=tk.StringVar()
    ety_pop=tk.Entry(win_calcpe,width=10 ,textvariable=var_pop)
    ety_pop.place(x=270,y=510)

    lb_emp=ttk.Label(win_calcpe,text='小区岗位:',font=('宋体',12))
    lb_emp.place(x=420,y=510)

    var_emp=tk.StringVar()
    ety_emp=tk.Entry(win_calcpe,width=10,textvariable=var_emp)
    ety_emp.place(x=530,y=510)



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
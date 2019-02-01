from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class Application(Frame):
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("for lich king~")
        self.root.minsize(700,600)
        self.root.maxsize(700,650)
        self.layout()

        self.root.mainloop()

    def layout(self):
        #定义读取数据按钮
        self.btn_rddata=ttk.Button(self.root,text='读取数据',command=self.read_data)
        self.btn_rddata.place(x=500,y=50,width=90,height=50)

        #定义设置参数按钮
        self.btn_configParam=ttk.Button(self.root,text='设置参数',command=self.configParam)
        self.btn_configParam.place(x=500,y=260,width=90,height=50)

        #定义计算人口与就业按钮
        self.btn_Calcrkgw=ttk.Button(self.root,text='计算人口岗位',command=self.Calcrkgw)
        self.btn_Calcrkgw.place(x=500,y=460,width=110,height=50)
    def read_data(self):
        self.win_rddata=tk.Toplevel(self.root)
        self.win_rddata.title("for lord~~")
        self.win_rddata.minsize(500,400)
        self.win_rddata.maxsize(500,450)

    def configParam(self):
        self.win_configParam=tk.Toplevel(self.root)
        self.win_configParam.title('设置相关参数')
        self.win_configParam.minsize(500,400)
        self.win_configParam.maxsize(500,450)

        #设置空置率
        self.label_snr=ttk.Label(self.win_configParam,text='空置率 :',font=('微软雅黑',12 ))
        self.label_snr.place(x=70,y=30)

        #设置空置率输入框的性质为double
        self.var_enty_snr=tk.DoubleVar()
        self.enty_snr=ttk.Entry(self.win_configParam,textvariable=self.var_enty_snr)
        self.enty_snr.place(x=170,y=30,height=30,width=90)

        #若需使用空置率，则使用下面语句
        # enty_snr=var_enty_snr.get()
        self.label_snrctrl=ttk.Label(self.win_configParam,text='(0~1)',font=('微软雅黑',12 ))
        self.label_snrctrl.place(x=280,y=30)


        #设置参数确认按钮
        self.btn_confirm=ttk.Button(self.win_configParam,text='设置完成',command=self.ParamSetted)
        self.btn_confirm.place(x=90,y=200,height=40,width=90)

    def ParamSetted(self):
        #进行空置率输入数据范围的判断
        if self.var_enty_snr.get()==0:
            tk.messagebox.showwarning(title='错误',message='请输入数字')
        elif self.var_enty_snr.get()>1:
            tk.messagebox.showwarning(title='错误',message='请输入0到1之间的数字')
        elif self.var_enty_snr.get()<0:
            tk.messagebox.showwarning(title='错误',message='请输入0到1之间的数字')
        else:
            self.enty_snr=self.var_enty_snr.get()
            c=self.var_enty_snr.get()*5
            print(c,type(c))
            self.win_configParam.destroy()



    def Calcrkgw(self):
        pass

if __name__=='__main__':
    app=Application()

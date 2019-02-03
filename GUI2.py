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

app.master.title('for calc demo~~ ')
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
    lb_baseyear = ttk.Label(win_rddata,text='基准年信息', font=('微软雅黑', 20))
    lb_baseyear.place(x=50, y=50 )

    lb_baseyearjz =ttk.Label(win_rddata,text='基准年建筑面积数据 : ',font=('微软雅黑', 12))
    lb_baseyearjz.place(x=50,y=125)



    def open_baseyearjz():
        file=filedialog.askopenfilename(title='打开基准年建筑面积数据',filetypes=[('Excel', '*.xlsx '), ('All Files', '*')])
        print(file)
        tb1=pd.read_excel(file)
        print(tb1)
        print(tb1.loc[0]) 

    #建筑面积输入
    entry_baseyearjz=ttk.Entry(win_rddata)
    entry_baseyearjz.place(x=310, y=130)

    btn_baseyearjz=ttk.Button(win_rddata,text='选择',command=open_baseyearjz)
    btn_baseyearjz.place(x=520,y=130)

    lb_baseyearrkgw=ttk.Label(win_rddata, text='基准年建筑人口岗位数据 : ', font=('微软雅黑', 12))
    lb_baseyearrkgw.place(x=50, y=200)

    # 人口岗位输入
    entry_baseyearrkgw=ttk.Entry(win_rddata)
    entry_baseyearrkgw.place(x=310, y=205)

    btn_baseyearrkgw=ttk.Button(win_rddata, text='选择')
    btn_baseyearrkgw.place(x=520, y=205 )

    cav_rddata=tk.Canvas(win_rddata, width=800, height=100)
    cav_rddata.place(x=50, y=240)

    cav_rddata.create_line(0,50,200,50,fill='red')
    cav_rddata.create_line(0, 40, 200, 50, fill='red')
    cav_rddata.create_line(0, 30, 200, 50, fill='red')
    cav_rddata.create_line(0, 0, 200, 50, fill='red')
    cav_rddata.create_line(0, 100, 200, 50, fill='red')






btn_readData = ttk.Button(app, text='读取数据',  command=read_data)

canvas.create_window(1000, 200, width=100, height=20,
                     window=entry)
canvas.create_window(1000, 350, width=150, height=40,    #这里的长和宽是定义按钮的长和宽,100和150是按钮的位置
                     window=btn_readData)





app.mainloop()
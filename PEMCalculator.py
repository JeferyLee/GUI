from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Application(Frame):
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("for lich king~")
        self.root.minsize(700,600)
        self.root.maxsize(700,650)
        self.layout()

        self.root.mainloop()

    def layout(self):
        self.btn_rddata=ttk.Button(self.root,text='读取数据',command=self.read_data)
        self.btn_rddata.pack(expand=YES,fill=None,anchor=NE,side=TOP)

        self.btn_confParam=ttk.Button(self.root,text='设置参数')

    def read_data(self):
        self.win_rddata=tk.Toplevel(self.root)
        self.win_rddata.title("for lord~~")
        self.win_rddata.minsize(400,300)
        self.win_rddata.maxsize(400,350)


if __name__=='__main__':
    app=Application()

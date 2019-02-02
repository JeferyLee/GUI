from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()


#创建一个对象
app=Application()

app.master.title('for calc demo~~ ')
app.master.minsize(1600,900)
app.master.maxsize(1920,1080)       #画布大小

canvas=tk.Canvas(app,width=1600, height=900)     #窗口设置
imgpath = '3.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(800, 400, image=photo)
canvas.pack()
entry = tk.Entry(app, insertbackground='blue', highlightthickness=2)
# entry.pack()

def read_data():
    win_rddata = tk.Toplevel(app)
    win_rddata.title("for lord~~")
    win_rddata.minsize(500, 400)
    win_rddata.maxsize(500, 450)

btn=tk.Button(app, width=20, height=10, text='读取数据',command=read_data)
# btn.pack()

# entry.place(x=200,y=20)
canvas.create_window(1400, 300, width=100, height=20,
                     window=entry)
canvas.create_window(1400,450, width=100, height=40,    #这里的长和宽是定义按钮的长和宽,100和150是按钮的位置
                     window=btn)





mainloop()
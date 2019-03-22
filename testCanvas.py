import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
# 背景
canvas = tk.Canvas(root, width=1200, height=699, bd=0, highlightthickness=0)
imgpath = '3.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(500, 200, image=photo)
canvas.pack()
entry = tk.Entry(root, insertbackground='blue', highlightthickness=2)
# entry.pack()
class calcParam(object):
    def __init__(self,name,age,win2):
        self.name=name
        self.age=age
    def get_name(self):
        pass
    def get_win2(self):
        self.get_win2=tk.Toplevel(root)
        self.get_win2.title('for win')
        self.get_win2.minsize(900, 700)
        self.var_ety1=tk.StringVar()
        self.ety1=ttk.Entry(self.get_win2,textvariable=self.var_ety1).pack()

        def confirm():
            print(self.var_ety1.get())
            self.get_win2.destroy()
        self.btn1=ttk.Button(self.get_win2,text='确定',command=confirm).pack()


def openwindow():
    a=calcParam(1,2,3)
    a.get_win2()
    print(a.var_ety1.get())
    # tk.messagebox.showinfo(message='ok')
'''
这里的openwindow命令调用以后，会自动
'''
btn1=tk.Button(root,width=20,height=10,text='abc',command=openwindow)
# btn.pack()


b=calcParam(4,5,6)
b.get_win2()
print(b.var_ety1.get())
# entry.place(x=200,y=20)
canvas.create_window(100, 50, width=100, height=20,
                     window=entry)
canvas.create_window(100,150, width=100, height=40,    #这里的长和宽是定义按钮的长和宽,100和150是按钮的位置
                     window=btn1)

root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import scrolledtext
# from tkinter import END

window=tk.Tk()
window.title("Fileopener")
window.geometry('500x400')
# str1="abcde"
# st=ScrolledText(window,height=20,width=30).place(x=10,y=50)
# st=ScrolledText(window).place(x=40,y=50)         #这样写是错误的,不能直接放place函数
st=ScrolledText(window,height=20,width=60)
st.place(x=20,y=50)
# st.pack(side=BOTTOM, fill=Y)   #这2个参数是必须的
# st.place(x=40,y=50)
# print(type(st))
# text1=Text(window,height=30,width=20).place(x=40,y=50)
# st.insert(END,str1)
# var_filename=tk.StringVar()
# var_filename.set("请在此处输入文件名")
filename=ttk.Entry(window,width=20)
filename.place(x=40,y=15)
print(filename.get())
def openfile():
    with open(filename.get())as f:
        str1=f.read()

        # print(str1,type(str1))
        # st.delete('1.0',END)       #1.0指的是第1行第0个字符
        st.insert(END,str1)

#this is a function for saving file
def savefile():
    with open(filename.get(),'w')as f:
        f.write(st.get('1.0',END))


btn_open=ttk.Button(window,text='open',command=openfile)
btn_save=ttk.Button(window,text='save',command=savefile)
# btn_open.grid(column=1,row=1)
# btn_save.grid(column=2,row=1)
btn_open.place(x=240,y=15)
btn_save.place(x=340,y=15)



window.mainloop()
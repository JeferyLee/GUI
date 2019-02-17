import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
root = tk.Tk()
# 背景
canvas = tk.Canvas(root, width=1200, height=699, bd=0, highlightthickness=0)
imgpath = '2.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(500, 200, image=photo)
canvas.pack()
entry = tk.Entry(root, insertbackground='blue', highlightthickness=2)
# entry.pack()
btn=tk.Button(root,width=20,height=10,text='abc')
# btn.pack()

# entry.place(x=200,y=20)
canvas.create_window(100, 50, width=100, height=20,
                     window=entry)
canvas.create_window(100,150, width=100, height=40,    #这里的长和宽是定义按钮的长和宽,100和150是按钮的位置
                     window=btn)

root.mainloop()

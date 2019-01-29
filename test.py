from tkinter import *
from PIL import ImageTk,Image



class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()

if __name__=='__main__':
    app=Application()
    app.mainloop()
'''
制作一个登陆窗口
'''

import tkinter as tk
import tkinter.messagebox
import pickle

window=tk.Tk()
window.title("for login window")
window.geometry('500x400')

canvas=tk.Canvas(window,width=500,height=200)
img_file=tk.PhotoImage(file='1.gif')
image=canvas.create_image(30,30,anchor='nw',image=img_file)  #将图片置于画布上
canvas.pack(side='top')

lb1=tk.Label(window,text='User name: ',width=12,height=3).place(x=110,y=180)
lb2=tk.Label(window,text='Password: ',width=12,height=3).place(x=110,y=220)
var_un=tk.StringVar()
var_un.set("example@python.com")
var_pwd=tk.StringVar()

un_ety=tk.Entry(window,textvariable=var_un).place(x=200,y=200)
pwd_ety=tk.Entry(window,textvariable=var_pwd,show='*').place(x=200,y=240)  #密码使用show函数

def login():
    usr_name=var_un.get()
    usr_pwd=var_pwd.get()
    print('usr_name='+usr_name)
    print('usr_pwd='+usr_pwd)
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usr_info=pickle.load(usr_file)

    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usr_info={'admin':'123'}
            pickle.dump(usr_info,usr_file)

    if usr_name in usr_info:   #如果用户名在文件里面
        print('True')
        print(usr_info[usr_name])
        if usr_pwd == usr_info[usr_name]:  #注意这里的字典变量不能加引号
            tk.messagebox.showinfo(title='Welcome',message='How are you?'+usr_name)
        else:
            tk.messagebox.showinfo(title='Error', message='Your password is wrong,try again!')
    else:   #如果用户名不在
        is_sign_up=tk.messagebox.askyesno(title='Welcome',message='You have not signed up yet,'
                                                                  'sign up today?')
        if is_sign_up:
            sign_up()
def sign_up():
    window_signup=tk.Toplevel(window)
    window_signup.title('for signup')
    window_signup.geometry('350x200')

    lb_un=tk.Label(window_signup,text='Usr name:').place(x=20,y=20)
    lb_pwd=tk.Label(window_signup,text='Password:').place(x=20,y=60)
    lb_pwd_conf = tk.Label(window_signup, text='Password Confirm:').place(x=20, y=100)

    #定义输入框
    var_new_un=tk.StringVar()
    new_un_ety=tk.Entry(window_signup,textvariable=var_new_un).place(x=170,y=22)

    var_new_pwd=tk.StringVar()
    new_pwd_ety=tk.Entry(window_signup,textvariable=var_new_pwd,show='*').place(x=170,y=62)

    var_new_pwdconf=tk.StringVar()
    new_pwdconf_ety=tk.Entry(window_signup,textvariable=var_new_pwdconf,show='*').place(x=170,y=102)

    def signup_success():
        new_un=var_new_un.get()
        new_pwd=var_new_pwd.get()
        new_pwd_conf=var_new_pwdconf.get()

        #先读取已经存在的用户信息文件
        with open('usr_info.pickle','rb') as usr_file:
            exist_usrinfo=pickle.load(usr_file)

        if new_pwd !=new_pwd_conf:
            tk.messagebox.showinfo(title='Error!',message=" Password and Password Confirm must be same.")
        elif new_un in exist_usrinfo:
            tk.messagebox.showinfo(message="User name has been signed up.")
        else:
            #将新的用户信息写入文件
            exist_usrinfo[new_un]=new_pwd
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usrinfo,usr_file)

            tk.messagebox.showinfo(message='Congratulations,you have signed up successfully.')

            window_signup.destroy()

    btn_signup=tk.Button(window_signup,text=' Sign up ',command=signup_success).place(x=140,y=150)

btn1=tk.Button(window,text='  Login  ',command=login).place(x=160,y=290)
btn2=tk.Button(window,text=' Sign up ',command=sign_up).place(x=260,y=290)

window.mainloop()


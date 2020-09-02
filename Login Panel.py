from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x400+500+120")
window.resizable(0, 0)
window.title("Login Portal")



def Log_but():
    if log_e1.get()=='Pawan87__':
        if log_e2.get()=='123':
            messagebox.showinfo("Info","Login Successfull")
        else:
            messagebox.showerror("Error","Password Not found")
    else:
        messagebox.showerror("Error","Invalid Username")


log_e1 = StringVar()
log_e2 = StringVar()


# =================================LOGIN=====================================
def Login():
    f2_login = Frame(bg='lightblue')
    f2_login.place(x=0, y=0, width=600, height=400)

    l3_login = Label(f2_login, text='Login Page', font=("arial", 30, 'bold'), bg='lightblue', fg='red')
    l3_login.place(x=200, y=30)

    l1_login = Label(f2_login, text='Enter Name', bg='lightblue', font=("arial", 12))
    l1_login.place(x=190, y=125)

    l2_login = Label(f2_login, text='Enter Pass', bg='lightblue', font=("arial", 12))
    l2_login.place(x=190, y=180)

    e1_login = Entry(f2_login, textvariable=log_e1)
    e1_login.place(x=300, y=125)

    e2_login = Entry(f2_login, show='*', textvariable=log_e2)
    e2_login.place(x=300, y=180)

    b2_login = Button(f2_login, text="Login", bg='green', fg='yellow', width=10, height=2, command=Log_but)
    b2_login.place(x=290, y=230)

    b3_login = Button(f2_login, text='Back', bg='grey', fg='white', width=7)
    b3_login.place(x=0, y=0)

    b4_login = Button(f2_login, text="Registration", bg='#0C4DF2', width=10, height=2)
    b4_login.place(x=515, y=354)

    b5_login = Button(f2_login, text="Home", bg='#0C4DF2', width=10, height=2)
    b5_login.place(x=7, y=354)

Login()


window.mainloop()
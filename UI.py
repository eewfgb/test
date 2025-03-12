from tkinter import *
from tkinter import messagebox
import back
win = Tk()
#====================================
win.geometry("200x180")
win.resizable(0,0)
win.title("Login Form")
#====================================
oj1 = back.Exam("C:/Users/Pc46/Desktop/exam/data.db")
oj1.create_table()
#====================================
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_pass.delete(0,END)
def insert():
    oj1.insert(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_pass.get())
def sign_up():
    if len(ent_email.get()) == 0 or len(ent_pass.get()) == 0:
        messagebox.showerror("NO!!","please fill the force field")
        return True
    s = oj1.read()
    for i in s:
        if ent_email.get() == i[3]:
            messagebox.showerror("NO!!","This email is already sign in")
            return True
    insert()
def sign_in():
    if len(ent_email.get()) == 0 or len(ent_pass.get()) == 0:
        messagebox.showerror("NO!!","please fill the force field")
        return True
    s = oj1.read()
    for i in s:
        if ent_email.get() == i[3] and ent_pass.get() == i[4]:
            messagebox.showinfo("YES","Wellcome!!")
            clear()
            return True
    messagebox.showerror("NO!!","This account isn't sign in")

#====================================
lbl_fname = Label(win,text="   Fname:")
lbl_fname.grid(row=0,column=0)
lbl_lname = Label(win,text="   Lname:")
lbl_lname.grid(row=1,column=0)
lbl_email = Label(win,text="* Email:")
lbl_email.grid(row=2,column=0)
lbl_pass = Label(win,text="* Password:")
lbl_pass.grid(row=3,column=0)

ent_fname = Entry(win)
ent_fname.grid(row=0,column=1)
ent_lname = Entry(win)
ent_lname.grid(row=1,column=1)
ent_email = Entry(win)
ent_email.grid(row=2,column=1)
ent_pass = Entry(win)
ent_pass.grid(row=3,column=1)

btn_up = Button(win,text="Sign Up",command=sign_up)
btn_up.place(x=40,y=100)
btn_in = Button(win,text="Sign In",command=sign_in)
btn_in.place(x=110,y=99)
win.mainloop()
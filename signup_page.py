from tkinter import *
from PIL import ImageTk
from tkinter import  messagebox
import pymysql

import subprocess

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1550x800+0+0")
        self.window.config(bg = "white")
        self.bg = ImageTk.PhotoImage(file=r"C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/backsign.jpg")  
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)
        frame = Frame(self.window, bg="#ebd3c5")
        frame.place(x=450,y=20,width=500,height=500)
        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="#ebd3c5").place(x=185, y=10)
        title2 = Label(frame, text="Join with us", font=("times new roman",13),bg="#ebd3c5" ).place(x=200, y=60)
        title3 = Label(frame, text="Go to login If you already Create you account", font=("times new roman",13),bg="#ebd3c5" ).place(x=90, y=400)

        name = Label(frame, text="Name", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
         
        self.name_txt = Entry(frame,font=("arial"))
        self.name_txt.place(x=20, y=135, width=200,height=30)

        
        email = Label(frame, text="Email", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)
        
        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20,y=215, width=300,height=30)

        

       
        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=260)
        
        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=305, width=300,height=30)

        self.terms = IntVar()
       
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=120,y=350,width=250)
        self.login= Button(frame,text="Log In",command=self.login_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=120,y=440,width=250)
        
    def signup_func(self):
        if self.name_txt.get()==""  or self.email_txt.get()==""  or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        
        else:
            try:
                connection = pymysql.connect(host="localhost", user="root", password="chethan@123", database="chethan")
                cur = connection.cursor()
                cur.execute("select * from user where email=%s",self.email_txt.get())
                row=cur.fetchone()

                # Check if th entered email id is already exists or not.
                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                else:
                    cur.execute("insert into user (Name,Email,Password) values(%s,%s,%s)",
                                    (
                                       
                                        self.name_txt.get(),
                                        self.email_txt.get(),
                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    subprocess.run(["python", "C:/Users/chethan/OneDrive/DesktopProject/sign language recognition system/login_page.py"])
                    self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    def login_func(self):
        subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/login_page.py"])
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host="localhost", user="root", password="chethan@123", database="chethan")
                cur = connection.cursor()
                cur.execute("select * from user where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=self.window)
                else:
                    messagebox.showinfo("Success","Wellcome to sign language recognition system",parent=self.window)
                    subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/home.py"])
                    # Clear all the entries
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    def reset_fields(self):
        self.name_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()

from tkinter import *
from tkinter import  messagebox
import pymysql
import subprocess
from PIL import  ImageTk

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Login Here ") 
        self.window.geometry("1550x800+0+0")
        self.bg = ImageTk.PhotoImage(file=r"C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/back.jpg");
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)
        self.frame3 = Frame( self.window, bg="#ebd3c5")
        self.frame3.place(x=585,y=50,width=400,height=300)
        self.email_label = Label(self.frame3,text="Email Address", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.email_entry.place(x=50, y=80, width=250)
        self.password_label = Label(self.frame3,text="Password", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray",show="*")
        self.password_entry.place(x=50, y=160, width=250)

        self.login_button = Button(self.frame3,text="Log In",command=self.login_func,font=("times new roman",18, "bold"),bd=0
                                   ,cursor="hand2",bg="blue",fg="white").place(x=100,y=220,width=150)
       
    
    def login_func(self):
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
                    subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/home1.py"])
                    
                    # Clear all the entries
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    
            

    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        root = Tk()
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)
# The main function
if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()
    app = login_page(root)
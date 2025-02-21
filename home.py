from tkinter import *
from PIL import ImageTk
import subprocess

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1550x800+0+0")
       
        self.bg = ImageTk.PhotoImage(file=r"C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/home.png")  
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        title1 = Label(self.window, text="Sign Language Recgonition System", font=("Arial black",20,"bold"),bg="lightgray",fg="black").place(x=500, y=650)
                                                                                                    
        
        self.signup = Button(self.window,text="Sign Up",command=self.sign_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2").place(x=1400,y=30,width=100)
        self.login= Button(self.window,text="Log In",command=self.login_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2").place(x=1250,y=30,width=100)
        self.About = Button(self.window,text="About",font=("times new roman",18, "bold"),bd=0,cursor="hand2").place(x=250,y=30,width=90)
        self.Service= Button(self.window,text="Service",font=("times new roman",18, "bold"),bd=0,cursor="hand2").place(x=150,y=30,width=90)
        self.Home = Button(self.window,text="Home",font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="lightgray").place(x=50,y=30,width=90)
        
    def login_func(self):      
         subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/login_page.py"])
    def sign_func(self): 
         subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/signup_page.py"])   
    
                  
        
if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()

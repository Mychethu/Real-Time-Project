from tkinter import *
from PIL import ImageTk
from tkinter import  messagebox

import subprocess

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1550x800+0+0")
        self.bg = ImageTk.PhotoImage(file=r"C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/home.png")  
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        self.Home = Button(self.window,text="Home",command=self.Home_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2").place(x=50,y=30,width=90)
        self.window = Button(self.window,text="=>Cleck Here To Start Actions<=",command=self.Action_func,font=("Arial Black",25, "bold"),bd=0,cursor="hand2",bg="pink").place(x=430,y=650,width=650)
    def Action_func(self):    
         subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/test.py"])
    def Home_func(self):   
        subprocess.run(["python", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/home.py"])
if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()

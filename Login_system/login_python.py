from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        
        #Background Image
        self.bg=ImageTk.PhotoImage(file="images/2.jpg")
        self.bg_image=Label(self.root, image = self.bg).place(x=0,y=0, relwidth = 1, relheight =1)

        #LoginFrame
        Frame_login = Frame(self.root, bg="black")
        #Frame_login.bg=ImageTk.PhotoImage(file="images/2.jpg")
        #Frame_login.bg_image=Label(Frame_login, image = Frame_login.bg).place(x=0,y=0, relwidth = 1, relheight =1) 
        Frame_login.place(x=330, y=150, width=500, height=400)
        
        
        #Title & Subtitle
        title = Label(Frame_login, text="LOGIN HERE", font=("Consolas",35,"bold"),fg="#6162FF",bg ="black").place(x=111,y=30)
        subtitle=Label(Frame_login, text="ENTER DETAILS BELOW", font=("Cloudy Old Style",11,"bold"),fg="#9595CD",bg ="black").place(x=111,y=80)
        
        #Username
        user=Label(Frame_login, text="USERNAME", font=("Cloudy Old Style",9,"bold"),fg="#9595CD",bg ="black").place(x=111,y=120)
        self.username = Entry(Frame_login, font=("Goudy old style",15),bg="#E7E6E6")
        self.username.place(x=111,y=140)
        
        #Password
        password=Label(Frame_login, text="PASSWORD", font=("Cloudy Old Style",9,"bold"),fg="#9595CD",bg ="black").place(x=111,y=180)
        self.password = Entry(Frame_login, font=("Goudy old style",15),bg="#E7E6E6")
        self.password.place(x=111,y=200)
        
        #Button
        submit = Button(Frame_login,command=self.check_function,cursor="hand2",text="LOGIN", font=("Cloudy Old Style",9),fg="#9595CD",bg ="black").place(x=111,y=240)
        forget = Button(Frame_login,command=self.forgot_password, text="FORGOT PASSWORD?",bd=0,cursor="hand2", font=("Cloudy Old Style",8),fg="blue",bg ="black").place(x=111,y=280, width = 180,height = 40)
        
    def check_function(self):
                usernames = ['JoshuaX','Stone','Victor']
                passwords = ['1234','5678','1112']
                if self.username.get()=="" or self.password.get()=="":
                    messagebox.showerror("Error","All fields are required", parent=self.root)
                elif self.username.get() not in usernames or self.password.get() not in passwords:
                    messagebox.showerror("Error","Incorrect username or password", parent=self.root)
                else:
                    messagebox.showinfo("Access",f"Welcome {self.username.get()}")
    
    def forgot_password(self):
        messagebox.showinfo('Note','Check source code for credentials...')
                    
        
        
        
root = Tk()
obj = Login(root)
root.mainloop()
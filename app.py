from tkinter import *

class NLPapp:
    def __init__(self):
        self.root = Tk()
        self.root.title("OOProject")
        self.root.iconbitmap('/Users/amulpoudel/Developer/OOProject/favicon.zip/favicon.ico')
        self.root.geometry("350x500")
        self.root.configure(bg="#87CEEB")
        self.login_gui()
        #mainloop keeps GUI in screen either it will vanish in matter os secondss
        self.root.mainloop()
        
    def login_gui(self):
        self.clear_screen()
        heading = Label(self.root,text="OOProject",bg="#000000")
        heading.pack(pady=(25,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label1 = Label(self.root,text="Enter email")
        label1.configure(font=('verdana',12,'bold'))
        label1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        label2 = Label(self.root,text="Enter Password")
        label2.configure(font=('verdana',12,'bold'))
        label2.pack(pady=(10,10))
        
        self.password_input = Entry(self.root,width=30,show="#")
        self.password_input.pack(pady=(5,10),ipady=4)
        
        login_btn = Button(self.root,text="Login")
        login_btn.configure(font=('verdana',12,'bold'))
        login_btn.pack(pady=(10,10))
        
        redirect_btn = Button(self.root,text="Not a Member? Register Now",bg="#000000",command=self.register_gui)
        redirect_btn.configure(font=('verdana',12,'bold'))
        redirect_btn.pack()
    
    def clear_screen(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
    def register_gui(self):
        self.clear_screen()
        heading = Label(self.root,text="Register")
        heading.pack(pady=(25,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label0 = Label(self.root,text="Enter Name")
        label0.configure(font=('verdana',12,'bold'))
        label0.pack(pady=(10,10))
        
        self.name_input = Entry(self.root,width=30)
        self.name_input.pack(pady=(5,10),ipady=4)
        
        label1 = Label(self.root,text="Enter email")
        label1.configure(font=('verdana',12,'bold'))
        label1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        label2 = Label(self.root,text="Enter Password")
        label2.configure(font=('verdana',12,'bold'))
        label2.pack(pady=(10,10))
        
        
        self.password_input = Entry(self.root,width=30,show="#")
        self.password_input.pack(pady=(5,10),ipady=4)
        
        login_btn = Button(self.root,text="Already a member??")
        login_btn.configure(font=('verdana',12,'bold'))
        login_btn.pack(pady=(10,10))
        
        redirect_btn = Button(self.root,text="Login",command=self.login_gui)
        redirect_btn.configure(font=('verdana',12,'bold'))
        redirect_btn.pack()
    
        
        
nlp = NLPapp()
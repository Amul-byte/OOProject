from tkinter import *
from mydb import Database
from myapi import NLP
class NLPapp:
    def __init__(self):
        
        self.dbo = Database()
        self.nlp= NLP()
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
        
        login_btn = Button(self.root,text="Login",command=self.perform_login)
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
        
        register_btn = Button(self.root,text="Register",command=self.perform_register)
        register_btn.configure(font=('verdana',12,'bold'))
        register_btn.pack(pady=(10,10))
        
        redirect_btn = Button(self.root,text="Already a member??Login",command=self.login_gui)
        redirect_btn.configure(font=('verdana',12,'bold'))
        redirect_btn.pack()
    
    def perform_register(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name,email,password)
        print(response)
        
    def home_gui(self):
        self.clear_screen()
        heading = Label(self.root,text="Home",bg="#000000")
        heading.pack(pady=(25,30))
        heading.configure(font=('verdana',24,'bold'))
        
        ner_btn = Button(self.root,text="NER",width=30,height=4,command=self.perform_register)
        ner_btn.configure(font=('verdana',12,'bold'))
        ner_btn.pack(pady=(10,10))
        
        lang_btn = Button(self.root,text="Language Detection",width=30,height=4,command=self.login_gui)
        lang_btn.configure(font=('verdana',12,'bold'))
        lang_btn.pack(pady=(10,10))
        
        sentiment_btn = Button(self.root,text="Text Sentiment",width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.configure(font=('verdana',12,'bold'))
        sentiment_btn.pack(pady=(10,10))
        
        logout_btn = Button(self.root,text="Logout",bg="#000000",height=3,width=15,command=self.login_gui)
        logout_btn.configure(font=('verdana',12,'bold'))
        logout_btn.pack()
        
        
    def go_back(self):
        go_back_btn = Button(self.root,text="Go back",bg="#000000",height=2,width=10,command=self.login_gui)
        go_back_btn.configure(font=('verdana',12,'bold'))
        go_back_btn.pack(pady=(10,10))
    
    
    
    def sentiment_gui(self):
        self.clear_screen()
        heading = Label(self.root,text="OOProject",bg="#000000")
        heading.pack(pady=(25,30))
        heading.configure(font=('verdana',24,'bold'))
        
        heading1 = Label(self.root,text="Sentiment Analysis ",bg="#000000")
        heading1.pack(pady=(25,30))
        heading1.configure(font=('verdana',24,'bold'))
        
        label1 = Label(self.root,text="Enter text")
        label1.configure(font=('verdana',12,'bold'))
        label1.pack(pady=(10,10))
        
        self.sentiment_input = Entry(self.root,width=30)
        self.sentiment_input.pack(pady=(5,10),ipady=4)
        
        
        
        sentiment_submit = Button(self.root,text="Analysis sentiment",bg="#000000",height=3,width=15,command=self.do_sentiment_analysis)
        sentiment_submit.configure(font=('verdana',12,'bold'))
        sentiment_submit.pack()
        
        self.sentiment_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.sentiment_result.configure(font=('verdana',12,'bold'))
        self.sentiment_result.pack(pady=(10,10))
        
        
        
        self.go_back()
        
        
    def do_sentiment_analysis(self):
        senti_value = self.sentiment_input.get()
        value = self.nlp.sentiment(senti_value)
        self.sentiment_result['text'] = value
    
    def perform_login(self):
        # name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search_data(email,password)
        print(response)
        
        if response == 1:
            self.home_gui()
        elif response == 0:
            self.register_gui()
        else:
            print("Error Pramul")
            
        
nlp = NLPapp()
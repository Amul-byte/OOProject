import nlpcloud
import dotenv
import os
dotenv.load_dotenv(override=True)

LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

class NLP:
    def __init__(self):
        self.__database = {}
        # self.__first_menu()
        
        
    # def __first_menu(self):
    #     first_input = input("""How would you like to proceed(Press the number accordingly)
    #              1. Register
    #              2. Login
    #              3. Wrong click""")
        
    #     if first_input == '1':
    #         self.__register()
            
    #     elif first_input == "2":
    #         self.__login()
            
    #     else:
    #         exit()
     
        
    # def __register(self):
        
    #     name = input("Enter your name")
    #     email = input("Enter Your email")
    #     password = input("Enter the password")

    #     if email in self.__database:
    #         print("Email is taken")
            
    #     else:
    #         self.__database[email]= [name,password]
    #         print("Register comlete")
    #         print(f"""This is yout info[email : [name,password]]
    #             {self.__database}""")
    #         self.__login()
            
    # def __login(self):
    #     email = input("Enter email")
    #     password= input("Enter your password")
        
    #     if email in self.__database:
    #         if self.__database[email][1]==password:
    #             print("Login Sucessfull")
    #             self.__second_menu()
    #         else:
    #             exit()
    #     else:
    #         print("This email; is not registered")
    #         self.__first_menu()
    
    # def __second_menu(self):
    #     second_input = input("""How would you like to proceed(Press the number accordingly)
    #              1. NER
    #              2. Language detection
    #              3. Sentiment
    #              4. LogOut""")
    #     print("okay")
        
    #     if second_input == '1':
    #         self.__ner()
    #     elif second_input  == "2":
    #         self.__lang_dect()
    #     elif second_input == "3":
    #         self.__sentiment()
    #     elif second_input == "4":
    #         self.__Logout()
    #     else:
    #         print("Wrong key")
    #         exit()
            
            
    def __ner(self):
        para = input("Enter the paragraph")
        term = input("Enter the term yopu want to search")
        client = nlpcloud.Client("finetuned-llama-3-70b", LLAMA_API_KEY, gpu=True)
        response = client.entities(para,
        searched_entity=term)
        print(f"here is your result for [{term}] in [{para}]")
        return response
        
    def __lang_dect(self):
        para = input("Enter the text for language detection")
        client = nlpcloud.Client("python-langdetect", LLAMA_API_KEY, gpu=False)
        response = client.langdetection(para)
        return f"The lngauge in text is [{response}]"
    
    def sentiment(self,para):
        self.para = para
        client = nlpcloud.Client("finetuned-llama-3-70b", LLAMA_API_KEY, gpu=True)
        response = client.sentiment(
        para,target="NLP Cloud")
        return f"The emotion is [{response}]"
        
    def __Logout(self):
        print("Sucessfully Logout")
        self.__first_menu()
    

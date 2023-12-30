#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#Import all commands
from signUp import signUp
from error import error

#Set up connections with the database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]


#set default color
color = "#1e1e1e"
#Import custom font
pyglet.font.add_file('assets/circular-std-medium-500.ttf')

#Function to simplify font size
def font(size):
    return ("circular",size)


#Setting up the GUI
#Creates main home gui
root = ctk.CTk(fg_color = color) 
root.geometry("1200x600+180+120")
loginFrame = ctk.CTkFrame(root, width = 1200, height = 600, fg_color = color)
loginFrame.place(relx = 0, rely = 0)


#Creates login to xxxx label
loginLabel = ctk.CTkLabel(loginFrame, text="Login to xxxx", font=font(50))
loginLabel.place(relx=0.5, rely=0.2, anchor="center")

usernameLabel = ctk.CTkLabel(loginFrame, text="Email", font=font(15))
usernameLabel.place(relx=0.335, rely=0.36, anchor="nw")
usernameEntry = ctk.CTkEntry(loginFrame, font= font(15), placeholder_text= "Name@domain.com", width= 400, height= 40, justify= "center")
usernameEntry.place(relx= 0.5, rely= 0.45, anchor= "center")

passLabel = ctk.CTkLabel(loginFrame, text="Password", font=font(15))
passLabel.place(relx=0.335, rely=0.51, anchor="nw")
passEntry = ctk.CTkEntry(loginFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*")
passEntry.place(relx= 0.5, rely= 0.6, anchor= "center")

def login():
    count = 0
    temp = loginInfo.find()
    for item in temp:
        if str(item['email']) == str(usernameEntry.get()) and str(item['password']) == str(passEntry.get()):
            count +=1  
            
    if count == 1:
        loginFrame.place_forget()
    else:
        error("Wrong password or username!", loginFrame)


#Creates log in up button
loginButton = ctk.CTkButton(loginFrame, text="Login in to xxxx", font=font(25), command= lambda:(login()), fg_color=color)
loginButton.place(relx=0.5, rely=0.75, anchor="center")

#Creates sign up button
signupButton = ctk.CTkButton(loginFrame, text="Sign up for xxxx", font=font(25), command= lambda:(signUp(loginFrame)), fg_color=color)
signupButton.place(relx=0.5, rely=0.9, anchor="center")







#Keeps gui running
if __name__ == "__main__":
    root.mainloop()




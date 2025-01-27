from tkinter import *
import sys
import random

# PASSWORD CREATOR & VALIDATOR
def createpass():
    def validate_password():
        userpass = userpass_entry.get()
        if len(userpass) < 8:
            message_label.config(text="Your Password must be at least 8 characters long.")
        elif userpass.islower():
            message_label.config(text="Your Password must contain at least 1 capital letter.")
        elif userpass.isdigit():
            message_label.config(text="Your Password must contain a letter.")
        elif userpass.isalpha():
            message_label.config(text="Your Password must contain a number.")
        else:
            createpass_menu.destroy()
            created_pass = Tk()
            created_pass.title("Password Creator")
            created_pass.geometry("420x150")
            Label(created_pass, text=f"Your new password is: {userpass}. Don't forget it!").place(relx=0.5, rely=0.2, anchor=CENTER)
            exit_button = Button(created_pass, text="Exit", command=sys.exit)
            exit_button.place(relx=0.5, rely=0.5, anchor=CENTER)
            created_pass.mainloop()

    menu.destroy()
    createpass_menu = Tk()
    createpass_menu.title("Password Creator")
    createpass_menu.geometry("420x150")

    Label(createpass_menu, text="Please enter your new password:").place(relx=0.5, rely=0.1, anchor=CENTER)
    userpass_entry = Entry(createpass_menu)
    userpass_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

    submit_button = Button(createpass_menu, text="Submit", command=validate_password)
    submit_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    message_label = Label(createpass_menu, text="")
    message_label.place(relx=0.5, rely=0.7, anchor=CENTER)

    createpass_menu.mainloop()

#Words for Generated Password in Lists
adj = ["Happy", "Sad", "Big", "Small", "Green", "Blue", "Nice", "Mean"]
noun = ["Dog", "Cat", "Cheese", "Pepper", "Sun", "Moon", "Sky", "Ground"]

#PASSWORD GENERATOR
def genpass():
    randnum = str(random.randint(1000,9999))
    genpass = adj[random.randint(0,7)] + noun[random.randint(0,7)] + randnum
    menu.destroy()
    genpass_menu = Tk()
    genpass_menu.title("Password Creator")
    genpass_menu.geometry("420x100")
    Label(genpass_menu, text="Your new password is " + genpass + ". Don't forget it!").place(relx=0.5, rely=0.3, anchor=CENTER)
    exit_button = Button(genpass_menu, text="Exit", command=sys.exit)
    exit_button.place(relx=0.5, rely=0.7, anchor=CENTER)
    genpass_menu.mainloop()

#MAIN-MENU
menu = Tk()
menu.title("Password Creator")
menu.geometry("420x210")

menu_label = Label(menu, text="Welcome to the Password Creator", pady=30,)
menu_label.place(relx=0.5, rely=0.1, anchor=CENTER)

button1 = Button(menu, text="Password Creator")
button1.place(relx=0.5, rely=0.3, anchor=CENTER)
button1.config(command=createpass)

button2 = Button(menu, text="Password Generator")
button2.place(relx=0.5, rely=0.5, anchor=CENTER)
button2.config(command=genpass)

button3 = Button(menu, text="Exit")
button3.place(relx=0.5, rely=0.7, anchor=CENTER)
button3.config(command=sys.exit)

menu.mainloop()
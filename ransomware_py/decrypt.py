import os
import sys
from cryptography.fernet import Fernet

#giving a choice whether user wants to run program or not
print("This program is dangerous. While it is meant to decrypt, \
if you have the wrong key it will encrypt all files in the current 'my_ransomware.py' \
is housed in as well as all files in the sub directories beyond repair")
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


#reads the saved decryption key file and saves to a variable
with open("thekey.key", "rb") as key:
    secretkey = key.read()


#reads encrypted file contents, decrypts and them writes back to the file. Leaving it unencrypted
for file in files:
    #read binary
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    #write binary
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
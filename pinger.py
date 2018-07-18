# Tool used for pinging.
import os
try:
	os.system("cls")
except:
	os.system("clear")
print("PINGING TOOL")
serv=input("SITE: ")
ping = os.system("ping " + serv + ">NUL")
if ping == 0:
	print("Host Is Up. Continue Pinging?")
	yeno=input("[y/n]")
	if yeno == "y":
		os.system("ping " + serv + " -t -l 32")
else: 
	print("Host Is Down Or Unavaliable.")
	os.system("pause")
# ipfinder.py
import os
import socket
try:
	os.system("cls")
except:
	os.system("clear")
print("IP FINDER")
site=input("SITE: ")
siteip=socket.gethostbyname(site)
print("The IP of " + site + " is " + siteip)
os.system("pause")
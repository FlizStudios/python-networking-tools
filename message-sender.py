#server owner msger
import socket
import os
print("MSG SENDER")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=input("SITE: ")
port=input("PORT: ")
s.connect((server, int(port)))
msg=input("MESSAGE TO SERVER: ")
print("sending")
s.send(msg.encode())
reply = s.recv(4096)
print("click enter to see result")
os.system("pause>NUL")
print(reply)
os.system("pause")
import os
import socket
import sys

os.system("cls")
host = socket.gethostbyname(socket.gethostname())   #ip of the server host machine
port = 9090

users = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #socket difinition; protocol TCP/IP
sock.bind((host, port))

quit = False
print("   ...Server started...    ")

while not quit:
    try:
        data, addr = sock.recvfrom(1024)
        if addr not in users:       #add new user
            users.append(addr)

        print(data.decode("utf-8"))

        #send the message for all users in chat except the sender
        for user in users:
            if addr != user:
                sock.sendto(data, user)

    except:
        print(sys.exc_info())
        print("[ Server stopped ]")
        quit = True;

sock.close()

import os
import socket
import threading
import time

os.system("cls")
print("   ...Welcome to the CryptoMessanger...   ")

shutdown = False
join = False

def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.0.103", 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #socket difinition; protocol TCP/IP
sock.bind((host, port))
sock.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target = receving, args = ("RecvThread", sock))
rT.start()

while not shutdown:
    if not join:
        sock.sendto(("[" + alias + "] >> join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()
            if message != "":
                sock.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)
            time.sleep(0.2)
        except:
            sock.sendto(("[" + alias + "] << left chat ").encode("utf-8"), server)
            shutdown = True


rT.join()
sock.close()

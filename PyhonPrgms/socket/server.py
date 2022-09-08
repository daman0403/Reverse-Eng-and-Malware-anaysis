from http import client
from logging.config import listen
import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("127.0.0.1",8888))
print("listening......")
s.listen(1)

client,addr = s.accept()

print("connected")


while True:
    cmd = input("$ ")
    client.send(cmd.encode())

    if cmd == "exit":
        break

    output = (client.recv(1024)).decode()
    print(output)


client.close()
s.close()












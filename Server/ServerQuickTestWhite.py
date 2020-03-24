import socket
import random
#creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting
s.connect(('127.0.0.1', 13456))
#sending
data = "1"
s.send(data.encode())
#recieving confirmation
data = s.recv(4096).decode()
print(data)
s.send(b"Whit,Pawn,B2,D2")
data = s.recv(4096).decode("utf-8")
print(data)
while True:
	x = 5
#closing
s.close()



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
while True:
	s.send(b"White, Pawn, b2, b4")
	
	
#closing
s.close()



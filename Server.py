import socket
import threading
from queue import Queue

PORT = 13456
HOST = "127.0.0.0"

normalQueue = Queue(maxsize = 5)
blitzQueue = Queue(maxsize = 5)
queueThread = threading.Thread(target =add_toQueue, args=(conn,))
gameThread = threadingThread(target - start_Game, args = (mode,))
mode = 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(5)

def add_toQueue(conn):
    mode = conn.recv(1024).decode()
    if (mode == 1):
        blitzQueue.put(conn)
    else if(mode == 2):
        normalQueue.put(conn)
        else
        print("Error adding to queue. Connection: ", conn)

def start_Game(gameMode)
fdgdfg

while true:
    conn, addr = s.accept()
    print('connected by: ', addr)
    threads.append(queueThread)
    queueThread.start()

    if(normalQueue.qsize() == 2)
    mode = 1
    threads.append(gameThread)
    gameThread.start()

    if(blitzQueue.qsize() == 2)
    mode = 2
    threads.append(gameThread)
    gameThread.start()








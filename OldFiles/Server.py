
import socket
import threading

def add_toQueue(conn):
    mode = conn.recv(1024).decode()
    if mode == 1 or mode == '1':
        normalQueue.append(conn)
        print('added to blitz queue')
    elif mode == 2 or mode == '2':
        print('added to normal queue')
        blitzQueue.append(conn)
    else:
        print("Error adding to queue. Connection: ", conn)

    print('Queue size: ', len(normalQueue))

def start_Game(gameMode):
    print('starting game with mode: ', gameMode)
    if gameMode == 1 or gameMode == '1':
        connection_white = normalQueue.pop(0)
        connection_white.send(b'%d' % 1)
        connection_black = normalQueue.pop(0)
        connection_black.send(b'%d' % 0)
    elif gameMode == 2:
        connection_white = blitzQueue.pop(0)
        connection_white.send(b'%d' % 1)
        connection_black = blitzQueue.pop(0)
        connection_black.send(b'%d' % 0)
    print('game started')
    
PORT = 13456
HOST = "127.0.0.1"

threads = []
#normalQueue = Queue(maxsize = 5)
#blitzQueue = Queue(maxsize = 5)

normalQueue = []
blitzQueue = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
print('socket bound')
s.listen(5)



while True:
    conn, addr = s.accept()
    print('connected by: ', addr)
    queueThread = threading.Thread(target = add_toQueue, args=(conn,))
    threads.append(queueThread)
    queueThread.start()

    print()

    if len(normalQueue) > 1:
        mode = 1
        gameThread = threading.Thread(target = start_Game, args = (mode,))
        threads.append(gameThread)
        gameThread.start()

    if len(blitzQueue) > 1:
        mode = 2
        gameThread = threading.Thread(target = start_Game, args = (mode,))
        threads.append(gameThread)
        gameThread.start()

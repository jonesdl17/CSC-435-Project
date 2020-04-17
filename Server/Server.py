import socket
import threading
import time
from serverGame import *


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

def start_Game(gameMode, connection_white, connection_black):
    try:
        recData = 0
        print('starting game with mode: ', gameMode)
        connection_white.send(b'%d' % 1)
        connection_black.send(b'%d' % 0)
        game = serverGame(gameMode, connection_white, connection_black)
        print('game started')

        gameInProgress, whiteTurn, blackTurn = True, True, False
        mostRecentPlayer = connection_white

        #white goes first
        turn = '1'
        connection_white.send(turn.encode('utf-8'))
        connection_black.send(turn.encode('utf-8'))

        while gameInProgress:

            #While White Turn, Only recieve input from white
            if whiteTurn:
                recData = (connection_white.recv(4096).decode())
                move = recData.split(",")
                mostRecentPlayer = connection_white
                print(move)
                
            #While blackTurn, only recieve input from black
            if blackTurn:
                recData = (connection_black.recv(4096).decode())
                move = recData.split(",")
                mostRecentPlayer = connection_black
                print(move)
            #Check to see if the move recieved from correct color is from correct assigned color
            validColor, whiteTurn, blackTurn = game.checkValidColor(move[0], whiteTurn, blackTurn)
            #If color check is passed then the valid piece movement is checked.
            if(validColor):
                start_tuple = (int(move[2]), int(move[3]))
                end_tuple = (int(move[4]), int(move[5]))
                validMove = game.movePiece(move[1], start_tuple, end_tuple)
                if(not validMove):
                    #if(inCheck())
                        #data = 1 + recData
                        #connection_white.send(data.encode("utf-8"))
                    #connection_black.send(data.encode("utf-8"))
                #els:
                #connection_white.send(data.encode("utf-8"))
                #connection_black.send(data.encode("utf-8"))
                # else:
                    '''data = "2, Invalid Move"
                    mostRecentPlayer.send(data.encode("UTF-8"))'''
                else:
                    connection_white.send(recData.encode('utf-8'))
                    connection_black.send(recData.encode('utf-8'))
                    #time.sleep(1)
                    turn = ''
                    if whiteTurn:
                        turn = '1'
                    else:
                        turn = '0'
                    connection_white.send(turn.encode('utf-8'))
                    connection_black.send(turn.encode('utf-8'))

            '''else:
                data = "2, Invalid Color Assignment"
                mostRecentPlayer.send(data.encode("utf-8"))'''
    except ConnectionError:
        print('connection lost')

    
PORT = 13456
HOST = "127.0.0.1"

threads = []

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

    print("Queue_Start")

    if len(normalQueue) > 1:
        mode = 1
        gameThread = threading.Thread(target = start_Game, args = (mode,normalQueue.pop(0), normalQueue.pop(0)))
        threads.append(gameThread)
        gameThread.start()

    if len(blitzQueue) > 1:
        mode = 2
        gameThread = threading.Thread(target = start_Game, args = (mode,blitzQueue.pop(0),blitzQueue.pop(0)))
        threads.append(gameThread)
        gameThread.start()
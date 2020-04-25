import socket
import threading
import time
from serverGame import *


def add_toQueue(conn):
    mode = conn.recv(1024).decode()
    if mode == 1 or mode == '1':
        normalQueue.append(conn)
    else:
        print("Error adding to queue. Connection: ", conn)


def start_Game(connection_white, connection_black):
    try:
        recData = 0
        connection_white.send(b'%d' % 1)
        connection_black.send(b'%d' % 0)
        game = serverGame(connection_white, connection_black)
        print("Starting Game")
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
                
            #While blackTurn, only recieve input from black
            if blackTurn:
                recData = (connection_black.recv(4096).decode())
                move = recData.split(",")
                mostRecentPlayer = connection_black

            #Check to see if the move recieved from correct color is from correct assigned color
            validColor, whiteTurn, blackTurn = game.checkValidColor(move[0], whiteTurn, blackTurn)
            #If color check is passed then the valid piece movement is checked.
            if(validColor):
                start_tuple = (int(move[2]), int(move[3]))
                end_tuple = (int(move[4]), int(move[5]))
                validMove, endGame = game.movePiece(move[1], start_tuple, end_tuple)
                if(not validMove):
                    #Because when checking the color validity changes the turn, if the move is invalid, swap the turns back.
                    whiteTurn = not whiteTurn
                    blackTurn = not blackTurn
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
                if(endGame):
                    print("Closing Game")
                    connection_black.close()
                    connection_white.close()
                    gameInProgess = False
                    return

            '''else:
                data = "2, Invalid Color Assignment"
                mostRecentPlayer.send(data.encode("utf-8"))'''
    except ConnectionError:
        print('connection lost')

#Accepting connections
def acceptConnection(socket, connection, address):
    try:
        conn, addr = socket.accept()
        connection.append(conn)
        address.append(addr)
    except KeyboardInterrupt:
        return
    except Exception:
        print('accept unsuccessful')
    
PORT = 13456
HOST = "0.0.0.0"

threads = []

normalQueue = []

acceptThread = None
acceptedConn = []
acceptedAddr = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(5)
print("Listening on " + HOST +":"+str(PORT))


try:
    while True:

        if acceptThread == None:
            acceptThread = threading.Thread(target=acceptConnection, args=(s, acceptedConn, acceptedAddr, ))
            acceptThread.start()
        elif len(acceptedConn) != 0 and len(acceptedAddr) != 0:
            acceptThread = None
            conn = acceptedConn.pop(0)
            addr = acceptedAddr.pop(0)
            print('connected by: ', addr)
            queueThread = threading.Thread(target = add_toQueue, args=(conn,))
            threads.append(queueThread)
            queueThread.start()
        if len(normalQueue) > 1:
            gameThread = threading.Thread(target = start_Game, args = (normalQueue.pop(0), normalQueue.pop(0)))
            threads.append(gameThread)
            gameThread.start()
            
except KeyboardInterrupt:
    print("Keyboard Interuppt initiated")
    print("Closing Server in 5 seconds")
    for conn in normalQueue:
        conn.close()
    time.sleep(5)
    s.close()

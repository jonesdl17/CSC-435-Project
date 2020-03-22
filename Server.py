import socket
import threading
from queue import Queue
from serverGame import *

PORT = 13456
HOST = "127.0.0.1"

normalQueue = Queue(maxsize = 5)
blitzQueue = Queue(maxsize = 5)
threads = []

mode = 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(5)


#Adds people to queue based on what mode they choose
def add_toQueue(conn,mode):
    print("mode", mode)
    if (mode == 2):
        blitzQueue.put(conn)
    else:
        if (mode == "1"):
            normalQueue.put(conn)
        else:
            print("Error adding to queue. Connection: ", conn)

def start_Game(gameMode, player1, player2):
    #Method scope variables only.
    recData = 0
    move  = 0
    gameInProgress, whiteTurn, blackTurn = True, True, False
    mostRecentPlayer = player1

    #Sends Players respective Colors.(First persont to join queue gets white.)
    player1.send(b"White")
    player2.send(b"Black")

    print(gameMode)
    #Checks gameMode to see if to make a time limit
    if(gameMode == "1"):
        print("Game")
        game = serverGame(gameMode,player1, player2)
    else:
        game = serverGame(gameMode, player1, player2)
    #Game Time
    while gameInProgress:
        #While White Turn, Only recieve input from white
        if whiteTurn:
            recData = (player1.recv(4096).decode())
            move = recData.split(",")
            mostRecentPlayer = player1
            print(move)
            
        #While blackTurn, only recieve input from black
        if blackTurn:
            recData = (player2.recv(4096).decode())
            move = recData.split(",")
            mostRecentPlayer = player2
            print(move)
        #Check to see if the move recieved from correct color is from correct assigned color
        validColor, whiteTurn, blackTurn = game.checkValidColor(move[0], whiteTurn, blackTurn)
        #If color check is passed then the valid piece movement is checked.
        if(validColor):
            validMove = game.movePiece(move[1], move[2], move[3])
            if(validMove):
                data = recData + ",F"
                print(data)
                #isInCheck = game.checkCheck()
                player1.send(data.encode("utf-8"))
                player2.send(data.encode("utf-8"))
            else:
                mostRecentPlayer.send(b"Invalid Move")

        else:
            mostRecentPlayer.send(b"Invalid Color Assignment")

            
            







while True:
    print("Loop Start")
    #Accepts connections and recieves their modes.
    conn, addr = s.accept()
    mode = conn.recv(4096).decode()
    print('connected by: ', addr)
    print("here",mode)

    #Adds players to Queue based on what mode they choose. Use a thread to add to Queue
    queueThread = threading.Thread(target =add_toQueue, args=(conn,mode,))
    threads.append(queueThread)
    queueThread.start()

    #When a queue reaches two people, a Thread is assigned to add people to a game.
    #Normal Queue
    if(normalQueue.qsize() == 1):
        gameThread = threading.Thread(target = start_Game, args = (mode,normalQueue.get(),normalQueue.get()))
        mode = 1
        threads.append(gameThread)
        gameThread.start()
    #Blitz Queue
    if(blitzQueue.qsize() == 1):
        gameThread = threading.Thread(target = start_Game, args = (mode,blitzQueue.get(),blitzQueue.get()))
        mode = 2
        threads.append(gameThread)
        gameThread.start()
    print("Loop End")






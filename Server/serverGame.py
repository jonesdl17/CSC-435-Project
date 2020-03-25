from moves import *
from serverBoard import *


class serverGame():
    gameBoard = 0
    charToInt = (())
    player1 = 0
    player2 = 0
    mode = 0

    def __init__(self, mode, player1, player2):

        print("ServerGame Started")
        gameBoard = serverBoard()
        gameBoard.init_pieces()
        gameBoard.listBoard()
        self.player1 = player1
        self.player2 = player2
        self.mode = mode


    
    #Checks validMoves using the moves file
    def checkValidMove(self, piece ,start, end):
        startTuple, endTuple = (start[0],start[1]), (end[0],end[1])
        if(piece == "Pawn"):
            return True
            return is_valid_move_pawn(self.board,startTuple, endTuple)
        elif(piece == "Rook"):
            return is_valid_move_rook(self.board, startTuple, endTuple)
        elif(piece == "Bishop"):
            return is_valid_move_bishop(self.board, startTuple, endTuple)
        elif(piece == "Knight"):
            return is_valid_move_bishop(self.board, startTuple, endTuple)
        elif(piece == "Queen"):
            return is_valid_move_queen(self.board, startTuple, endTuple)
        elif(piece == "King"):
            return is_valid_move_king(self.board, startTuple, endTuple)
        else:
            print("Invalid Piece")
            return False

    #Move the piece on the board.
    def movePiece(self, piece, start, end):
        print(serverGame.checkValidMove(piece,start,end))
        if(True):
            #MovePieceCode
            return True
        else:
            return False
            
        
    #Checks to see if recv data is from the correct person
    #returns True/False and alternates turns if it is from the right person
    def checkValidColor(self, color, whiteTurn, blackTurn):
        if whiteTurn & (color == "White"):
            print("Yes")
            whiteTurn = False
            blackTurn = True
        else:
            if blackTurn & (color == "Black"):
                whiteTurn = True
                blackTurn = False
            else:
                return False, whiteTurn, blackTurn
        return True, whiteTurn, blackTurn

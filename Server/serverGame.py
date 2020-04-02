from moves import *
from serverBoard import *


class serverGame():
    gameBoard = None
    charToInt = (())
    player1 = 0
    player2 = 0
    mode = 0

    def __init__(self, mode, player1, player2):

        print("ServerGame Started")
        self.gameBoard = serverBoard()
        self.gameBoard.init_pieces()
        self.gameBoard.listBoard()
        self.player1 = player1
        self.player2 = player2
        self.mode = mode


    
    #Checks validMoves using the moves file
    def checkValidMove(self, piece ,startTuple, endTuple):
        is_valid = False
        if(piece == "Pawn"):
            is_valid = is_valid_move_pawn(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Rook"):
            is_valid =  is_valid_move_rook(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Bishop"):
            is_valid =  is_valid_move_bishop(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Knight"):
            is_valid =  is_valid_move_knight(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Queen"):
            is_valid =  is_valid_move_queen(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "King"):
            is_valid =  is_valid_move_king(self.gameBoard.board, startTuple, endTuple)
        
        #if valid move, move the pieces in the board array.
        if is_valid:
            self.gameBoard.place_piece(startTuple[0], startTuple[1], endTuple[0], endTuple[1])

        return is_valid

    #Move the piece on the board.
    def movePiece(self, piece, start, end):
        valid_move = serverGame.checkValidMove(self, piece,start,end)
        print(valid_move)
        if(valid_move):
            #MovePieceCode
            return True
        else:
            return False
            
        
    #Checks to see if recv data is from the correct person
    #returns True/False and alternates turns if it is from the right person
    def checkValidColor(self, color, whiteTurn, blackTurn):
        if whiteTurn & (color == "White" or color == '1'):
            print("Yes")
            whiteTurn = False
            blackTurn = True
        else:
            if blackTurn & (color == "Black" or color == '0'):
                whiteTurn = True
                blackTurn = False
            else:
                return False, whiteTurn, blackTurn
        return True, whiteTurn, blackTurn

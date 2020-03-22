from moves import *


class serverGame():
    charToInt = (())
    player1 = 0
    player2 = 0
    mode = 0

    def __init__(self, mode, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.mode = mode


    

    def checkValidMove(piece,start, end):
        startTuple, endTuple = (start[0],start[1]), (end[0],end[1])
        if(piece == "Pawn"):
            return True
            return moves.is_valid_move_pawn(board,start_tuple, end_tuple)
        else:
            if(piece == "Rook"):
                return moves.is_valid_move_rook(board, start_tuple, end_tuple)
            else:
                if(piece == "Bishop"):
                    return moves.is_valid_move_bishop(board, start_tuple, end_tuple)
                else:
                    if(piece == "Knight"):
                        return moves.is_valid_move_bishop(board, start_tuple, end_tuple)
                    else:
                        if(piece == "Queen"):
                            return moves.is_valid_move_Queen(board, start_tuple, end_tuple)
                        else:
                            #NEED KING
                            print("Invalid Piece")
                            return False
    def movePiece(self, piece, start, end):
        print(serverGame.checkValidMove(piece,start,end))
        if(True):
            #MovePieceCode
            return True
        else:
            return False
            
        

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

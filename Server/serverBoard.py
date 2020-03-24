from serverPiece import *

#initializing the board
class serverBoard():
    board = []

    def __init__(self):
        print("ServerBoard Started")
        for i in range(8):
            self.board.append([0] * 8)


    def init_pieces(self):
        #initialize white pieces
        board[0][0].changeHasPiece(Rook(1))
        board[1][0].changeHasPiece(Knight(1))
        board[2][0].changeHasPiece(Bishop(1))
        board[3][0].changeHasPiece(Queen(1))
        board[4][0].changeHasPiece(King(1))
        board[5][0].changeHasPiece(Bishop(1))
        board[6][0].changeHasPiece(Knight(1))
        board[7][0].changeHasPiece(Rook(1))
        board[0][1].changeHasPiece(Pawn(1))
        board[1][1].changeHasPiece(Pawn(1))
        board[2][1].changeHasPiece(Pawn(1))
        board[3][1].changeHasPiece(Pawn(1))
        board[4][1].changeHasPiece(Pawn(1))
        board[5][1].changeHasPiece(Pawn(1))
        board[6][1].changeHasPiece(Pawn(1))
        board[7][1].changeHasPiece(Pawn(1))
        #initialize black pieces
        board[0][7].changeHasPiece(Rook(0))
        board[1][7].changeHasPiece(Knight(0))
        board[2][7].changeHasPiece(Bishop(0))
        board[3][7].changeHasPiece(Queen(0))
        board[4][7].changeHasPiece(King(0))
        board[5][7].changeHasPiece(Bishop(0))
        board[6][7].changeHasPiece(Knight(0))
        board[7][7].changeHasPiece(Rook(0))
        board[0][6].changeHasPiece(Pawn(0))
        board[1][6].changeHasPiece(Pawn(0))
        board[2][6].changeHasPiece(Pawn(0))
        board[3][6].changeHasPiece(Pawn(0))
        board[4][6].changeHasPiece(Pawn(0))
        board[5][6].changeHasPiece(Pawn(0))
        board[6][6].changeHasPiece(Pawn(0))
        board[7][6].changeHasPiece(Pawn(0))
        print("Pieces has been placed")








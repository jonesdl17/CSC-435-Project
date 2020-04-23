from serverPiece import *
from serverSquare import *


#initializing the board
class serverBoard():
    board = []
    pieces_checking_white_king = []
    pieces_checking_black_king = []

    def __init__(self):
        for i in range(8):
            self.board.append([0] * 8)
        for row in range(8):
            for col in range(8):
                self.board[col][row] = serverSquare(col, row)

    def listBoard(self):
        for row in range(8):
            for col in range(8):
                print(self.board[col][row].getPiece())
                
    def init_pieces(self):
        #initialize white pieces
        self.board[0][0].changeHasPiece(Rook(1))
        self.board[1][0].changeHasPiece(Knight(1))
        self.board[2][0].changeHasPiece(Bishop(1))
        self.board[3][0].changeHasPiece(Queen(1))
        self.board[4][0].changeHasPiece(King(1))
        self.board[5][0].changeHasPiece(Bishop(1))
        self.board[6][0].changeHasPiece(Knight(1))
        self.board[7][0].changeHasPiece(Rook(1))
        self.board[0][1].changeHasPiece(Pawn(1))
        self.board[1][1].changeHasPiece(Pawn(1))
        self.board[2][1].changeHasPiece(Pawn(1))
        self.board[3][1].changeHasPiece(Pawn(1))
        self.board[4][1].changeHasPiece(Pawn(1))
        self.board[5][1].changeHasPiece(Pawn(1))
        self.board[6][1].changeHasPiece(Pawn(1))
        self.board[7][1].changeHasPiece(Pawn(1))
        #initialize black pieces
        self.board[0][7].changeHasPiece(Rook(0))
        self.board[1][7].changeHasPiece(Knight(0))
        self.board[2][7].changeHasPiece(Bishop(0))
        self.board[3][7].changeHasPiece(Queen(0))
        self.board[4][7].changeHasPiece(King(0))
        self.board[5][7].changeHasPiece(Bishop(0))
        self.board[6][7].changeHasPiece(Knight(0))
        self.board[7][7].changeHasPiece(Rook(0))
        self.board[0][6].changeHasPiece(Pawn(0))
        self.board[1][6].changeHasPiece(Pawn(0))
        self.board[2][6].changeHasPiece(Pawn(0))
        self.board[3][6].changeHasPiece(Pawn(0))
        self.board[4][6].changeHasPiece(Pawn(0))
        self.board[5][6].changeHasPiece(Pawn(0))
        self.board[6][6].changeHasPiece(Pawn(0))
        self.board[7][6].changeHasPiece(Pawn(0))

    #Check if the targeted spot is where a king is at
    def hasKingBeenCaptured(self, target_col, target_row):
        try:
            if self.board[target_col][target_row].piece.name == "King":
                return True
        except AttributeError:
            pass
    #place the piece
    def place_piece(self, source_col, source_row, target_col, target_row):
        game = False
        game = self.hasKingBeenCaptured(target_col, target_row)
        if self.board[source_col][source_row].piece.name == "Pawn":
                self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
                self.board[source_col][source_row].piece = None
                self.board[target_col][target_row].piece.madeFirstMove()
        elif self.board[source_col][source_row].piece.name == "Rook":
                self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
                self.board[source_col][source_row].piece = None
        elif self.board[source_col][source_row].piece.name == "Bishop":
                self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
                self.board[source_col][source_row].piece = None
        elif self.board[source_col][source_row].piece.name == "Knight":
                self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
                self.board[source_col][source_row].piece = None
        elif self.board[source_col][source_row].piece.name == "King":
                self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
                self.board[source_col][source_row].piece = None
        elif self.board[source_col][source_row].piece.name == "Queen":
                self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
                self.board[source_col][source_row].piece = None
        else:
            self.board[target_col][target_row].piece = self.board[source_col][source_row].piece
            self.board[source_col][source_row].piece = None

        return game
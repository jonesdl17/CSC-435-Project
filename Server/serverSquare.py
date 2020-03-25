


class serverSquare():
    col = 0
    row = 0

    hasPiece = False
    pieceColor = 0
    piece = None

#constructor creates coordianates, piece attributes are defaulted to none

    def __init__(self, col, row):
        self.col = col
        self.row = row


#tell if it has a piece
    def hasPiece(self):
        return self.hasPiece

#to swap piece stats from having one to none and vice versa
    def changeHasPiece(self, piece):
        if(self.hasPiece == True):
            self.hasPiece = False
            self.piece = None
            self.pieceColor = 0
        else:
            self.hasPiece = True
            self.piece = piece
            self.pieceColor = piece.getColor()
    def getPiece(self):
        return self.piece
#getter for piece color of current location. returns -1 for black, 1 for white 0 for none
    def getPieceColor(self):
        if (self.hasPiece(self)):
            return self.pieceColor
        else:
            return 0

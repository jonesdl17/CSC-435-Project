import pygame

#to create individual squares with own coordiantes, to if it has a piece, and the piece color and piece
class Square():
    xAxis = 0
    yAxis = 0
    col = 0
    row = 0
    coordianates = 0
    hasPiece = False
    pieceColor = 0
    piece = 0

#constructor creates coordianates, piece attributes are defaulted to none
###############currently prints coordiantes(debugging purpose, delete later)
    def __init__(self, col, row):
        self.xAxis = 600/8 * row
        self.yAxis = 600/8 * col
        print(self.xAxis, self.yAxis)
        self.coordianates = (self.xAxis, self.yAxis)

#getter for coordiantes
    def getCoord(self):
        return self.coordianates
#tell if it has a piece
    def hasPiece(self):
        return self.hasPiece

#to swap piece stats from having one to none and vice versa
    def changeHasPiece(self, piece):
        if(self.hasPiece == True):
            self.hasPiece = False
            self.piece = 0
            self.pieceColor = 0
        else:
            self.hasPiece = True
            self.piece = piece
            self.pieceColor = piece.getColor()

#getter for piece color of current location. returns -1 for black, 1 for white 0 for none
    def getPieceColor(self):
        if (self.hasPiece(self)):
            return self.pieceColor
        else:
            return 0
    




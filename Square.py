import pygame
width = 600
height = 600
border_distance_x = 32
border_distance_y = 35
image_width = int((width - border_distance_x * 2)/8)
image_height = int((height - border_distance_y * 2)/8)
#to create individual squares with own coordiantes, to if it has a piece, and the piece color and piece
class Square():
    col = 0
    row = 0
    xAxis = 0
    yAxis = 0
    coordianates = 0
    hasPiece = False
    pieceColor = 0
    piece = None

#constructor creates coordianates, piece attributes are defaulted to none

    def __init__(self, col, row):
        self.xAxis = col * image_width + border_distance_x
        self.yAxis = row * image_height + border_distance_y
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
            self.piece = None
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
    




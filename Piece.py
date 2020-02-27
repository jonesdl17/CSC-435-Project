import pygame
#I think it oragnizes the pieces better, so we don't have to import a ton of imports on board
#1 = white pieces, -1 = Black pieces

class Piece:
    imageSize = [75,75]
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getColor(self):
        return self.color

class King(Piece):
    def __init__(self, color):
        super().__init__("King", color)
        if color == 1:
            self.image = "./King-White.png"
        else:
            self.image = "./King-Black.png"
       

class Queen(Piece):
    def __init__(self, color):
        super().__init__("Queen", color)
        if color == 1:
            self.image = "./Queen-White.png"
        else:
            self.image = "./Queen-Black.png"
       

class Knight(Piece):
    def __init__(self, color):
        super().__init__("Knight", color)
        if color == 1:
            self.image = "./Knight-White.png"
        else:
            self.image = "./Knight-Black.png"
       

class Bishop(Piece):
    def __init__(self, color):
        super().__init__("Bishop", color)
        if color == 1:
            self.image = "./Bishop-White.png"
        else:
            self.image = "./Bishop-Black.png"

class Rook(Piece):
    def __init__(self, color):
        super().__init__("Rook", color)
        if color == 1:
            self.image = "./Rook-White.png"
        else:
            self.image = "./Rook-Black.png"

class Pawn(Piece):
    def __init__(self, color):
        super().__init__("Pawn", color)
        if color == 1:
            self.image = "./Pawn-White.png"
        else:
            self.image = "./Pawn-Black.png"
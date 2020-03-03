import pygame
#I think it oragnizes the pieces better, so we don't have to import a ton of imports on board
#1 = white pieces, -1 = Black pieces

class Piece:
    imageSize = [75,75] 

    
    def __init__(self, name):
        self.name = name

class King(Piece):
    def __init__(self, name):
        super().__init__("King")
        self.image = "./King.png"
       

class Queen(Piece):
    def __init__(self, name):
        super().__init__("Queen")
        self.image = "./Queen.png"
       

class Knight(Piece):
    def __init__(self, name):
        super().__init__("Knight")
        self.image = "./Knight.png"
       

class Bishop(Piece):
    def __init__(self, name):
        super().__init__("Bishop")
        self.image = "./Bishop.png"

class Rook(Piece):
    def __init__(self, name):
        super().__init__("Rook")
        self.image = "./Rook.png"

class Pawn(Piece):
    def __init__(self, name):
        super().__init__("Pawn")
        self.image = "./Pawn.png"
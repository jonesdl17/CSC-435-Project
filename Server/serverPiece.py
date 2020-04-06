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
       

class Queen(Piece):
    def __init__(self, color):
        super().__init__("Queen", color)
       

class Knight(Piece):
    def __init__(self, color):
        super().__init__("Knight", color)
       

class Bishop(Piece):
    def __init__(self, color):
        super().__init__("Bishop", color)

class Rook(Piece):
    def __init__(self, color):
        super().__init__("Rook", color)

class Pawn(Piece):
    firstMove = True
    def __init__(self, color):
        super().__init__("Pawn", color)

    def checkFirstMove(self):
        return self.firstMove

    def madeFirstMove(self):
        if(self.firstMove):
            self.firstMove = False
            print("Made first Move ", self.firstMove)

    
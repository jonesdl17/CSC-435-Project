from Piece import Piece

class King(Piece):
    def __init__(self, name):
        super().__init__("King")
        self.image = "./King.png"
import pygame
from Piece import Piece

class Rook(Piece):
    def __init__(self, name):
        super().__init__("Rook")
        self.image = "./King.png"
       
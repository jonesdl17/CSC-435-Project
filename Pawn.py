import pygame
from Piece import Piece

class Pawn(Piece):
    def __init__(self, name):
        super().__init__("Pawn")
        self.image = "./King.png"
       
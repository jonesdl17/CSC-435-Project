import pygame
from Piece import Piece

class Queen(Piece):
    def __init__(self, name):
        super().__init__("Queen")
        self.image = "./Queen.png"
       
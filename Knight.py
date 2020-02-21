import pygame
from Piece import Piece

class Knight(Piece):
    def __init__(self, name):
        super().__init__("Knight")
        self.image = "./King.png"
       
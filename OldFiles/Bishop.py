import pygame
from Piece import Piece

class Bishop(Piece):
    def __init__(self, name):
        super().__init__("Bishop")
        self.image = "./King.png"
       
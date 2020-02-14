import pygame
from King import King

width = 600
height = 600
pygame.display.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess")
pygame.display.get_surface().fill((255,255,255))
pygame.display.update()
isWhite = True

for y in range(8):
    for x in range(8):
        color = [255,255,255] if isWhite else [0,0,0]
        pygame.draw.rect(screen, color, pygame.Rect(x * int(width/8), y * int(height/8), int(width/8), int(height/8)))
        isWhite = not isWhite
    isWhite = not isWhite

pygame.display.update() 

board = [[0] * 8] * 8

board[0][0] = King("King")
king_piece = pygame.image.load(board[0][0].image)
screen.blit(king_piece, (100, 200))
print("image loaded")

blnExitGame = False
while not blnExitGame:
    #event = pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blnExitGame = True

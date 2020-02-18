import pygame
from King import King
screen = 0
width = 600
height = 600
king_piece = 0
image_width = int(width/8)
image_height = int(height/8)
board = [[0] * 8] * 8

def draw_board():
    global screen, image_width, image_height
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    pygame.display.get_surface().fill((255,255,255))
    pygame.display.update()
    isWhite = True

    for y in range(8):
        for x in range(8):
            color = [255,255,255] if isWhite else [0,0,0]
            pygame.draw.rect(screen, color, pygame.Rect(x * image_width, y * image_height, image_width, image_height))
            isWhite = not isWhite
        isWhite = not isWhite

    pygame.display.update() 

def draw_pieces(x = 0, y = 0):
    global king_piece
    board[0][0] = King("King")
    king_piece = pygame.image.load(board[0][0].image)

    king_piece = pygame.transform.smoothscale(king_piece, (image_width, image_height))
    screen.blit(king_piece, (x, y))
    pygame.display.update()

def move_piece():
    global screen, board
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    drag = 0
    if click[0] == 1 and king_piece.get_rect().collidepoint((mouse[0], mouse[1])):
        print("yeah")


draw_board()
draw_pieces()

blnExitGame = False
while not blnExitGame:
    #event = pygame.event.wait()
    for event in pygame.event.get():
        move_piece()
        if event.type == pygame.QUIT:
            blnExitGame = True
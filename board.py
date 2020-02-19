import pygame
from Piece import *
screen = 0
width = 600
height = 600
king_piece = 0
king_piece_rect = None
board_image = 0
image_width = int(width/8)
image_height = int(height/8)
board = [[0] * 8] * 8

def draw_board():
    global screen, image_width, image_height, board_image
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    pygame.display.get_surface().fill((255,255,255))
    pygame.display.update()
    
    board_image = pygame.image.load("board.jpg")
    board_image = pygame.transform.smoothscale(board_image, (width, height))
    screen.blit(board_image, (0, 0))
    pygame.display.update() 

def draw_pieces(x = 0, y = 0):
    global king_piece, board, screen, king_piece_rect
    board[0][0] = King("King")
    king_piece = pygame.image.load(board[0][0].image)

    king_piece = pygame.transform.smoothscale(king_piece, (image_width, image_height))
    king_piece_rect = screen.blit(king_piece, (x, y))
    pygame.display.update()

def update_king(x, y):
    global king_piece, board, screen, king_piece_rect
    screen.blit(board_image, (0, 0))
    king_piece_rect = screen.blit(king_piece, (x, y))
    pygame.display.update()

def move_piece():
    global screen, board, king_piece
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    drag = 0

    if click[0] == 1 and king_piece_rect.collidepoint((mouse[0], mouse[1])):
        update_king(mouse[0] - image_width/2, mouse[1] - image_height/2)

draw_board()
draw_pieces()

blnExitGame = False
while not blnExitGame:
    #event = pygame.event.wait()
    for event in pygame.event.get():
        move_piece()
        if event.type == pygame.QUIT:
            blnExitGame = True

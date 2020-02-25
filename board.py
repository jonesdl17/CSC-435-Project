import pygame
from Piece import *
from Square import *
screen = 0
width = 600
height = 600
border_distance = 35
king_piece = None
king_piece_rect = None
board_image = None
image_width = int((width - border_distance * 2)/8)
image_height = int((height - border_distance * 2)/8)
board = [[0] * 8] * 8
dragging = False

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
    global screen, board, king_piece, dragging
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[0] == 1 and king_piece_rect.collidepoint((mouse[0], mouse[1])):
        update_king(mouse[0] - image_width/2, mouse[1] - image_height/2)
        dragging = True

    #This is really bad way to get the piece to fit in the square but it works for now and I will fix it later.
    if click[0] == 0 and dragging:
        x = mouse[0]
        x -= border_distance
        x = int(x / image_width)
        x = x * image_width
        x += border_distance
        if x >= (width - border_distance):
            x = width - border_distance - image_width
        elif x <= border_distance:
            x = border_distance

        y = mouse[1]
        y -= border_distance
        y = int(y / image_height)
        y = y * image_height
        y += border_distance

        if y >= (height - border_distance):
            y = height - border_distance - image_height
        elif y <= border_distance:
            y = border_distance

        update_king(x, y)
        dragging = False

def createSquares():
    i = 0
    for row in range(8):
        for col in range(8):
            board[col][row] = Square(col , row)
draw_board()
draw_pieces()
createSquares()




            


blnExitGame = False
while not blnExitGame:
    #event = pygame.event.wait()
    for event in pygame.event.get():
        move_piece()
        if event.type == pygame.QUIT:
            blnExitGame = True

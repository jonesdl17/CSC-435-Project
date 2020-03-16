import pygame
from Piece import *
from Square import *
from moves import *
from find_valid_moves import *
screen = None
board_image = None
width = 600
height = 600
border_distance_x = 32
border_distance_y = 35
king_piece = None
king_piece_rect = None
image_width = int((width - border_distance_x * 2)/8)
image_height = int((height - border_distance_y * 2)/8)
selected = False
source_col = 0
source_row = 0



#have to initialize it this way because FUCK PYTHON!
board = []
for i in range(8):
    board.append([0] * 8)




def init_board():
    global screen, image_width, image_height, board_image
    for row in range(8):
        for col in range(8):
          board[col][row] = Square(col, row)

    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    pygame.display.get_surface().fill((255,255,255))
    pygame.display.update()
    
    board_image = pygame.image.load("board.jpg")
    board_image = pygame.transform.smoothscale(board_image, (width, height))
    screen.blit(board_image, (0, 0))
    pygame.display.update() 

    init_pieces()

def convert_x_y_to_col_row(x, y):
        x -= border_distance_x
        col = int(x / image_width)
        
        y -= border_distance_y
        row = int(y / image_height)
        if row >= 8:
            row = 7
        elif row <= 0:
            row = 0
        if col >= 8:
            col = 7
        elif col <= 0:
            col = 0

        return (col, row)

def init_pieces():
    global board
    #initialize white pieces
    board[0][0].changeHasPiece(Rook(1))
    board[1][0].changeHasPiece(Knight(1))
    board[2][0].changeHasPiece(Bishop(1))
    board[3][0].changeHasPiece(Queen(1))
    board[4][0].changeHasPiece(King(1))
    board[5][0].changeHasPiece(Bishop(1))
    board[6][0].changeHasPiece(Knight(1))
    board[7][0].changeHasPiece(Rook(1))
    board[0][1].changeHasPiece(Pawn(1))
    board[1][1].changeHasPiece(Pawn(1))
    board[2][1].changeHasPiece(Pawn(1))
    board[3][1].changeHasPiece(Pawn(1))
    board[4][1].changeHasPiece(Pawn(1))
    board[5][1].changeHasPiece(Pawn(1))
    board[6][1].changeHasPiece(Pawn(1))
    board[7][1].changeHasPiece(Pawn(1))
    #initialize black pieces
    board[0][7].changeHasPiece(Rook(0))
    board[1][7].changeHasPiece(Knight(0))
    board[2][7].changeHasPiece(Bishop(0))
    board[3][7].changeHasPiece(Queen(0))
    board[4][7].changeHasPiece(King(0))
    board[5][7].changeHasPiece(Bishop(0))
    board[6][7].changeHasPiece(Knight(0))
    board[7][7].changeHasPiece(Rook(0))
    board[0][6].changeHasPiece(Pawn(0))
    board[1][6].changeHasPiece(Pawn(0))
    board[2][6].changeHasPiece(Pawn(0))
    board[3][6].changeHasPiece(Pawn(0))
    board[4][6].changeHasPiece(Pawn(0))
    board[5][6].changeHasPiece(Pawn(0))
    board[6][6].changeHasPiece(Pawn(0))
    board[7][6].changeHasPiece(Pawn(0))
    update_board()

def update_board():
    global board
    board_image = pygame.image.load("board.jpg")
    board_image = pygame.transform.smoothscale(board_image, (width, height))
    screen.blit(board_image, (0, 0))
    pygame.display.update() 
    for row in range(8):
        for col in range(8):
            if board[col][row].piece != None:
                image = pygame.image.load(board[col][row].piece.image)
                image = pygame.transform.smoothscale(image, (image_width, image_height))
                screen.blit(image, (board[col][row].xAxis, board[col][row].yAxis))

    pygame.display.update()

def select(col, row):
    global source_col, source_row
    source_col = col
    source_row = row
    x, y = board[source_col][source_row].getCoord()
    rec = pygame.Rect(x, y, image_width, image_height)
    pygame.draw.rect(screen, (255, 0, 0), rec, 1)
    pygame.display.update()

def find_valid_move_rook():
    global board, screen, source_col, source_row
    source_tuple = (source_col, source_row)
    is_valid = True
    for i in range (source_row + 1, 8):
        is_valid = is_valid and (board[source_tuple[0]][i].piece == None or board[source_tuple[0]][i].piece.color == 0)
        if is_valid:
            x, y = board[source_tuple[0]][i].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[source_tuple[0]][i].piece != None and board[source_tuple[0]][i].piece.color == 0:
            is_valid = False
    is_valid = True
    for i in range (source_row - 1, -1, -1):
        is_valid = is_valid and (board[source_tuple[0]][i].piece == None or board[source_tuple[0]][i].piece.color == 0)
        if is_valid:
            x, y = board[source_tuple[0]][i].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[source_tuple[0]][i].piece != None and board[source_tuple[0]][i].piece.color == 0:
            is_valid = False
    is_valid = True
    for i in range (source_col + 1, 8):
        is_valid = is_valid and (board[i][source_tuple[1]].piece == None or board[i][source_tuple[1]].piece.color == 0)
        if is_valid:
            x, y = board[i][source_tuple[1]].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[i][source_tuple[1]].piece != None and board[i][source_tuple[1]].piece.color == 0:
            is_valid = False
    is_valid = True
    for i in range (source_col - 1, -1, -1):
        is_valid = is_valid and (board[i][source_tuple[1]].piece == None or board[i][source_tuple[1]].piece.color == 0)
        if is_valid:
            x, y = board[i][source_tuple[1]].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[i][source_tuple[1]].piece != None and board[i][source_tuple[1]].piece.color == 0:
            is_valid = False
    pygame.display.update()

def find_valid_move_pawn():
    global board, screen, source_col, source_row
    if source_row + 1 <= 7 and board[source_col][source_row + 1].piece == None or board[source_col][source_row + 1].piece.color == 0:
        x, y = board[source_col][source_row + 1].getCoord()
        rec = pygame.Rect(x, y, image_width, image_height)
        pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    pygame.display.update()

def find_valid_move_bishop():
    global board, screen, source_col, source_row
    row = source_row
    is_valid = True
    for i in range(source_col + 1, 8):
        row += 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col - 1, -1, -1):
        row += 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col + 1, 8):
        row -= 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col - 1, -1, -1):
        row -= 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    pygame.display.update()


def find_valid_move_knight():
    global board, screen, source_col, source_row
    if source_col - 1 < 8 and source_col - 1 > -1 and source_row + 2 < 8 and source_row + 2 > -1:
        if board[source_col - 1][source_row + 2].piece == None or board[source_col - 1][source_row + 2].piece.color == 0:
            x, y = board[source_col - 1][source_row + 2].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col - 1 < 8 and source_col - 1 > -1 and source_row - 2 < 8 and source_row - 2 > -1:
        if board[source_col - 1][source_row - 2].piece == None or board[source_col - 1][source_row - 2].piece.color == 0:
            x, y = board[source_col - 1][source_row - 2].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col - 2 < 8 and source_col - 2 > -1 and source_row + 1 < 8 and source_row + 1 > -1:
        if board[source_col - 2][source_row + 1].piece == None or board[source_col - 2][source_row + 1].piece.color == 0:
            x, y = board[source_col - 2][source_row + 1].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col - 2 < 8 and source_col - 2 > -1 and source_row - 1 < 8 and source_row - 1 > -1:
        if board[source_col - 2][source_row - 1].piece == None or board[source_col - 2][source_row - 1].piece.color == 0:
            x, y = board[source_col - 2][source_row - 1].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col + 1 < 8 and source_col + 1 > -1 and source_row + 2 < 8 and source_row + 2 > -1:
        if board[source_col + 1][source_row + 2].piece == None or board[source_col + 1][source_row + 2].piece.color == 0:
            x, y = board[source_col + 1][source_row + 2].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col + 1 < 8 and source_col + 1 > -1 and source_row - 2 < 8 and source_row - 2 > -1:
        if board[source_col + 1][source_row - 2].piece == None or board[source_col + 1][source_row - 2].piece.color == 0:
            x, y = board[source_col + 1][source_row - 2].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col + 2 < 8 and source_col + 2 > -1 and source_row + 1 < 8 and source_row + 1 > -1:
        if board[source_col + 2][source_row + 1].piece == None or board[source_col + 2][source_row + 1].piece.color == 0:
            x, y = board[source_col + 2][source_row + 1].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if source_col + 2 < 8 and source_col + 2 > -1 and source_row - 1 < 8 and source_row - 1 > -1:
        if board[source_col + 2][source_row - 1].piece == None or board[source_col + 2][source_row - 1].piece.color == 0:
            x, y = board[source_col + 2][source_row - 1].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    pygame.display.update()

def find_valid_move_king():
    global board, screen, source_col, source_row
    col, row = (source_col, source_row)
    if col - 1 < 8 and col - 1 > -1:
        if row - 1 < 8 and row - 1 > -1:
            if board[col - 1][row - 1].piece == None or board[col - 1][row - 1].piece.color == 0:
                x, y = board[col - 1][row - 1].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[col - 1][row].piece == None or board[col - 1][row].piece.color == 0:
            x, y = board[col - 1][row].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if row - 1 < 8 and row + 1 > -1:
            if board[col - 1][row + 1].piece == None or board[col - 1][row + 1].piece.color == 0:
                x, y = board[col - 1][row + 1].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if row - 1 < 8 and row - 1 > -1:
        if board[col][row - 1].piece == None or board[col][row - 1].piece.color == 0:
            x, y = board[col][row - 1].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if row + 1 < 8 and row + 1 > -1:
        if board[col][row + 1].piece == None or board[col][row + 1].piece.color == 0:
            x, y = board[col][row + 1].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    if col + 1 < 8 and col + 1 > -1:
        if row - 1 < 8 and row - 1 > -1:
            if board[col + 1][row - 1].piece == None or board[col + 1][row - 1].piece.color == 0:
                x, y = board[col + 1][row - 1].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[col + 1][row].piece == None or board[col + 1][row].piece.color == 0:
            x, y = board[col + 1][row].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if row - 1 < 8 and row + 1 > -1:
            if board[col + 1][row + 1].piece == None or board[col + 1][row + 1].piece.color == 0:
                x, y = board[col + 1][row + 1].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
    pygame.display.update()

def find_valid_move_queen():
    global board, screen, source_col, source_row
    source_tuple = (source_col, source_row)
    is_valid = True
    for i in range (source_row + 1, 8):
        is_valid = is_valid and (board[source_tuple[0]][i].piece == None or board[source_tuple[0]][i].piece.color == 0)
        if is_valid:
            x, y = board[source_tuple[0]][i].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[source_tuple[0]][i].piece != None and board[source_tuple[0]][i].piece.color == 0:
            is_valid = False
    is_valid = True
    for i in range (source_row - 1, -1, -1):
        is_valid = is_valid and (board[source_tuple[0]][i].piece == None or board[source_tuple[0]][i].piece.color == 0)
        if is_valid:
            x, y = board[source_tuple[0]][i].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[source_tuple[0]][i].piece != None and board[source_tuple[0]][i].piece.color == 0:
            is_valid = False
    is_valid = True
    for i in range (source_col + 1, 8):
        is_valid = is_valid and (board[i][source_tuple[1]].piece == None or board[i][source_tuple[1]].piece.color == 0)
        if is_valid:
            x, y = board[i][source_tuple[1]].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[i][source_tuple[1]].piece != None and board[i][source_tuple[1]].piece.color == 0:
            is_valid = False
    is_valid = True
    for i in range (source_col - 1, -1, -1):
        is_valid = is_valid and (board[i][source_tuple[1]].piece == None or board[i][source_tuple[1]].piece.color == 0)
        if is_valid:
            x, y = board[i][source_tuple[1]].getCoord()
            rec = pygame.Rect(x, y, image_width, image_height)
            pygame.draw.rect(screen, (0, 0, 255), rec, 1)
        if board[i][source_tuple[1]].piece != None and board[i][source_tuple[1]].piece.color == 0:
            is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col + 1, 8):
        row += 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col - 1, -1, -1):
        row += 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col + 1, 8):
        row -= 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    row = source_row
    is_valid = True
    for i in range(source_col - 1, -1, -1):
        row -= 1
        if row < 8 and row > -1:
            is_valid = is_valid and (board[i][row].piece == None or board[i][row].piece.color == 0)
            if is_valid:
                x, y = board[i][row].getCoord()
                rec = pygame.Rect(x, y, image_width, image_height)
                pygame.draw.rect(screen, (0, 0, 255), rec, 1)
            if board[i][row].piece != None and board[i][row].piece.color == 0:
                is_valid = False
    pygame.display.update()

def find_valid_moves(col, row):
    global board
    if board[col][row].piece.name == "Pawn":
        find_valid_move_pawn()
    if board[col][row].piece.name == "Rook":
        find_valid_move_rook()
    if board[col][row].piece.name == "Bishop":
        find_valid_move_bishop()
    if board[col][row].piece.name == "Knight":
        find_valid_move_knight()
    if board[col][row].piece.name == "King":
        find_valid_move_king()
    if board[col][row].piece.name == "Queen":
        find_valid_move_queen()

def place_piece(target_col, target_row):
    global source_col, source_row, selected
    if board[source_col][source_row].piece.name == "Pawn":
        if is_valid_move_pawn(board, (source_col, source_row), (target_col, target_row)):
            board[target_col][target_row].piece = board[source_col][source_row].piece
            board[source_col][source_row].piece = None
    elif board[source_col][source_row].piece.name == "Rook":
        if is_valid_move_rook(board, (source_col, source_row), (target_col, target_row)):
            board[target_col][target_row].piece = board[source_col][source_row].piece
            board[source_col][source_row].piece = None
    elif board[source_col][source_row].piece.name == "Bishop":
        if is_valid_move_bishop(board, (source_col, source_row), (target_col, target_row)):
            board[target_col][target_row].piece = board[source_col][source_row].piece
            board[source_col][source_row].piece = None
    elif board[source_col][source_row].piece.name == "Knight":
        if is_valid_move_knight(board, (source_col, source_row), (target_col, target_row)):
            board[target_col][target_row].piece = board[source_col][source_row].piece
            board[source_col][source_row].piece = None
    elif board[source_col][source_row].piece.name == "King":
        if is_valid_move_king(board, (source_col, source_row), (target_col, target_row)):
            board[target_col][target_row].piece = board[source_col][source_row].piece
            board[source_col][source_row].piece = None
    elif board[source_col][source_row].piece.name == "Queen":
        if is_valid_move_queen(board, (source_col, source_row), (target_col, target_row)):
            board[target_col][target_row].piece = board[source_col][source_row].piece
            board[source_col][source_row].piece = None
    else:
        board[target_col][target_row].piece = board[source_col][source_row].piece
        board[source_col][source_row].piece = None
    update_board()
    

def handle_click():
    global selected, source_col, source_row
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        col, row = convert_x_y_to_col_row(mouse[0], mouse[1])
        has_piece = board[col][row].piece != None

        if has_piece and not selected and board[col][row].piece.color == 1:
            selected = True
            select(col, row)
            find_valid_moves(col, row)
        elif not has_piece and selected or has_piece and board[col][row].piece.color == 0:
            selected = False
            place_piece(col, row)
        elif selected and row == source_row and col == source_col:
            selected = False
            update_board()
        elif has_piece and board[col][row].piece.color == 1:
            update_board()
            selected = True
            select(col, row)
            find_valid_moves(col, row)


init_board()

blnExitGame = False
while not blnExitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blnExitGame = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click()
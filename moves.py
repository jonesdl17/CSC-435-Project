from Piece import *
def is_valid_move_pawn(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8  and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    if source_tuple[0] == target_tuple[0] and target_tuple[1] == source_tuple[1] + 2 and board[source_tuple[0]][source_tuple[1]].piece.checkFirstMove() and is_in_board or source_tuple[0] == target_tuple[0] and target_tuple[1] == source_tuple[1] - 2 and is_in_board and board[source_tuple[0]][source_tuple[1]].piece.checkFirstMove():
        is_valid = True
    elif source_tuple[0] == target_tuple[0] and target_tuple[1] == source_tuple[1] + 1 or source_tuple[0] == target_tuple[0] and target_tuple[1] == source_tuple[1] - 1 and is_in_board:
        is_valid = True
    return is_valid

def is_valid_move_rook(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8 and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    
    if source_tuple[0] == target_tuple[0] and source_tuple[1] != target_tuple[1]:
        is_valid = True
        if source_tuple[1] < target_tuple[1]:
            for i in range(source_tuple[1] + 1, target_tuple[1]):
                is_valid = is_valid and (board[source_tuple[0]][i].piece == None)
        else:
            for i in range(target_tuple[1] + 1, source_tuple[1]):
                is_valid = is_valid and (board[source_tuple[0]][i].piece == None)
    elif source_tuple[1] == target_tuple[1] and source_tuple[0] != target_tuple[0]:
        is_valid = True
        if source_tuple[0] < target_tuple[0]:
            for i in range(source_tuple[0] + 1, target_tuple[0]):
                is_valid = is_valid and (board[i][source_tuple[1]].piece == None)
        else:
            for i in range(target_tuple[0] + 1, source_tuple[0]):
                is_valid = is_valid and (board[i][source_tuple[1]].piece == None)
    return is_valid

def is_valid_move_bishop(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8 and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    if abs(target_tuple[0] - source_tuple[0]) == abs(target_tuple[1] - source_tuple[1]):
        is_valid = True
        if source_tuple[1] < target_tuple[1]:
            multiplier = -1 if source_tuple[0] > target_tuple[0] else 1
            col = source_tuple[0]
            for i in range(source_tuple[1] + 1, target_tuple[1]):
                col += 1 * multiplier
                is_valid = is_valid and (board[col][i].piece == None)
        else:
            multiplier = -1 if source_tuple[0] < target_tuple[0] else 1
            col = target_tuple[0]
            for i in range(target_tuple[1] + 1, source_tuple[1]):
                col += 1 * multiplier
                is_valid = is_valid and (board[col][i].piece == None)
    return is_valid

def is_valid_move_knight(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8 and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    
    if target_tuple[1] == source_tuple[1] + 2 or target_tuple[1] == source_tuple[1] - 2:
        if target_tuple[0] == source_tuple[0] + 1 or target_tuple[0] == source_tuple[0] -1:
            is_valid = True
    elif target_tuple[0] == source_tuple[0] + 2 or target_tuple[0] == source_tuple[0] - 2:
        if target_tuple[1] == source_tuple[1] + 1 or target_tuple[1] == source_tuple[1] -1:
            is_valid = True
    return is_valid

def is_valid_move_king(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8 and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    
    if abs(target_tuple[0] - source_tuple[0]) == 1 or abs(target_tuple[1] - source_tuple[1]) == 1:
        is_valid = True
    return is_valid

def is_valid_move_queen(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8 and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    
    if source_tuple[0] == target_tuple[0] and source_tuple[1] != target_tuple[1]:
        is_valid = True
        if source_tuple[1] < target_tuple[1]:
            for i in range(source_tuple[1] + 1, target_tuple[1]):
                is_valid = is_valid and (board[source_tuple[0]][i].piece == None)
        else:
            for i in range(target_tuple[1] + 1, source_tuple[1]):
                is_valid = is_valid and (board[source_tuple[0]][i].piece == None)
    elif source_tuple[1] == target_tuple[1] and source_tuple[0] != target_tuple[0]:
        is_valid = True
        if source_tuple[0] < target_tuple[0]:
            for i in range(source_tuple[0] + 1, target_tuple[0]):
                is_valid = is_valid and (board[i][source_tuple[1]].piece == None)
        else:
            for i in range(target_tuple[0] + 1, source_tuple[0]):
                is_valid = is_valid and (board[i][source_tuple[1]].piece == None)
    
    if abs(target_tuple[0] - source_tuple[0]) == abs(target_tuple[1] - source_tuple[1]):
        is_valid = True
        if source_tuple[1] < target_tuple[1]:
            multiplier = -1 if source_tuple[0] > target_tuple[0] else 1
            col = source_tuple[0]
            for i in range(source_tuple[1] + 1, target_tuple[1]):
                col += 1 * multiplier
                is_valid = is_valid and (board[col][i].piece == None)
        else:
            multiplier = -1 if source_tuple[0] < target_tuple[0] else 1
            col = target_tuple[0]
            for i in range(target_tuple[1] + 1, source_tuple[1]):
                col += 1 * multiplier
                is_valid = is_valid and (board[col][i].piece == None)
    return is_valid
def is_valid_move_pawn(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8  and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    if source_tuple[0] == target_tuple[0] and target_tuple[1] == source_tuple[1] + 1 and is_in_board:
        is_valid = True
    return is_valid

def is_valid_move_rook(board, source_tuple, target_tuple):
    is_valid = False
    is_in_board = target_tuple[0] < 8 and target_tuple[0] >= 0 and target_tuple[1] < 8 and target_tuple[1] >= 0 
    if target_tuple[0] == source_tuple[0] and target_tuple[1] != source_tuple[1]:
        is_valid = True
        for i in range(source_tuple[1] + 1, target_tuple[1] + 1):
            is_valid = is_valid and (board[source_tuple[0]][i].piece == None)
    elif target_tuple[1] == source_tuple[1] and target_tuple[0] != source_tuple[0]:
        is_valid = True
        for i in range(source_tuple[0] + 1, target_tuple[0] + 1):
            is_valid = is_valid and (board[i][source_tuple[1]].piece == None)
    return is_valid
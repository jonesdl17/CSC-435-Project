from moves import *
from serverBoard import *


class serverGame():
    gameBoard = None
    charToInt = (())
    player1 = 0
    player2 = 0

    #Initlizing pieces
    def __init__(self, player1, player2):
        self.gameBoard = serverBoard()
        self.gameBoard.init_pieces()
        self.player1 = player1
        self.player2 = player2


    
    #Checks validMoves using the moves file
    def checkValidMove(self, piece ,startTuple, endTuple):
        is_valid = False
        if(piece == "Pawn"):
            is_valid = is_valid_move_pawn(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Rook"):
            is_valid =  is_valid_move_rook(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Bishop"):
            is_valid =  is_valid_move_bishop(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Knight"):
            is_valid =  is_valid_move_knight(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "Queen"):
            is_valid =  is_valid_move_queen(self.gameBoard.board, startTuple, endTuple)
        elif(piece == "King"):
            is_valid =  is_valid_move_king(self.gameBoard.board, startTuple, endTuple) and not self.check_if_in_check(self.gameBoard.board[startTuple[0]][startTuple[1]].piece.color, endTuple[0], endTuple[1])
        
        game = False
        #if valid move, move the pieces in the board array.
        if is_valid:
            game = self.gameBoard.place_piece(startTuple[0], startTuple[1], endTuple[0], endTuple[1])

        return is_valid, game

    #Move the piece on the board.
    def movePiece(self, piece, start, end):
        valid_move, game = serverGame.checkValidMove(self, piece,start,end)
        if(valid_move):
            #MovePieceCode
            return True, game
        else:
            return False, game
            
        
    #Checks to see if recv data is from the correct person
    #returns True/False and alternates turns if it is from the right person
    def checkValidColor(self, color, whiteTurn, blackTurn):
        if whiteTurn & (color == "White" or color == '1'):
            whiteTurn = False
            blackTurn = True
        else:
            if blackTurn & (color == "Black" or color == '0'):
                whiteTurn = True
                blackTurn = False
            else:
                return False, whiteTurn, blackTurn
        return True, whiteTurn, blackTurn

    #checks to see if square is in check
    def check_if_in_check(self, color, source_col, source_row):
        board = self.gameBoard.board
        isInCheck = False
        other_color = 0 if color == 1 else 1
        #check for pawn
        if color == 1:
            if source_row + 2 < 8 and board[source_col][source_row + 2].piece != None and board[source_col][source_row + 1].piece == None:
                if board[source_col][source_row + 2].piece.color == other_color and (board[source_col][source_row + 2].piece.name == 'Pawn' and not board[source_col][source_row + 2].piece.checkFirstMove()):
                    isInCheck = True
                    print('in check: ')
                    print(source_col, source_row)
                    print(source_col, source_row + 2)
                    print()
            if source_row + 1 < 8 and (board[source_col][source_row + 1].piece != None and board[source_col][source_row + 1].piece.color == other_color and board[source_col][source_row + 1].piece.name == 'Pawn'):
                isInCheck = True
                print('in check: ')
                print(source_col, source_row)
                print(source_col, source_row + 1)
                print()
        elif color == 0:
            if source_row - 2 > -1 and board[source_col][source_row - 2].piece != None and board[source_col][source_row - 1].piece == None:
                if board[source_col][source_row - 2].piece.color == other_color and (board[source_col][source_row - 2].piece.name == 'Pawn' and not board[source_col][source_row - 2].piece.checkFirstMove()):
                    isInCheck = True
                    print('in check: ')
                    print(source_col, source_row)
                    print(source_col, source_row - 2)
                    print()
            if source_row - 1 > -1 and (board[source_col][source_row - 1].piece != None and board[source_col][source_row - 1].piece.color == other_color and board[source_col][source_row - 1].piece.name == 'Pawn'):
                isInCheck = True
                print('in check: ')
                print(source_col, source_row)
                print(source_col, source_row - 1)
                print()

        #check for rook
        source_tuple = (source_col, source_row)
        for i in range (source_row + 1, 8):
            if board[source_tuple[0]][i].piece != None and board[source_tuple[0]][i].piece.color == other_color and (board[source_tuple[0]][i].piece.name == 'Rook' or board[source_tuple[0]][i].piece.name == 'Queen'):
                isInCheck = True
            elif board[source_tuple[0]][i].piece != None:
                break
        for i in range (source_row - 1, -1, -1):
            if board[source_tuple[0]][i].piece != None and board[source_tuple[0]][i].piece.color == other_color and (board[source_tuple[0]][i].piece.name == 'Rook' or board[source_tuple[0]][i].piece.name == 'Queen'):
                isInCheck = True
            elif board[source_tuple[0]][i].piece != None:
                break
        for i in range (source_col + 1, 8):
            if board[i][source_tuple[1]].piece != None and board[i][source_tuple[1]].piece.color == other_color and (board[i][source_tuple[1]].piece.name == 'Rook' or board[i][source_tuple[1]].piece.name == 'Queen'):
                isInCheck = True
            elif board[i][source_tuple[1]].piece != None:
                break
        for i in range (source_col - 1, -1, -1):
            if board[i][source_tuple[1]].piece != None and board[i][source_tuple[1]].piece.color == other_color and (board[i][source_tuple[1]].piece.name == 'Rook' or board[i][source_tuple[1]].piece.name == 'Queen'):
                isInCheck = True
            elif board[i][source_tuple[1]].piece != None:
                break

        #check for bishop
        row = source_row
        for i in range(source_col + 1, 8):
            row += 1
            if row < 8 and row > -1:
                if board[i][row].piece != None and board[i][row].piece.color == other_color and (board[i][row].piece.name == 'Bishop' or board[i][row].piece.name == 'Queen'):
                    isInCheck = True
                elif board[i][row].piece != None:
                    break
        row = source_row
        for i in range(source_col - 1, -1, -1):
            row += 1
            if row < 8 and row > -1:
                if board[i][row].piece != None and board[i][row].piece.color == other_color and (board[i][row].piece.name == 'Bishop' or board[i][row].piece.name == 'Queen'):
                    isInCheck = True
                elif board[i][row].piece != None:
                    break
        row = source_row
        for i in range(source_col + 1, 8):
            row -= 1
            if row < 8 and row > -1:
                if board[i][row].piece != None and board[i][row].piece.color == other_color and (board[i][row].piece.name == 'Bishop' or board[i][row].piece.name == 'Queen'):
                    isInCheck = True
                elif board[i][row].piece != None:
                    break
        row = source_row
        for i in range(source_col - 1, -1, -1):
            row -= 1
            if row < 8 and row > -1:
                if board[i][row].piece != None and board[i][row].piece.color == other_color and (board[i][row].piece.name == 'Bishop' or board[i][row].piece.name == 'Queen'):
                    isInCheck = True
                elif board[i][row].piece != None:
                    break

        #check for knight
        if source_col - 1 < 8 and source_col - 1 > -1 and source_row + 2 < 8 and source_row + 2 > -1:
            if board[source_col - 1][source_row + 2].piece != None and board[source_col - 1][source_row + 2].piece.color == other_color and board[source_col - 1][source_row + 2].piece.name == 'Knight':
                isInCheck = True
        if source_col - 1 < 8 and source_col - 1 > -1 and source_row - 2 < 8 and source_row - 2 > -1:
            if board[source_col - 1][source_row - 2].piece != None and board[source_col - 1][source_row - 2].piece.color == other_color and board[source_col - 1][source_row - 2].piece.name == 'Knight':
                isInCheck = True
        if source_col - 2 < 8 and source_col - 2 > -1 and source_row + 1 < 8 and source_row + 1 > -1:
            if board[source_col - 2][source_row + 1].piece != None and board[source_col - 2][source_row + 1].piece.color == other_color and board[source_col - 2][source_row + 1].piece.name == 'Knight':
                isInCheck = True
        if source_col - 2 < 8 and source_col - 2 > -1 and source_row - 1 < 8 and source_row - 1 > -1:
            if board[source_col - 2][source_row - 1].piece != None and board[source_col - 2][source_row - 1].piece.color == other_color and board[source_col - 2][source_row - 1].piece.name == 'Knight':
                isInCheck = True
        if source_col + 1 < 8 and source_col + 1 > -1 and source_row + 2 < 8 and source_row + 2 > -1:
            if board[source_col + 1][source_row + 2].piece != None and board[source_col + 1][source_row + 2].piece.color == other_color and board[source_col + 1][source_row + 2].piece.name == 'Knight':
                isInCheck = True
        if source_col + 1 < 8 and source_col + 1 > -1 and source_row - 2 < 8 and source_row - 2 > -1:
            if board[source_col + 1][source_row - 2].piece != None and board[source_col + 1][source_row - 2].piece.color == other_color and board[source_col + 1][source_row - 2].piece.name == 'Knight':
                isInCheck = True
        if source_col + 2 < 8 and source_col + 2 > -1 and source_row + 1 < 8 and source_row + 1 > -1:
            if board[source_col + 2][source_row + 1].piece != None and board[source_col + 2][source_row + 1].piece.color == other_color and board[source_col + 2][source_row + 1].piece.name == 'Knight':
                isInCheck = True
        if source_col + 2 < 8 and source_col + 2 > -1 and source_row - 1 < 8 and source_row - 1 > -1:
            if board[source_col + 2][source_row - 1].piece != None and board[source_col + 2][source_row - 1].piece.color == other_color and board[source_col + 2][source_row - 1].piece.name == 'Knight':
                isInCheck = True
        return isInCheck
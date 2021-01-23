def is_a_valid_symbol(symbol):
    return symbol.upper() in ('X', 'O')


def is_a_valid_move(move, board):
    return move in board


def is_a_give_up_move(move):
    return move == '0'


def is_a_win_move(board):
    same_symbol_in_a_row = board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]
    same_symbol_in_a_column = board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]
    same_symbol_in_a_diagonal = board[0] == board[4] == board[8] or board[2] == board[4] == board[6]

    return same_symbol_in_a_row or same_symbol_in_a_column or same_symbol_in_a_diagonal


def were_all_moves_done(board):
    for symbol in board:
        if symbol != 'X' and symbol != 'O':
            return False

    return True


def is_a_tied_game(board):
    return were_all_moves_done(board) and not is_a_win_move(board)






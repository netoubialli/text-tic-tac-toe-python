def is_a_valid_symbol(symbol):
    return symbol.upper() in ('X', 'O')


def check_move(move, game_board):
    if is_a_give_up_move(move):
        raise Exception('You gave up the game.')

    board = game_board.board
    if not is_a_valid_move(move, board):
        return False

    game_board.set_player_move(move)

    if is_a_win_move(board)
        raise Exception(getWinMessage(move, board))


    #if is_a_tie_move(player_move, board):
    #    print_tie_msg()
    #    return

    return True

def is_a_give_up_move(move):
    return move == '0'


def is_a_valid_move(move, board):
    return move in board

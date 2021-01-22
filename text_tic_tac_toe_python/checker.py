from text_tic_tac_toe_python.announcer import print_invalid_move_msg, print_game_board


def is_a_valid_symbol(symbol):
    return symbol.upper() in ('X', 'O')


def check_move(move, game_board):
    pass
    #if is_a_win_move(move, board)

    #if is_a_win_move(player_move, board):
    #    print_win_msg
    #    return

    #if is_a_tie_move(player_move, board):
    #    print_tie_msg()
    #    return


def check_player_move(move, game_board):
    if is_a_give_up_move(move):
        raise Exception('You gave up the game.')

    board = game_board.board
    if not is_a_valid_move(move, board):
        print_invalid_move_msg()
        print_game_board(board)
        return False

    game_board.set_player_move(move)
    check_move(move, game_board)


def is_a_give_up_move(move):
    return move == '0'


def is_a_valid_move(move, board):
    return move in board
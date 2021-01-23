from text_tic_tac_toe_python import constants


def ask_player_symbol():
    player_symbol = input('Which of these symbols would you like to play with: O or X? ')
    return player_symbol.upper()

def print_welcome_msg():
    print('Welcome!')
    print('Some tips to play:')
    print('1) A tic-tac-toe board will be shown to you containing the numbers from 1 to 9 representing each available position on the board, as follows.')
    print_blank_game_board()
    print_blank_line()
    print('2) You choose a symbol to play: O or X.')
    print_blank_line()
    print('3) You make your moves by choosing a number available on the board.')
    print_blank_line()
    print('4) The machine will play against you.')
    print_blank_line()
    print('5) Whoever completes a row, column or diagonal with his symbol, wins the game.')
    print_blank_line()
    print('I hope you have a lot of fun. Let''s play!')
    print_blank_line()


def print_blank_line():
    print('')


def print_game_board(game_board):
    print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
    print('-|-|-')
    print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
    print('-|-|-')
    print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])
    print_blank_line()


def print_blank_game_board():
    print_game_board(constants.EMPTY_BOARD)


def ask_player_next_move():
    return input('Please type the number corresponding your next move or 0 to give up! ')


def print_invalid_move_msg():
    print('You made an invalid move. Please, try again!')


def print_game_result(result):
    print(result)
    print('Thanks for playing and I hope to see you soon!')


def print_machine_turn():
    print('Now it is the machine\'s turn to play!')

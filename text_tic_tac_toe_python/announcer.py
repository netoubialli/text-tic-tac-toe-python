def ask_player_symbol():
    player_symbol = ask_something('Which of these symbols would you like to play with: O or X? ')
    return player_symbol


def ask_something(msg):
    return input(msg)


def print_something(msg):
    print(msg)


def print_welcome_msg():
    print_something('Welcome!')
    print_something('Some tips to play:')
    print_something('1) A tic-tac-toe board will be shown to you containing numbers 1 to 9 representing each available position on the board, as follows.')
    print_blank_game_board()
    print_blank_line()
    print_something('2) You choose a symbol to play: O or X.')
    print_blank_line()
    print_something('3) You make your moves by choosing a number available on the board.')
    print_blank_line()
    print_something('4) The machine will play against you.')
    print_blank_line()
    print_something('5) Whoever completes a row, column or diagonal with his symbol, wins the game.')
    print_blank_line()
    print_something('I hope you have a lot of fun. Let''s play!')
    print_blank_line()


def print_blank_line():
    print_something('')


def print_game_board(game_board):
    print_something(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
    print_something('-|-|-')
    print_something(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
    print_something('-|-|-')
    print_something(game_board[6] + '|' + game_board[7] + '|' + game_board[8])
    print_blank_line()


def print_blank_game_board():
    print_game_board(['1','2','3','4','5','6','7','8','9'])


def ask_player_next_move():
    return ask_something('Please type the number corresponding your next move or 0 to give up! ')


def print_invalid_move_msg():
    print_something('You made an invalid move. Please, try again!')

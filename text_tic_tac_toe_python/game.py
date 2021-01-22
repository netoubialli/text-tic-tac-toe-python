from text_tic_tac_toe_python.announcer import ask_player_symbol, print_welcome_msg, print_game_board, ask_player_next_move
from text_tic_tac_toe_python.checker import is_a_valid_symbol, check_player_move
from text_tic_tac_toe_python.game_board import GameBoard


def play(player_symbol):
    game_board = GameBoard(player_symbol)
    print_game_board(game_board.board)

    #while True:
    #    if not next_player_move(game_board):
    #        continue
        #next_robot_move()


def initialize_game():
    print_welcome_msg()
    player_symbol = ask_player_symbol()
    if not is_a_valid_symbol(player_symbol):
        raise Exception('You only can play with X or O. Please run the game again to inform your option')

    play(player_symbol)


def next_player_move(game_board):
    move = ask_player_next_move()
    check_player_move(move, game_board)

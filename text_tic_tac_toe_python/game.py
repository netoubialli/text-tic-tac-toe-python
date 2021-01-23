import time

from text_tic_tac_toe_python import constants, checker
from text_tic_tac_toe_python.announcer import print_game_result, ask_player_symbol, print_game_board, \
    ask_player_next_move, print_invalid_move_msg, print_machine_turn
from text_tic_tac_toe_python.checker import is_a_valid_symbol, is_a_valid_move, is_a_give_up_move, is_a_win_move, \
    is_a_tied_game
from random import randint


class Game:
    def __init__(self):
        self.machine_symbol = 'X'
        self.player_symbol = ask_player_symbol()
        if not is_a_valid_symbol(self.player_symbol):
            raise Exception('You only can play with X or O. Please run the game again to inform your option')

        if self.player_symbol == 'X':
            self.machine_symbol = 'O'
        self.board = constants.EMPTY_BOARD
        self.is_finished = False
        self.result = ''

        self.play()

    def play(self):
        self.print_the_board()

        while not self.is_finished:
            self.next_round()

        print_game_result(self.result)

    def print_the_board(self):
        print_game_board(self.board)

    def next_round(self):
        self.next_player_move()
        if not self.is_finished:
            self.next_machine_move()

    def next_player_move(self):
        checked = False
        while not checked:
            move = ask_player_next_move()
            if is_a_give_up_move(move):
                self.set_finished('You gave up the game.')
                return

            checked = is_a_valid_move(move, self.board)
            if not checked:
                print_invalid_move_msg()
                self.print_the_board()

        self.set_player_move(move)
        self.print_the_board()

    def next_machine_move(self):
        print_machine_turn()
        time.sleep(1)
        while True:
            move = str(randint(0,8))
            if is_a_valid_move(move, self.board):
                break

        self.set_machine_move(move)
        self.print_the_board()

    def set_player_move(self, move):
        self.set_move(move, self.player_symbol)

    def set_machine_move(self, move):
        self.set_move(move, self.machine_symbol)

    def set_move(self, move, symbol):
        self.board[int(move) - 1] = symbol

        if is_a_win_move(self.board):
            self.set_finished(self.get_win_message(symbol))
        if is_a_tied_game(self.board):
            self.set_finished('We have a tie!!!')

    def set_finished(self, result):
        self.is_finished = True
        self.result = result

    def get_win_message(self, symbol):
        return 'Congratulations!!! You won the game.' if symbol == self.player_symbol else "You lost the game."

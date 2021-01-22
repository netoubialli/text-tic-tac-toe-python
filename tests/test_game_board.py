from unittest import TestCase
from text_tic_tac_toe_python.game_board import GameBoard


class GameBoardTest(TestCase):
    def test_initialize_game_board_with_player_symbol_x_should_set_robot_symbol_o_and_the_board_with_numbers(self):
        game_board = GameBoard('X')

        self.assertEqual('X', game_board.player_symbol, 'Player symbol should be X')
        self.assertEqual('O', game_board.robot_symbol, 'Robot symbol should be O')
        self.assertEqual(['1','2','3','4','5','6','7','8','9'], game_board.board, 'Board should be [1,2,3,4,5,6,7,8,9]')

    def test_initialize_game_board_with_player_symbol_o_should_set_robot_symbol_x_and_the_board_with_numbers(self):
        game_board = GameBoard('O')

        self.assertEqual('O', game_board.player_symbol, 'Player symbol should be O')
        self.assertEqual('X', game_board.robot_symbol, 'Robot symbol should be X')
        self.assertEqual(['1','2','3','4','5','6','7','8','9'], game_board.board, 'Board should be [1,2,3,4,5,6,7,8,9]')

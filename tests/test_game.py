from unittest import TestCase, mock
from text_tic_tac_toe_python import constants
from text_tic_tac_toe_python.game import Game

from random import randint

class GameTest(TestCase):
    def test_initialize_game_with_invalid_symbol_should_raise_an_exception(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol:
            mock_ask_player_symbol.return_value = 'z'

            with self.assertRaises(Exception) as context:
                Game()

            self.assertTrue('You only can play with X or O. Please run the game again to inform your option' in str(context.exception))
            mock_ask_player_symbol.assert_called_once()

    def test_initialize_game_with_player_symbol_x_should_set_machine_symbol_o_and_the_board_with_numbers(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol, \
                mock.patch('text_tic_tac_toe_python.game.Game.play') as mock_play:
            mock_ask_player_symbol.return_value = 'X'
            mock_play.return_value = None

            game = Game()

            self.assertEqual('X', game.player_symbol, 'Player symbol should be X')
            self.assertEqual('O', game.machine_symbol, 'Machine symbol should be O')
            self.assertEqual(constants.EMPTY_BOARD, game.board, 'Board should be [1,2,3,4,5,6,7,8,9]')
            self.assertEqual(False, game.is_finished, 'The game shouldn''t be over')
            self.assertEqual('', game.result, 'The game result should be empty')

    def test_initialize_game_board_with_player_symbol_o_should_set_machine_symbol_x_and_the_board_with_numbers(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol, \
                mock.patch('text_tic_tac_toe_python.game.Game.play') as mock_play:
            mock_ask_player_symbol.return_value = 'O'
            mock_play.return_value = None

            game = Game()

            self.assertEqual('O', game.player_symbol, 'Player symbol should be O')
            self.assertEqual('X', game.machine_symbol, 'Machine symbol should be X')
            self.assertEqual(constants.EMPTY_BOARD, game.board, 'Board should be [1,2,3,4,5,6,7,8,9]')
            self.assertEqual(False, game.is_finished, 'The game shouldn''t be over')
            self.assertEqual('', game.result, 'The game result should be empty')

    def test_initialize_game_with_valid_symbol_should_start_the_game(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol, \
                mock.patch('text_tic_tac_toe_python.game.Game.play') as mock_play:
            mock_ask_player_symbol.return_value = 'X'
            mock_play.return_value = 'The game was started'

            self.assertTrue('The game was started', Game())
            mock_ask_player_symbol.assert_called_once()
            mock_play.assert_called_once()

    def test_give_up_player_move_should_finish_the_game(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol, \
                mock.patch('text_tic_tac_toe_python.game.Game.play') as mock_play, \
                mock.patch('text_tic_tac_toe_python.game.ask_player_next_move') as mock_ask_player_next_move:
            mock_ask_player_symbol.return_value = 'X'
            mock_play.return_value = 'The game was started'
            mock_ask_player_next_move.return_value = '0'

            game = Game()
            game.next_player_move()
            self.assertEqual(True, game.is_finished, 'The game should be over')
            self.assertEqual('You gave up the game.', game.result, 'The game result should be the given up message')

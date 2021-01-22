from unittest import TestCase, mock

from text_tic_tac_toe_python.game import initialize_game


class Game(TestCase):
    def test_initialize_game_with_invalid_symbol_should_raise_an_exception(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol:
            mock_ask_player_symbol.return_value = 'z'

            with self.assertRaises(Exception) as context:
                initialize_game()

            self.assertTrue('You only can play with X or O. Please run the game again to inform your option' in str(context.exception))
            mock_ask_player_symbol.assert_called_once()

    def test_initialize_game_with_valid_symbol_should_start_the_game(self):
        with mock.patch('text_tic_tac_toe_python.game.ask_player_symbol') as mock_ask_player_symbol:
            mock_ask_player_symbol.return_value = 'X'

            with mock.patch('text_tic_tac_toe_python.game.play') as mock_play:
                mock_play.return_value = 'The game was started'

                self.assertTrue('The game was started', initialize_game())
                mock_ask_player_symbol.assert_called_once()
                mock_play.assert_called_once()


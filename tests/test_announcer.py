from unittest import TestCase, mock
from text_tic_tac_toe_python.announcer import ask_player_symbol


class Announcer(TestCase):
    def test_ask_player_symbol_should_be_x(self):
        with mock.patch('text_tic_tac_toe_python.announcer.input') as mock_ask_something:
            mock_ask_something.return_value = 'X'
            player_symbol = ask_player_symbol()
            self.assertTrue(player_symbol == 'X')
            mock_ask_something.assert_called_once()

    def test_ask_player_symbol_should_be_o(self):
        with mock.patch('text_tic_tac_toe_python.announcer.input') as mock_ask_something:
            mock_ask_something.return_value = 'O'
            player_symbol = ask_player_symbol()
            self.assertTrue(player_symbol == 'O')
            mock_ask_something.assert_called_once()

    def test_ask_player_next_move_should_be_1(self):
        with mock.patch('text_tic_tac_toe_python.announcer.input') as mock_ask_something:
            mock_ask_something.return_value = '1'
            player_symbol = ask_player_symbol()
            self.assertTrue(player_symbol == '1')
            mock_ask_something.assert_called_once()

    def test_ask_player_next_move_should_be_2(self):
        with mock.patch('text_tic_tac_toe_python.announcer.input') as mock_ask_something:
            mock_ask_something.return_value = '2'
            player_symbol = ask_player_symbol()
            self.assertTrue(player_symbol == '2')
            mock_ask_something.assert_called_once()
from unittest import TestCase, mock
from text_tic_tac_toe_python.checker import is_a_valid_symbol, is_a_valid_move, is_a_give_up_move, is_a_win_move, \
    were_all_moves_done, is_a_tied_game
from text_tic_tac_toe_python import constants


class Checker(TestCase):
    def test_lower_x_is_valid_should_return_true(self):
        self.assertTrue(is_a_valid_symbol('x'))

    def test_upper_x_is_valid_should_return_true(self):
        self.assertTrue(is_a_valid_symbol('X'))

    def test_lower_o_is_valid_should_return_true(self):
        self.assertTrue(is_a_valid_symbol('o'))

    def test_upper_o_is_valid_should_return_true(self):
        self.assertTrue(is_a_valid_symbol('O'))

    def test_lower_z_is_valid_should_return_false(self):
        self.assertFalse(is_a_valid_symbol('z'))

    def test_upper_z_is_valid_should_return_false(self):
        self.assertFalse(is_a_valid_symbol('Z'))

    def test_1_is_valid_should_return_false(self):
        self.assertFalse(is_a_valid_symbol('1'))

    def test_special_symbol_is_valid_should_return_false(self):
        self.assertFalse(is_a_valid_symbol('@'))

    def test_1_is_a_valid_move_on_an_empty_board_should_return_true(self):
        is_valid = is_a_valid_move('1', constants.EMPTY_BOARD)
        self.assertTrue(is_valid)

    def test_10_is_a_valid_move_on_an_empty_board_should_return_false(self):
        is_valid = is_a_valid_move('10', constants.EMPTY_BOARD)
        self.assertFalse(is_valid)

    def test_3_is_a_valid_move_on_a_complete_board_should_return_false(self):
        is_valid = is_a_valid_move('3', ['X','X','O','O','O','X','X','O','X'])
        self.assertFalse(is_valid)

    def test_0_is_a_give_up_move_should_return_true(self):
        is_give_up = is_a_give_up_move('0')
        self.assertTrue(is_give_up)

    def test_00_is_a_give_up_move_should_return_false(self):
        is_give_up = is_a_give_up_move('00')
        self.assertFalse(is_give_up)

    def test_same_symbols_in_the_first_row_should_be_a_win_move(self):
        is_win = is_a_win_move(['X', 'X', 'X', '4', '5', '6', '7', '8', '9'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_second_row_should_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', '3', 'O', 'O', 'O', '7', '8', '9'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_third_row_should_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', '3', '4', '5', '6', 'X', 'X', 'X'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_first_column_should_be_a_win_move(self):
        is_win = is_a_win_move(['X', '2', '3', 'X', '5', '6', 'X', '8', '9'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_second_column_should_be_a_win_move(self):
        is_win = is_a_win_move(['1', 'O', '3', '4', 'O', '6', '7', 'O', '9'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_third_column_should_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', 'X', '4', '5', 'X', '7', '8', 'X'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_second_column_should_be_a_win_move(self):
        is_win = is_a_win_move(['1', 'O', '3', '4', 'O', '6', '7', 'O', '9'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_left_diagonal_should_be_a_win_move(self):
        is_win = is_a_win_move(['X', '2', '3', '4', 'X', '6', '7', '8', 'X'])
        self.assertTrue(is_win)

    def test_same_symbols_in_the_right_diagonal_should_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', 'X', '4', 'X', '6', 'X', '8', '9'])
        self.assertTrue(is_win)

    def test_different_symbols_in_the_first_row_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['X', 'O', 'X', '4', '5', '6', '7', '8', '9'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_second_row_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', '3', 'X', 'O', 'O', '7', '8', '9'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_third_row_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', '3', '4', '5', '6', 'X', 'X', '9'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_first_column_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['O', '2', '3', 'X', '5', '6', 'X', '8', '9'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_second_column_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['1', 'X', '3', '4', 'O', '6', '7', 'O', '9'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_third_column_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['1', '2', 'X', '4', '5', 'O', '7', '8', 'X'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_second_column_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['1', 'O', '3', '4', 'X', '6', '7', 'O', '9'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_left_diagonal_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['X', '2', '3', '4', 'O', 'O', '7', 'O', 'O'])
        self.assertFalse(is_win)

    def test_different_symbols_in_the_right_diagonal_should_not_be_a_win_move(self):
        is_win = is_a_win_move(['O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X'])
        self.assertFalse(is_win)

    def test_all_moves_were_done_with_an_incomplete_game_should_return_false(self):
        all_moves_done = were_all_moves_done(['1', '2', 'X', 'X', 'O', 'O', 'X', 'O', 'X'])
        self.assertFalse(all_moves_done)

    def test_all_moves_were_done_with_a_complete_game_should_return_true(self):
        all_moves_done = were_all_moves_done(['O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X'])
        self.assertTrue(all_moves_done)

    def test_tied_game_with_an_incomplete_game_should_return_false(self):
        tied_game = is_a_tied_game(['1', '2', 'X', 'X', 'O', 'O', 'X', 'O', 'X'])
        self.assertFalse(tied_game)

    def test_tied_game_with_a_game_won_should_return_false(self):
        tied_game = is_a_tied_game(['X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'O'])
        self.assertFalse(tied_game)

    def test_tied_game_with_a_complete_and_a_game_not_won_should_return_true(self):
        all_moves_done = were_all_moves_done(['O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X'])
        self.assertTrue(all_moves_done)

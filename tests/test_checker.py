from unittest import TestCase, mock
from text_tic_tac_toe_python.checker import is_a_valid_symbol, is_a_valid_move, is_a_give_up_move


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
        is_valid = is_a_valid_move('1', ['1','2','3','4','5','6','7','8','9'])
        self.assertTrue(is_valid)

    def test_10_is_a_valid_move_on_an_empty_board_should_return_false(self):
        is_valid = is_a_valid_move('10', ['1','2','3','4','5','6','7','8','9'])
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

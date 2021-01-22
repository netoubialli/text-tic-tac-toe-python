
class GameBoard:
    player_symbol = None
    robot_symbol = 'X'
    board = ['1','2','3','4','5','6','7','8','9']

    def __init__(self, player_symbol):
        self.player_symbol = player_symbol

        if player_symbol == 'X':
            self.robot_symbol = 'O'

    def set_player_move(self, move):
        self.set_move(move, self.player_symbol)

    def set_move(self, move, symbol):
        self.board[int(move)-1] = symbol

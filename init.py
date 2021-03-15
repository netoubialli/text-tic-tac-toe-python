from text_tic_tac_toe_python.announcer import print_welcome_msg
from text_tic_tac_toe_python.game import Game

if __name__ == '__main__':
    try:
        print_welcome_msg()
        Game()
    except Exception as e:
        print(e)

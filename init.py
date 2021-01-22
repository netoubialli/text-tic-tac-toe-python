from text_tic_tac_toe_python.announcer import print_something
from text_tic_tac_toe_python.game import initialize_game

if __name__ == '__main__':
    try:
        initialize_game()
    except Exception as e:
        print_something(e)

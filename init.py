from text_tic_tac_toe_python.game import initialize_game

if __name__ == '__main__':
    try:
        initialize_game()
    except Exception as e:
        print(e)

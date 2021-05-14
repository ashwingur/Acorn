from game import Game
import os
import sys

instructions = sys.argv
clear_board = False
if len(instructions) <= 1 or len(instructions) > 3:
    print('Usage: python3 run.py <filename> [play]')
    exit()
elif len(instructions ) == 3:
    if instructions[2] == 'play':
        clear_board = True
    else:
        print('Usage: python3 run.py <filename> [play]')
        exit()
filename = instructions[1]

game_object = Game(filename)
game_object.print_grid_to_string()

while True:
    inp = input("\nInput a move: ").lower()
    if inp not in ['w','a','s','d','e']:
        if inp == 'q':
            print('\nBye!')
            exit()
        else:
            game_object.print_grid_to_string()
            print('\nPlease enter a valid move (w, a, s, d, e, q).')
            continue
    if clear_board:
        os.system("clear")

    game_object.game_move(inp)
    game_object.print_grid_to_string()

    if game_object.msg != '':
        print('\n' + game_object.msg)

    if game_object.finished:
        if game_object.lost:
            # Display game over message
            game_object.game_over()
        else:
            # Display game won message
            game_object.game_won()
        break

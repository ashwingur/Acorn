from grid import grid_to_string
from game_parser import parse, read_lines
from game import Game
from player import Player

'''Since the input provided to the grid_to_string() has already been validated
by parse, and the move the player has made has been validated by the game class.
Hence grid will only receive positive cases. However, we will still test negative
cases in case the error was not caught.'''

# Testing a small, simple grid
def test_grid_simple():
    grid = read_lines('board_simple2.txt')
    game_object = Game('board_simple2.txt')
    game_object.start()
    output = '***\nA Y\n***\n\nYou have 0 water buckets.'
    assert output == grid_to_string(grid, game_object.player), "Invalid grid display"
    print('Simple grid test passed')

# Testing a larger grid with many different types of cells
def test_grid_super_hard():
    grid = read_lines('board_super_hard.txt')
    game_object = Game('board_super_hard.txt')
    output = """*A*************
*       2 *  W*
* *** ** **** *
* * WW*   1   *
* ***** ***** *
*  2 *   ** *F*
*W**W***   FFF*
* 1********FFF*
*************Y*

You have 0 water buckets."""
    assert output == grid_to_string(grid,game_object.player), "Invalid grid display"
    print("Super hard grid test passed")


# Edge case of when the grid given is not a matrix of cell objects
def test_grid_empty():
    grid = [' ']
    player = Player()

    try:
        grid_to_string(grid, player)
    except AttributeError as e:
        assert str(e) == "'str' object has no attribute 'display'"


def run_tests():
    test_grid_simple()
    test_grid_super_hard()
    test_grid_empty()

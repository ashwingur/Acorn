from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

# Positive test case where a valid input is given, and the dimensions of the
# returned grid are checked
def test_parse_grid_size():
    lines = ['****\n','X  Y\n','****']
    grid = parse(lines)
    assert len(grid) == 3, "Grid should have 3 rows."
    assert len(grid[0]) == 4, 'Every row in the grid must have 4 cells.'
    print('Testing grid size sucessful')

# A negative case as an empty board is given, and thus the configuration is
# not correct
def test_parse_empty_line():
    line = ['']
    try:
        grid = parse(line)
    except ValueError as e:
        assert str(e) == 'Expected 1 starting position, got 0.'
    print('Testing empty board successful')

# The cells.py class is not required to be tested directly as the grid returned by
# parse contains all the different cell types, which can be tested.
def test_parse_cell_objects():
    lines = ['*XWF\n',' Y11\n']
    grid = parse(lines)
    assert isinstance(grid[0][0],Wall),'Cell should be an object of type Wall'
    assert grid[0][0].display == '*', 'Cell of type "Wall" should have display "*" '

    assert isinstance(grid[0][1],Start),'Cell should be an object of type Start'
    assert grid[0][1].display == 'X', 'Cell of type "Start" should have display "X" '

    assert isinstance(grid[0][2],Water),'Cell should be an object of type Water'
    assert grid[0][2].display == 'W', 'Cell of type "Water" should have display "W" '

    assert isinstance(grid[0][3],Fire),'Cell should be an object of type Fire'
    assert grid[0][3].display == 'F', 'Cell of type "Fire" should have display "F" '

    assert isinstance(grid[1][0],Air),'Cell should be an object of type Air'
    assert grid[1][0].display == ' ', 'Cell of type "Air" should have display " " '

    assert isinstance(grid[1][1],End),'Cell should be an object of type End'
    assert grid[1][1].display == 'Y', 'Cell of type "End" should have display "Y" '

    assert isinstance(grid[1][2],Teleport),'Cell should be an object of type Teleport'
    assert grid[1][2].display == '1', 'Cell of type "Teleport" should have display "1" '
    print('Testing cell objects successful')

# This is a negative case which is also an edge case, as all characters in the given
# grid are valid, but the teleport pad does not have a partner
def test_parse_single_teleport_pad():
    lines = ['*****\n','X 1 Y\n','*****']
    try:
        grid = parse(lines)
    except ValueError as e:
        assert str(e) == 'Teleport pad 1 does not have an exclusively matching pad.'
    print('Testing single teleport pad successful')


def run_tests():
    test_parse_grid_size()
    test_parse_empty_line()
    test_parse_cell_objects()
    test_parse_single_teleport_pad()

from game import Game


# Positive test case that should end up with the player finishing the game
#
def test_game_move_finished():
    game_object = Game('board_medium.txt')
    game_object.game_move('s')
    game_object.game_move('d')
    game_object.game_move('d')
    game_object.game_move('s')
    assert game_object.finished == True, "Game should be in finished state"
    assert game_object.lost == False, "Game should not be lost"
    print('Game finished successfully')

# Negative test case as the player is not supposed to go into a wall
def test_hit_wall():
    game_object = Game('board_medium.txt')
    assert game_object.player.row == 0, "Row position should be 0"
    assert game_object.player.col == 2, "Column position should be 2"
    # Moves that hits a wall on both the left and right of the start position
    game_object.game_move('a')
    assert game_object.player.row == 0, "Row position should be 0"
    assert game_object.player.col == 2, "Column position should be 2"
    game_object.game_move('d')
    assert game_object.player.row == 0, "Row position should be 0"
    assert game_object.player.col == 2, "Column position should be 2"
    print('Wall collision successful')

# Negative edge case to test how the game handles a player trying to go out of
# the map boundary.
def test_out_of_bounds():
    game_object = Game('board_medium.txt')
    assert game_object.player.row == 0, "Row position should be 0"
    assert game_object.player.col == 2, "Column position should be 2"
    game_object.game_move('w')
    assert game_object.player.row == 0, "Row position should be 0"
    assert game_object.player.col == 2, "Column position should be 2"
    print('Out of bounds successful')


def run_tests():
    test_game_move_finished()
    test_hit_wall()
    test_out_of_bounds()

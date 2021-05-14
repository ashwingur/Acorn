from game import Game
# The player class requires a game object to be created, in order to properly test on a grid
# The game_move function runs the player move function

# Positive test case to check if moves and picking up buckets is working
def test_player_position_and_buckets():
    game_object = Game('board_medium.txt')
    assert game_object.player.row == 0, "Player row should be 0"
    assert game_object.player.col == 2, "Player column should be 2"
    assert game_object.player.num_water_buckets == 0, "Player should have 0 water buckets"
    game_object.game_move('s')
    assert game_object.player.row == 1, "Player row should be 1"
    assert game_object.player.col == 2, "Player column should be 2"
    assert game_object.player.num_water_buckets == 1, "Player should have 1 water bucket"
    game_object.game_move('a')
    assert game_object.player.row == 1, "Player row should be 1"
    assert game_object.player.col == 1, "Player column should be 1"
    assert game_object.player.num_water_buckets == 0, "Player should have 0 water buckets"
    game_object.game_move('e')
    assert game_object.player.row == 1, "Player row should be 1"
    assert game_object.player.col == 1, "Player column should be 1"
    assert game_object.player.num_water_buckets == 0, "Player should have 0 water buckets"
    print('Player position and buckets tested successfully')

# Negative test cases are not required as run.py validates the user inputs

def run_tests():
    test_player_position_and_buckets()

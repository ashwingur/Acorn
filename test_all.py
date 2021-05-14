"""
A simple program that will import your tests and run them all!
Be sure you include tests for your other modules like cells and player!

Usage: python3 test_all.py
"""

# Run.py does not need to be tested, as it is essentially the same as being
# an end to end test. Cells.py is also tested in both game_parser and game
# which require cells.py to function correctly. 

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_player import run_tests as test_player

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
test_grid()
test_parser()
test_player()

# Run the e2e script
subprocess.call(['./test_e2e.sh'])

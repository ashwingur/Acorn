class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0

        # This will be updated when the game_object is initialised
        self.row = 0
        self.col = 0

    def move(self, move):
        # Change player position in the correct direction by 1
        # Note that the 'e' move does not require any position to be changed
        if move == 'w':
            self.row -= 1
        elif move == "a":
            self.col -= 1
        elif move == "s":
            self.row += 1
        elif move == "d":
            self.col += 1

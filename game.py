from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import Start, Wall


class Game:
    def __init__(self, filename):
        self.player = Player()
        self.filename = filename
        self.moves_made = []
        self.finished = False
        self.lost = False
        self.grid = read_lines(filename)
        self.msg = ''
        self.start()

        # Attributes used by the solver
        self.picked_bucket = False
        self.on_tp_pad = False

    def start(self):
        # Loop through the grid and find the start cell, and make that the player
        # position
        for i in self.grid:
            for j in i:
                if isinstance(j, Start):
                    self.player.row = j.pos[0]
                    self.player.col = j.pos[1]


    def game_move(self, move):
        # Store current location, so if an illegal move is made, it can go back
        y = self.player.row
        x = self.player.col

        # Perform the given move command
        self.player.move(move)

        if (self.player.row < 0 or self.player.col < 0
        or self.player.row >= len(self.grid) or self.player.col >= len(self.grid[0])):
            # If the player is on the border and tries to step out of bounds, act as a wall
            # None is used in step as we do not require a cell instance here
            result = Wall.step(None,self)
            self.msg = result[2]
        else:
            # The player did not try step out of bounds, so perform the step
            # command for the cell type that the player went to
            result = self.grid[self.player.row][self.player.col].step(self)

            if len(result) == 3:
                self.msg = result[2]
            else:
                # The player moved onto the cell that does not return a message
                self.msg = ''

        isLegalMove, isEndingMove = result[0], result[1]

        if isLegalMove:
            if isEndingMove:
                # Player landed on finish point (Won game)
                self.moves_made.append(move)
                self.finished = True
            else:
                # Player made a legal move that did not win the game_won
                # i.e. player stepped on air,TP pad, water, start
                self.moves_made.append(move)

        else:
            if isEndingMove:
                # Player stepped on fire and died (Game over)
                self.moves_made.append(move)
                self.finished = True
                self.lost = True
            else:
                # Player walked into a wall, revert back to previous position
                self.player.row = y
                self.player.col = x

    def game_over(self):
        # Function to display the game over message when the player loses
        print('\nThe Fire Nation triumphs! The Honourable Furious Forest'\
              ' is reduced to a pile of ash and is scattered to the'\
              ' winds by the next storm... You have been roasted.\n')
        s = 's'
        if len(self.moves_made) == 1:
            s = ''
        print(f'You made {len(self.moves_made)} move{s}.')
        moves = ', '.join(self.moves_made)
        print(f'Your move{s}: {moves}\n')
        print('=====================\n'\
              '===== GAME OVER =====\n'\
              '=====================')

    def game_won(self):
        # Function to display the game won message when the player wins
        print('\n\nYou conquer the treacherous maze set up by the Fire'\
              ' Nation and reclaim the Honourable Furious Forest '\
              'Throne, restoring your hometown back to its former '\
              'glory of rainbow and sunshine! Peace reigns over the'\
              ' lands.\n')
        s = 's'
        if len(self.moves_made) == 1:
            s = ''
        print(f'You made {len(self.moves_made)} move{s}.')
        moves = ', '.join(self.moves_made)
        print(f'Your move{s}: {moves}\n')
        print('=====================\n'\
              '====== YOU WIN! =====\n'\
              '=====================')

    def print_grid_to_string(self):
        print(grid_to_string(self.grid, self.player))

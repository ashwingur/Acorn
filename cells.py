class Start:
    def __init__(self,y,x):
        self.display = 'X'
        self.pos = [y,x]

    def step(self, game):
        # [is_legal_move, is_game ending move]
        # This double boolean return is used in all step functions
        return (True, False)


class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        return (True, True)


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        return (True, False)


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        return (False, False, "You walked into a wall. Oof!")


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        #print("FIREE")
        #exit()
        if game.player.num_water_buckets > 0:
            game.player.num_water_buckets -= 1
            self.display = ' '
            return (True, False,"With your strong acorn arms, you throw a water bucket"\
            " at the fire. You acorn roll your way through the extinguished flames!")
        else:
            return (False, True, "\nYou step into the fires and watch your"\
                    " dreams disappear :(." )


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        self.display = ' '
        game.player.num_water_buckets += 1
        return (True, False, "Thank the Honourable Furious Forest,"\
               " you've found a bucket of water!")


class Teleport:
    def __init__(self, display, y, x):
        self.display = display
        self.partner_location = []
        self.location = [y, x]

    def step(self, game):
        game.player.row = self.partner_location[0]
        game.player.col = self.partner_location[1]
        game.on_tp_pad = True
        return (True, False, "Whoosh! The magical gates break Physics as we "\
        "know it and opens a wormhole through space and time.")

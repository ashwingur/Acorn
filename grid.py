def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    single_string = ""
    row = 0
    column = 0
    # Loop through the grid and use the cells' display attributes
    # If the current position in the grid is the player, replace it with the
    # player's display ('A')
    while row < len(grid):
        while column < len(grid[0]):
            if player.row == row and player.col == column:
                single_string += player.display
            else:
                single_string += grid[row][column].display
            column += 1
        row += 1
        column = 0
        single_string += "\n"

    # Add on the water bucket message with the proper plural phrasing
    buckets = player.num_water_buckets
    s = 's'
    if buckets == 1:
        s = ''
    single_string += f"\nYou have {buckets} water bucket{s}."
    return single_string

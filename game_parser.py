import sys
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    # Read the given file, if it does not exist print error and exit
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print(f'{filename} does not exist!')
        sys.exit()

    return parse(lines)


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    row = 0
    column = 0

    # Counters to help validate the given grid
    x_count = 0
    y_count = 0
    tp_pads_list = []

    # Grid in which the list of list of cell objects will be appended to
    grid = []

    while row < len(lines):
        line = []
        while column < len(lines[0]) - 1: # -1 to ignore \n
            current_cell = lines[row][column]

            if not(current_cell.isnumeric()): # Checking for incorrect letter
                if current_cell == "X":
                    x_count += 1
                    cell_object = Start(row, column)
                    line.append(cell_object)
                elif current_cell == "Y":
                    y_count += 1
                    cell_object = End()
                    line.append(cell_object)
                elif current_cell == "F":
                    cell_object = Fire()
                    line.append(cell_object)
                elif current_cell == "W":
                    cell_object = Water()
                    line.append(cell_object)
                elif current_cell == " ":
                    cell_object = Air()
                    line.append(cell_object)
                elif current_cell == "*":
                    cell_object = Wall()
                    line.append(cell_object)
                else:
                    raise ValueError(f"Bad letter in configuration file: {current_cell}.")
            else: # Checking for invalid teleport pad pairs or 0
                if current_cell == "0":
                    raise ValueError(f"Bad letter in configuration file: {current_cell}.")
                cell_object = Teleport(current_cell, row, column)
                line.append(cell_object)

                hasPair = False
                # If a pair has been successfully found, we can remove it from the list
                # We know also know the 2 locations of the pair, and so we can update
                # the respective partner_location attributes
                for cell in tp_pads_list:
                    if cell.display == cell_object.display:
                        cell.partner_location = [cell_object.location[0],cell_object.location[1]]
                        cell_object.partner_location = [cell.location[0],cell.location[1]]
                        tp_pads_list.remove(cell)
                        hasPair = True

                # If current cell is the first TP pad, then add it to the tp_pads_list
                if not(hasPair):
                    tp_pads_list.append(cell_object)

            column += 1
        # The current row has been completed, move to next row
        grid.append(line)
        column = 0
        row += 1

    # Raising errors for invalid grids
    if x_count != 1:
        raise ValueError(f"Expected 1 starting position, got {x_count}.")
    if y_count != 1:
        raise ValueError(f"Expected 1 ending position, got {y_count}.")
    if tp_pads_list:
        raise ValueError(f"Teleport pad {tp_pads_list[0].display} does not have an exclusively matching pad.")

    return grid

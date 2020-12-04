# Source: https://adventofcode.com/2020/day/3
# Part 1: Count how many trees (#) do you encounter while descending the map (input) with a given pattern
# Part 2: Check multiple slopes and multiple the number of trees encountered. Ex:
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked in Part1.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

# Slope pattern, Ex: (3, 1) --> 3 steps right, 1 step down
slope_list = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

# Upload terrain
terrain = []
with open(r"./day3_input") as fh:
    for row in fh:
        terrain.append(row.strip("\n"))


from math import ceil
from functools import reduce
import operator

# Multiplication equivalent of sum()
prod = lambda lst: reduce(operator.mul, lst, 1)


def update_loc(c_coord, step):

    mov_right = step[0]
    mov_down = step[1]

    x_coord = c_coord[0] + mov_right
    y_coord = c_coord[1] + mov_down

    return (x_coord, y_coord)


def check_slope(slope, terrain):

    # Start coordinates
    loc = (0, 0)

    trees = []
    for i in range(len(terrain)):
        # Get terrain row (Y_coord)
        try:
            t_row = terrain[loc[1]]
        except IndexError:
            print(f"X_coord {loc[1]} out of boundaries of terrain length ({len(terrain)})")
            continue

        # Extend terrain as necessary to locate X_coord. The ratio "X_target_coord / terrain_length" rounded up (ceil)
        # will make it long enough. Ex: Coord 25 in a terrain of length 10 needs to be at least x2.5 (x3) longer
        if loc[0] >= len(t_row):
            ext_factor = ceil(loc[0] / len(t_row)) + 1
            t_row = t_row * ext_factor

        try:
            block = t_row[loc[0]]
        except IndexError:
            print("Fuck!")
            exit()

        # Visual check:
        dis = True
        if not dis:
            print(i, loc, block, t_row, "\n")

        if block == "#":
            trees.append(loc)

        # Get new position coordinates (X, Y) in terrain after every step
        loc = update_loc(loc, slope)

    n_trees = len(trees)

    print(f"Number of trees encountered for slope {slope}: {n_trees}")

    return n_trees


tot_trees = []
for slope in slope_list:
    n_trees = check_slope(slope, terrain)
    tot_trees.append(n_trees)

print(f"Product of total number of trees: {prod(tot_trees)}")

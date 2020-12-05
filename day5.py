# Source: https://adventofcode.com/2020/day/5

# TODO we could validate input,
#  Ex: len(input_str) == 10 and not set(list(input_str)).difference({'F', 'B', 'L', 'R'}) # (only FBLR characters)
boarding_pass = []
with open(r"./day5_input") as fh:
    for row in fh:
        boarding_pass.append(row.strip("\n"))

# Part 1: Find seat values (row, col, id)
# Example of --> input: expect values
# FBFBBFFRLR: row 44, column 5, seat ID 357 (44 * 8 + 5 = 357).
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

# Disable/Enable visual check
dis = True


def get_sector(sector, def_chars, s_type=None):

    if s_type == "row":
        lower_half, upper_half = "F", "B"
    elif s_type == "seat":
        lower_half, upper_half = "L", "R"
    else:
        print(f"ERROR: Invalid type {s_type}")
        exit()

    for c in def_chars:
        min_val, max_val = min(sector), max(sector)

        # +1 due to 0 index of input sector
        dist = (max_val - min_val + 1) / 2
        half_val = min_val + dist

        if not dis:
            print(c, " | ", sector, " | ", f"{min_val} - {half_val} - {max_val}")

        if c == lower_half:
            sector = (min_val, half_val-1)
        elif c == upper_half:
            sector = (half_val, max_val)
        else:
            print(f"ERROR: Invalid character {c}")
            exit()

    if not dis:
        print(f"Input {def_chars} value: {sector}")

    # TODO we could validate output. Ex: assert len(set(sector)) == 1
    return sector


# Start sectors
row_sector = (0, 127)
seat_sector = (0, 8)

seat_id_lst = []
for b_pass in boarding_pass:
    row_chars = b_pass[:7]
    seat_chars = b_pass[-3:]

    sector = get_sector(row_sector, row_chars, s_type="row")
    row = int(min(sector))

    sector = get_sector(seat_sector, seat_chars, s_type="seat")
    seat = int(min(sector))

    seat_id = row * 8 + seat

    if not dis:
        print(f"{b_pass}: row {row}, seat {seat}, ID {seat_id}")

    seat_id_lst.append(seat_id)

print(f"Max observed seat ID: {max(seat_id_lst)}")

# Part 2: Find missing seat IDs
# Observed-IDs range
obv_range = list(range(min(seat_id_lst), max(seat_id_lst)))

miss_ids = set(obv_range).difference(set(seat_id_lst))

print(f"Missing IDs: {miss_ids}")

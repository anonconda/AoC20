# Source: https://adventofcode.com/2020/day/2

from collections import namedtuple, Counter

# Upload information into a convenient data structure
Data = namedtuple("Data", "n_range target password")

data = []
with open(r"./day2_input") as fh:
    for row in fh:
        n_range, c_target, pass_str = row.strip("\n").replace(":", "").split(" ")

        temp = [int(v) for v in n_range.split("-")]
        n_range = (min(temp), max(temp))

        r_data = Data(n_range=n_range, target=c_target, password=pass_str)
        data.append(r_data)

# Part 1: Find if password (2nd column) fits the password policy (1st column)
valid = []
for d in data:
    char_count = Counter(d.password)
    if d.n_range[0] <= char_count[d.target] <= d.n_range[1]:
        valid.append(d)

print(f"Number of valid passwords: {len(valid)}")

# Part 2: Password policy check is changed, see Source above
valid = []
for d in data:
    pos_1, pos_2 = d.n_range
    # Index start from 1
    char_1 = d.password[pos_1-1]
    char_2 = d.password[pos_2-1]

    if char_1 == d.target and char_2 != d.target:
        print(f"{d.target} | {pos_1}-{char_1}, {pos_2}-{char_2} | {d.password}")
        valid.append(d)
    elif char_1 != d.target and char_2 == d.target:
        print(f"{d.target} | {pos_1}-{char_1}, {pos_2}-{char_2} | {d.password}")
        valid.append(d)
    else:
        pass

print(f"Number of valid passwords: {len(valid)}")

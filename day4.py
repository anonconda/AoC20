# Source: https://adventofcode.com/2020/day/4

from collections import defaultdict

# Passport fields
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

pass_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

# Passport data structure: a dictionary (Key: unique passport ID) of a dictionary (containing passport fields)
pass_id = 1
pass_data_obj = defaultdict(lambda: defaultdict(None))

pass_list = []
with open(r"./day4_input") as fh:
    for row in fh:
        # Passports are separated by empty lines
        if not row.strip("\n"):
            # Create new passport object by creating new ID in data structure
            pass_id += 1
        else:
            dt = pass_data_obj[pass_id]
            for field in pass_fields:
                if field in row:
                    field_val = row.strip("\n").split(f"{field}:")[1].split(" ")[0]
                    dt[field] = field_val

print(f"Total passports: {len(pass_data_obj)}")

# Part 1: make cip field optional
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
pass_valid = []
for pass_id, pass_data in pass_data_obj.items():
    valid = True
    for field in required_fields:
        if field not in pass_data.keys():
            valid = False
            continue

    if valid:
        pass_valid.append(pass_data)

print(f"Number of valid passports (1st Pass): {len(pass_valid)}")


# Part2: Strict check of passport fields
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# For hcl check
valid_hcl_char = {"a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "#"}

strict_valid_pass = []
for pass_data in pass_valid:

    # Tracking error messages to help debugging and validate
    error_msg = set()
    valid = True
    for field in pass_data.keys():

        if not 1920 <= int(pass_data["byr"]) <= 2002:
            error_msg.add("Invalid byr: {}".format(pass_data["byr"]))
            valid = False
            continue

        if not 2010 <= int(pass_data["iyr"]) <= 2020:
            error_msg.add("Invalid iyr: {}".format(pass_data["iyr"]))
            valid = False
            continue

        if not 2020 <= int(pass_data["eyr"]) <= 2030:
            error_msg.add("Invalid eyr: {}".format(pass_data["eyr"]))
            valid = False
            continue

        if pass_data["hgt"].endswith("cm"):
            height = pass_data["hgt"].strip("cm")
            if not 150 <= int(height) <= 193:
                error_msg.add("Invalid hgt: {}".format(pass_data["hgt"]))
                valid = False
                continue
        elif pass_data["hgt"].endswith("in"):
            height = pass_data["hgt"].strip("in")
            if not 59 <= int(height) <= 76:
                error_msg.add("Invalid hgt: {}".format(pass_data["hgt"]))
                valid = False
                continue
        else:
            error_msg.add("Invalid hgt: {}".format(pass_data["hgt"]))
            valid = False
            continue

        if pass_data["hcl"].startswith("#"):
            # Check string if of given length with valid char only
            hc = pass_data["hcl"].strip("#")
            if not len(hc) == 6 or set(list(hc)).difference(valid_hcl_char):
                error_msg.add("Invalid hcl: {}".format(pass_data["hcl"]))
                valid = False
                continue
        else:
            error_msg.add("Invalid hcl: {}".format(pass_data["hcl"]))
            valid = False
            continue

        if pass_data["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            error_msg.add("Invalid ecl: {}".format(pass_data["ecl"]))
            valid = False
            continue

        if not len(pass_data["pid"]) == 9:
            error_msg.add("Invalid pid: {}".format(pass_data["pid"]))
            valid = False
            continue
        else:
            try:
                pid_n = int(pass_data["pid"])
            except:
                error_msg.add("Invalid pid: {}".format(pass_data["pid"]))
                valid = False
                continue

    if valid:
        strict_valid_pass.append(pass_data)
    else:
        dis = True
        if not dis:
            print(pass_data)
            print(" ".join(sorted(error_msg)))
            print("\n")


print(f"Number of valid passports (Strict): {len(strict_valid_pass)}")

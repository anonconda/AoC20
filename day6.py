# Source: https://adventofcode.com/2020/day/6

# Disable/Enable visual check
dis = False

groups_answers_lst = []
with open(r"./day6_input") as fh:
    grp = []
    for row in fh:
        # One line per person, Groups of persons separated by empty lines
        if not row.strip("\n") and grp:
            groups_answers_lst.append(grp)
            grp = []
        else:
            per_ans = row.strip("\n")
            grp.append(per_ans)

    # Append last group!
    if grp:
        groups_answers_lst.append(grp)

# Part 1: Find unique elements in group of passengers
n_uniq_lst = []
for grp in groups_answers_lst:
    pooled_ans = "".join(grp)
    n_uniq = len(set(pooled_ans))
    n_uniq_lst.append(n_uniq)

print(f"Sum of the Nº of Unique answers per group: {sum(n_uniq_lst)}\n")

# Part 2: Find common answers among persons in a group (intersect of elements in group)
all_groups_common = []
for i, grp_ans in enumerate(groups_answers_lst, 1):
    # Intersection of all elements in a list
    grp_inter = set(grp_ans[0]).intersection(*grp_ans)
    all_groups_common.append(len(grp_inter))

    if dis:
        print(i, grp_ans, grp_inter, "\n")

print(f"Sum of the Nº of Common answers per group: {sum(all_groups_common)}\n")

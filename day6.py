# Source: https://adventofcode.com/2020/day/6

# Input example:
# This list represents answers from five groups:
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b

groups_answers_lst = []
with open(r"./day6_input") as fh:
    grp = []
    for row in fh:
        if not row.strip("\n"):
            if grp:
                groups_answers_lst.append(grp)
                grp = []
        else:
            per_ans = row.strip("\n")
            grp.append(per_ans)

    # Append last group!
    if grp:
        groups_answers_lst.append(grp)

# Part 1: Find sum of "The number of Combined(*) answers" for each group (*) That's it, unique elements in group. Ex:
# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11

n_uniq_lst = []
for grp in groups_answers_lst:
    pooled_ans = "".join(grp)
    n_uniq = len(set(pooled_ans))
    n_uniq_lst.append(n_uniq)

print(f"Sum of the Nº of Unique answers per group: {sum(n_uniq_lst)}\n")

# Part 2: Find sum of Common(*) answers between members of one group. (*) That's it, intersect of elements in group. Ex:
# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

# Disable/Enable visual check
dis = False

all_groups_common = []
for i, grp_ans in enumerate(groups_answers_lst, 1):
    # Intersection of all elements in a list
    grp_inter = set(grp_ans[0]).intersection(*grp_ans)
    all_groups_common.append(len(grp_inter))

    if dis:
        print(i, grp_ans, grp_inter, "\n")

print(f"Sum of the Nº of Common answers per group: {sum(all_groups_common)}\n")

import sys


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
lines[-1] += "\n"

rows = []
for line in lines:
    input_line = line[:-1]
    row = [int(x) for x in input_line]
    rows.append(row)

a = len(rows)


def get_trees_towards_right(rows, col_index, row_index):
    row = rows[row_index]
    trees = row[col_index + 1 :]
    return trees


def get_trees_towards_left(rows, col_index, row_index):
    row = rows[row_index]
    first_trees = row[:col_index]
    trees = list(reversed(first_trees))
    return trees


def get_trees_towards_bottom(rows, col_index, row_index):
    column = [row[col_index] for row in rows]
    trees = column[row_index + 1 :]
    return trees


def get_trees_towards_up(rows, col_index, row_index):
    column = [row[col_index] for row in rows]
    first_trees = column[:row_index]
    trees = list(reversed(first_trees))
    return trees


def count_visible_trees(u, me):
    if len(u) >= 1:
        nb = 1
        max_seen = me
        for x in u[1:]:
            if x > max_seen:
                nb += 1
                max_seen = x
        return nb
    else:
        return 0


if __name__ == "__main__":
    scores = {}
    for c in range(a):
        for r in range(a):
            me = rows[r][c]
            up = count_visible_trees(get_trees_towards_up(rows, c, r), me)
            right = count_visible_trees(get_trees_towards_right(rows, c, r), me)
            bottom = count_visible_trees(get_trees_towards_bottom(rows, c, r), me)
            left = count_visible_trees(get_trees_towards_left(rows, c, r), me)
            scores[(c, r)] = up * right * bottom * left
    print(scores)
    print(max(scores.values()))

# for i in range(a):

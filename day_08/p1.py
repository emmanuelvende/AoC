import sys


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
lines[-1] += "\n"

rows = []
for line in lines:
    input_line = line[:-1]
    row = [x for x in input_line]
    rows.append(row)
a = len(rows)


def is_visible(x, first_trees, edge):
    if len(first_trees) == 0:
        return x > edge
    else:
        return x > edge and max(first_trees) < x


def get_column_from_up(rows, col):
    return [row[col] for row in rows]


def get_column_from_down(rows, col):
    return list(reversed(get_column_from_up(rows, col)))


def get_row_from_left(rows, row):
    return rows[row]


def get_row_from_right(rows, row):
    return list(reversed(rows[row]))


# print("=== TEST === get_column_from_up")
# for i in range(a):
#     print(f"{i=} --> {get_column_from_up(rows, col=i)=}")

# print("=== TEST === get_column_from_down")
# for i in range(a):
#     print(f"{i=} --> {get_column_from_down(rows, col=i)=}")

# print("=== TEST === get_row_from_left")
# for i in range(a):
#     print(f"{i=} --> {get_row_from_left(rows, row=i)=}")

# print("=== TEST === get_row_from_right")
# for i in range(a):
#     print(f"{i=} --> {get_row_from_right(rows, row=i)=}")


def check_visibility(trees):
    nb = 0
    edge = trees[0]
    rank = 0

    inside_trees = trees[1:-1]
    for i, x in inside_trees[1:]:
        pass

    # inside_trees = trees[1:-1]
    # for i, x in enumerate(inside_trees):
    #     if is_visible(x, inside_trees[:i], edge):
    #         nb += 1
    #         rank = i
    #         break
    return nb, rank


def detect_from_up(rows, col):
    column = get_column_from_up(rows, col)
    return check_visibility(column)


def detect_from_down(rows, i):
    column = get_column_from_down(rows, i)
    return check_visibility(column)


def detect_from_left(rows, i):
    row = get_row_from_left(rows, i)
    return check_visibility(row)


def detect_from_right(rows, i):
    row = get_row_from_right(rows, i)
    return check_visibility(row)


# for i in range(1, a - 1):
#     print(f"{i=} --> {detect_from_up(rows, i)=}")
#     print(f"{i=} --> {detect_from_right(rows, i)=}")
#     print(f"{i=} --> {detect_from_down(rows, i)=}")
#     print(f"{i=} --> {detect_from_left(rows, i)=}")

# nb_edges = 4 * a - 3
nb_edge_trees = 4 * (a - 1)

# for i in range(a):
#     print(f"{i=} --> {get_column_from_up(rows, i)=}")

# for i in range(a):
#     print(f"{i=} --> {get_column_from_down(rows, i)=}")

detected_trees = set()

for i in range(a):
    detected_trees.add((i, 0))
    detected_trees.add((i, a - 1))
    detected_trees.add((0, i))
    detected_trees.add((a - 1, i))
print(f"nb of edge trees : {len(detected_trees)}")

for i in range(a):
    up_visibility, rank = detect_from_up(rows, i)
    if up_visibility >= 1:
        col, row = i, rank
        detected_trees.add((col, row))

    right_visibility, rank = detect_from_right(rows, i)
    if right_visibility >= 1:
        col, row = a - 1 - rank, i
        detected_trees.add((col, row))

    down_visibility, rank = detect_from_down(rows, i)
    if down_visibility >= 1:
        col, row = i, a - 1 - rank
        detected_trees.add((col, row))

    left_visibility, rank = detect_from_left(rows, i)
    if left_visibility >= 1:
        col, row = rank, i
        detected_trees.add((col, row))

print(f"{detected_trees=}")

print(f"{len(detected_trees)=}")

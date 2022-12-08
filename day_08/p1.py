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

# for row in rows:
#     print(row)
# print(len(rows[0]))
# print(len(rows))



def is_visible(x, rest_of_trees, mini):
    if len(rest_of_trees) == 0:
        return x > mini
    else:
        return max(rest_of_trees) <= x and x > mini


def get_column_from_up(rows, i):
    return [row[i] for row in rows]


def get_column_from_down(rows, i):
    return list(reversed(get_column_from_up(rows, i)))


def get_row_from_left(rows, i):
    return rows[i]


def get_row_from_right(rows, i):
    return list(reversed(rows[i]))


def count(u, mini):
    nb = 0
    for i, x in enumerate(u):
        if is_visible(x, u[i + 1 :], mini):
            nb += 1
            break
    return nb


def count_from_up(rows, i):
    column = get_column_from_up(rows, i)
    return count(column, column[0])


def count_from_down(rows, i):
    column = get_column_from_down(rows, i)
    return count(column, column[0])


def count_from_left(rows, i):
    row = get_row_from_left(rows, i)
    return count(row, row[0])


def count_from_right(rows, i):
    row = get_row_from_right(rows, i)
    return count(row, row[0])



a = len(rows)

for i in range(1, a-1):
    print(f"{i=} --> {count_from_up(rows, i)=}")
    print(f"{i=} --> {count_from_right(rows, i)=}")
    print(f"{i=} --> {count_from_down(rows, i)=}")
    print(f"{i=} --> {count_from_left(rows, i)=}")

# nb_edges = 4 * a - 3 
nb_edges = 4 * a - 3 - 4

# for i in range(a):
#     print(f"{i=} --> {get_column_from_up(rows, i)=}")

# for i in range(a):
#     print(f"{i=} --> {get_column_from_down(rows, i)=}")

total = 0
for i in range(1, a-1):
    total += count_from_up(rows, i)
    total += count_from_right(rows, i)
    total += count_from_down(rows, i)
    total += count_from_left(rows, i)

total += nb_edges

print(total)
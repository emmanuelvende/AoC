import sys


with open(sys.argv[1], "r") as f:
    input_ = f.read()


MAP = input_.split("\n")
# print(the_map)
H = len(MAP)
W = len(MAP[0])
print(f"{H=}, {W=}")

# All positions in map are (r, c)


def find_char(char):
    for r, row in enumerate(MAP):
        c = row.find(char)
        if c != -1:
            break
    return r, c


S = find_char("S")
E = find_char("E")

print(f"{S=} {E=}")

# DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1), ".": (0, 0)}
DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def altitude(pos):
    return ord(MAP[pos[0]][pos[1]])


def move(pos_, mov):
    return tuple(pos_[i] + mov[i] for i in range(2))


def is_in_map(pos_):
    return 0 <= pos_[0] < H and 0 <= pos_[1] < W


# print(f"{is_in_map((0, 0))=}")


def can_go(pos_, dir_):
    """dir_ and pos are (x, y)"""
    new_pos = move(pos_, dir_)
    can_go = is_in_map(new_pos) and (
        (altitude(new_pos) - altitude(pos_) <= 1) or (new_pos == E)
    )
    return can_go


# for dir_s, dir_ in DIRS.items():
#     print(f"{dir_s=} ", end="")
#     print(f"{can_go((0, 0), dir_)=}")


move_choices = []
positions = []
end_reached = False
pos = S
positions.append(pos)

blocked = False
while not end_reached and not blocked:
    moving = False
    for move_choice, dir_ in DIRS.items():
        if can_go(pos, dir_):
            pos = move(pos, dir_)
            positions.append(pos)
            move_choices.append(move_choice)
            moving = True
            break
        end_reached = pos == E
        blocked = not moving
success = end_reached
print(success, move_choices, positions)

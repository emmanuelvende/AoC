def fact(n):
    x = 1 if n == 0 else n * fact(n-1)
    return x

print(fact(50))


E = (20, 30)

directions = []

def can_move(pos_, direction_):
    return False

def move(pos_, direction_):
    return pos_

positions = []
moves = []

def explore(pos):
    state = "unknown"
    positions.append(pos)
    if pos == E:
        state = "success"
    else:
        for direction in directions:
            if can_move(pos, direction):
                moves.append(direction)
                new_pos = move(pos, direction)
                if new_pos not in self.positions:
                    explore(new_pos)
            if len(moves) == 0:
                state = "blocked"

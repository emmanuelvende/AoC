import sys

PRINT = 1

def print_(x, end="\n"):
    if PRINT:
        print(x, end=end)


def is_right_order(u_, v_):
    U, V = len(u_), len(v_)
    return False



with open(sys.argv[1], "r") as f:
    input_ = f.read()

pairs = input_.split("\n\n")
analysis_results = []     # list of (u, v, bool)

for pair in pairs:
    u, v = pair.split("\n")
    u, v = eval(u), eval(v)
    print_(f"{u=}, {v=}")
    analysis_results.append((u, v, is_right_order(u, v)))

indices_sum = 0
for i, r in enumerate(analysis_results):
    indices_sum += i if r[2] else 0

print(indices_sum)
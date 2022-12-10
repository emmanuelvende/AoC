import sys


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
lines[-1] += "\n"

NTH_TIMES_TO_CONSIDER = [20, 60, 100, 140, 180, 220]


class Device:
    def __init__(self):
        self.time = 0
        self.signal_strength = 0

    def tick(self, x):
        self.time += 1
        if self.time in NTH_TIMES_TO_CONSIDER:
            self.signal_strength += self.time * x


device = Device()
x = 1

for line in lines:
    args = line[:-1].split()
    if len(args) == 1:
        op = args[0]
    else:
        op, val = args
    if op == "noop":
        device.tick(x)
    elif op == "addx":
        device.tick(x)
        device.tick(x)
        x += int(val)

print(device.signal_strength)

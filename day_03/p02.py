def compute_priority(letter):
    if letter.upper() == letter:
        return ord(letter) - 38
    else:
        return ord(letter) - 96


with open("input.txt", "r") as f:
    lines = f.readlines()

lists_of_3_lines = []
index = 0
list_of_3_lines = []
for line in lines:
    list_of_3_lines.append(line)
    index += 1
    if index == 3:
        lists_of_3_lines.append(list_of_3_lines)
        list_of_3_lines = []
        index = 0


def find_badge(line_a, line_b, line_c):
    item = ""
    for x in line_a:
        if (x in line_b) and (x in line_c):
            item = x
            break
    return item


total = 0
for list_of_3_lines in lists_of_3_lines:
    badge = find_badge(*list_of_3_lines)
    score = compute_priority(badge)
    total += score

print(total)

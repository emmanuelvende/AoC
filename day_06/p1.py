import itertools

with open("input.txt", "r") as f:
    text = f.read()

def test_all_diff(u):
    """
    u = (a, b, c, d)
    """
    success = True
    for pair in itertools.combinations(u, 2):
        success = success and (pair[0] != pair[1])
    return success



def test_on_text(text):
    for i, x in enumerate(text):
        if i >= 4:
            a = x
            b = text[i - 1]
            c = text[i - 2]
            d = text[i - 3]
            if test_all_diff((a, b, c, d)):
                answer = i + 1
                break
    return answer



print(test_on_text("bvwbjplbgvbhsrlpgdmjqwftvncz"))
print(test_on_text("nppdvjthqldpwncqszvftbrmjlhg"))
print(test_on_text("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print(test_on_text("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
print(test_on_text(text))
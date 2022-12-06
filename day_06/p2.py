import itertools

with open("input.txt", "r") as f:
    text = f.read()

# print(text)


def test_all_diff(u):
    """
    u : iterable
    """
    success = True
    for pair in itertools.combinations(u, 2):
        success = success and (pair[0] != pair[1])
    return success



def test_on_text(text):
    for i, x in enumerate(text):
        if i >= 14:
            chars = [text[i-k] for k in range(14)]
            if test_all_diff(chars):
                answer = i + 1
                break
    return answer



# print(test_on_text("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
# print(test_on_text("bvwbjplbgvbhsrlpgdmjqwftvncz"))
# print(test_on_text("nppdvjthqldpwncqszvftbrmjlhg"))
# print(test_on_text("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
# print(test_on_text("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
print(test_on_text(text))
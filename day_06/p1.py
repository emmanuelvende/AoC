import itertools

with open("input.txt", "r") as f:
    text = f.read()


def test_that_all_char_are_different(u):
    """
    u = (a, b, c, d)
    """
    success = True
    for pair in itertools.combinations(u, 2):
        success = success and (pair[0] != pair[1])
    return success


def find_1st_serie_of_different_chars_in_text(text):
    for i, x in enumerate(text):
        if i >= 4:
            a = x
            b = text[i - 1]
            c = text[i - 2]
            d = text[i - 3]
            if test_that_all_char_are_different((a, b, c, d)):
                answer = i + 1
                break
    return answer

# print(find_1st_serie_of_different_chars_in_text("bvwbjplbgvbhsrlpgdmjqwftvncz"))
# print(find_1st_serie_of_different_chars_in_text("nppdvjthqldpwncqszvftbrmjlhg"))
# print(find_1st_serie_of_different_chars_in_text("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
# print(find_1st_serie_of_different_chars_in_text("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
print(find_1st_serie_of_different_chars_in_text(text))

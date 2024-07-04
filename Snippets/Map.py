words = ["boat", "tree", "game", "color"]


def add_s(string):
    return string + "s"


# plurals = map(lambda x: x + "s", words)
plurals = map(add_s, words)


print(list(plurals))

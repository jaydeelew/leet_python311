def args(*args):
    for value in args:
        print(f"The arg is: {value}")


def key_word_args(**kwargs):
    for key, value in kwargs.items():
        print("The value of key {} is {}".format(key, value))


args("alpha", "beta", "delta")
key_word_args(a="alpha", b="beta", c="delta")

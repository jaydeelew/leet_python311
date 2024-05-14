# this way of passing arguments is called positional arguments
def args(*args):
    for value in args:
        print(f"The arg is: {value}")


# this way of passing arguments is called keyword arguments (or named arguments)
def key_word_args(**kwargs):
    for keyword, value in kwargs.items():
        print("The value of keyword {} is {}".format(keyword, value))


x = 2
args("alpha", "beta", "delta")
key_word_args(a="alpha", b="beta", c="delta")

# this way of passing arguments is called positional arguments
def args(*args):
    # for value in args:
    #     print("The arg is", value)
    print(args[1])


# this way of passing arguments is called keyword arguments (or named arguments)
def key_word_args(**kwargs):
    # for keyword, value in kwargs.items():
    #     print("The value of keyword", keyword, "is", value)
    print(kwargs["b"])


args("alpha", "beta", "delta")
key_word_args(a="alpha", b="beta", c="delta")

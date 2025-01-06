# 0. Decorators
# A decorator is a function that takes another function as input and extends its behavior
# without explicitly modifying the original function's code
def myDecorator(func):
    # wrapper() is a closure that adds functionality around the original function
    def wrapper():
        # Prints the name of the function being executed
        print(f"Running {func.__name__}")
        # Calls the original function
        func()
        # Prints after the function is done
        print("Complete")

    return wrapper


# The @myDecorator syntax is equivalent to: doThis = myDecorator(doThis)
@myDecorator
def doThis():
    print("Doing this")


# Same decoration pattern applied to doThat
@myDecorator
def doThat():
    print("Doing that")


# When these functions are called, they actually run the wrapper function
# which includes the extra logging behavior
doThis()
doThat()

def try_except(a, b):
    try:
        quotient = a / b
        # quotient = a.div(b)
        # quotient = a / c
        print(quotient)
        return quotient
    except ZeroDivisionError:
        print("Make sure no divisions by 0 are made.")
        return None
    except NameError:
        print("Make sure both numbers are defined.")
        return None
    except TypeError:
        print("Make sure both numbers are of the same type.")
        return None
    except Exception as e:
        print(e)
        return None
    finally:
        print("This is always executed.")
        return 7.0


try_except(10, 2)
try_except(10, 0)
try_except(10, "a")

# finally overrides return value
# print(try_except(10, 2))

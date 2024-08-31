# recursively return fib(n)
def fib1(n):

    return n if n < 2 else fib1(n - 1) + fib1(n - 2)

    # Time complexity: O(2^n)
    # - Each call to fib1 makes two recursive calls, resulting in an exponential number of calls.
    # - The recursive tree will have a depth of n, and each level i has 2^i nodes.
    # - The total number of nodes in the tree is approximately 2^(n+1) - 1, which is O(2^n).
    #
    # Space complexity: O(n)
    # - The space is consumed by the recursive call stack.
    # - In the worst case, the recursive call stack will have a depth of n, resulting in O(n) space.
    # - Note that the space used by the recursive call stack is separate from any space used by the input or output.


# recursively return fib(n) with memoization
def fib2(n, memo={0: 0, 1: 1}):

    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)

    return memo[n]

    # Time complexity: O(n)
    # - Each number from 0 to n is calculated only once due to memoization.
    # - There will be at most n+1 recursive calls, resulting in O(n) time complexity.
    #
    # Space complexity: O(n)
    # - The space is consumed by the recursive call stack and the memoization dictionary.
    # - In the worst case, the recursive call stack will have a depth of n, resulting in O(n) space.
    # - The memoization dictionary will also store at most n+1 key-value pairs, resulting in O(n) space.
    # - Therefore, the overall space complexity is O(n).


# iteratively return fib(n)
def fib3(n):
    if n < 2:
        return n

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

    # Time complexity: O(n)
    # - The function uses a single loop that iterates from 2 to n, resulting in O(n) iterations.
    # - Each iteration performs constant-time operations, so the overall time complexity is O(n).
    #
    # Space complexity: O(1)
    # - The function uses only a constant amount of extra space for the variables prev and curr.
    # - The space used does not depend on the input size n, so the space complexity is O(1).


# recursively return fibonacci values up through fib(n)
def fib4(n):

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_list = fib4(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

    # Time complexity: O(2^n)
    # - The function makes two recursive calls for each value of n greater than 1.
    # - This results in a recursive tree with a depth of n and approximately 2^n nodes.
    # - Each node in the tree represents a constant-time operation, so the overall time complexity is O(2^n).
    #
    # Space complexity: O(n)
    # - The space is consumed by the recursive call stack and the returned list.
    # - In the worst case, the recursive call stack will have a depth of n, resulting in O(n) space.
    # - The returned list will contain n+1 elements, also resulting in O(n) space.
    # - Therefore, the overall space complexity is O(n).


# recursively return fibonacci values up through fib(n) using a generator
def fib5(n):

    if n == 0:
        yield 0
    elif n == 1:
        yield 0
        yield 1
    else:
        fib_gen = fib5(n - 1)
        fib_list = list(fib_gen)
        fib_list.append(fib_list[-1] + fib_list[-2])

        for num in fib_list:
            yield num

    # Time complexity: O(2^n)
    # - The function makes two recursive calls for each value of n greater than 1.
    # - This results in a recursive tree with a depth of n and approximately 2^n nodes.
    # - Each node in the tree represents a constant-time operation, so the overall time complexity is O(2^n).
    #
    # Space complexity: O(n)
    # - The space is consumed by the recursive call stack and the generated list.
    # - In the worst case, the recursive call stack will have a depth of n, resulting in O(n) space.
    # - The generated list will contain n+1 elements, also resulting in O(n) space.
    # - Therefore, the overall space complexity is O(n).


# iteratively return fibonacci values up through fib(n)
def fib6(n):
    if n < 2:
        return [0] if n == 0 else [0, 1]
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list

    # Time complexity: O(n)
    # - The function iterates from 2 to n+1, performing constant-time operations in each iteration.
    # - The number of iterations is proportional to n, resulting in a linear time complexity.
    #
    # Space complexity: O(n)
    # - The function uses a list (fib_list) to store the Fibonacci numbers.
    # - The size of the list grows linearly with n, as it stores n+1 elements.
    # - Therefore, the space complexity is O(n).


# iteratively return fibonacci values up through fib(n)
def fib7(n):
    fib_list = []
    prev, curr = 0, 1
    for _ in range(n + 1):
        fib_list.append(prev)
        prev, curr = curr, prev + curr
    return fib_list

    # Time complexity: O(n)
    # - The function iterates from 0 to n+1, performing constant-time operations in each iteration.
    # - The number of iterations is proportional to n, resulting in a linear time complexity.
    #
    # Space complexity: O(n)
    # - The function uses a list (fib_list) to store the Fibonacci numbers.
    # - The size of the list grows linearly with n, as it stores n+1 elements.
    # - Therefore, the space complexity is O(n).


# iteratively return fibonacci values up through fib(n) using a generator
def fib8(n):
    prev, curr = 0, 1
    for _ in range(n + 1):
        yield prev
        prev, curr = curr, prev + curr

    # Time complexity: O(n)
    # - The function iterates from 0 to n+1, performing constant-time operations in each iteration.
    # - The number of iterations is proportional to n, resulting in a linear time complexity.
    #
    # Space complexity: O(1)
    # - The function uses a constant amount of extra space to store the variables prev and curr.
    # - It does not use any additional data structures that grow with the input size.
    # - The space used by the generator to keep track of its state is negligible.


n = 5


print(fib1(n))
print(fib2(n))
print(fib3(n))
print(list(fib4(n)))
print(list(fib5(n)))
print(fib6(n))
print(fib7(n))
print(list(fib8(n)))

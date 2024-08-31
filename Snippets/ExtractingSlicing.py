# extract column from 2D list
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column = [row[1] for row in data]
print(column)  # output: [2, 5, 8]

# replace a range of elements in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1:4] = [10, 20, 30]
print(numbers)  # output: [1, 10, 20, 30, 5, 6, 7, 8, 9]

# insert a list of elements in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[4:4] = [75, 76]
print(numbers)  # output: [1, 2, 3, 4, 75, 76, 5, 6, 7, 8, 9]

# remove a range of elements from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1:4] = []
print(numbers)  # output: [1, 5, 6, 7, 8, 9]

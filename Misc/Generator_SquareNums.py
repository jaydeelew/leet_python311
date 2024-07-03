def generator(n):
    for i in range(n):
        yield i**2


# for i in generator():
#     print(i, end=" ")

g = generator(9)
for i in g:
    print(i, end=" ")

print()

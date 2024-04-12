def generator():
    str = "string"
    for s in str:
        yield s


for i in generator():
    print(i, end=" ")

print()

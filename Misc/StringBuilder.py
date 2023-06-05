def string_builder(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)


s = "my string"
print(string_builder(s))

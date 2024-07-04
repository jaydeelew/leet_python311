def stringify(listOfCharacters):
    build_string = ""
    for c in listOfCharacters:
        build_string = build_string + c
    return build_string


sample = ["h", "e", "l", "l", "o"]
print(stringify(sample))

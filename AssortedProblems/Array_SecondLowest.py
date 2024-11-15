# Given the names and grades for each student in a class of students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically
# and print each name on a new line.

import bisect


def second_lowest(nested_list):
    lowest = min(x[1] for x in nested)
    sec_low = float("inf")
    names = []

    for sub in nested:
        if sub[1] == sec_low:
            bisect.insort(names, sub[0])
        elif sub[1] < sec_low and sub[1] > lowest:
            names.clear()
            names.append(sub[0])
            sec_low = sub[1]

    for name in names:
        print(name)


# nested = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
# Output:
# Berry
# Harry

nested = [["Prashant", 52.22], ["Kush", 52.223], ["Kant", 52.222], ["Kanti", 52.2222], ["Harshit", 52.22222]]
# Output:
# Kant

second_lowest(nested)

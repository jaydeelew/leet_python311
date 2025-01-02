# 0. Second Lowest
# Given the names and grades for each student in a class of students stored in a nested list,
# print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically
# and print each name on a new line.


def secondLowest(nested):

    # Work with a copy of the list to avoid modifying the input.
    # The list is sorted by the scores first, then the names.
    students = sorted(nested, key=lambda x: (x[1], x[0]))

    # Find the second lowest grade.
    scores = sorted(set(x[1] for x in students))
    if len(scores) < 2:
        return

    # By creating a set and thereby removing duplicates and sorting it,
    # we will have scores[1] be the second lowest score
    second_min = scores[1]

    # Print names of students with second lowest grade
    for name, score in nested:
        if score == second_min:
            print(name)


nested = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
# Output:
# Berry
# Harry

# nested = [["Prashant", 52.22], ["Kush", 52.223], ["Kant", 52.222], ["Kanti", 52.2222], ["Harshit", 52.22222]]
# Output:
# Kant

secondLowest(nested)

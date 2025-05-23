# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    buttons = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"],
    ]

    # use list comprehension to turn digits string into list of digits
    digits_list = [int(x) for x in digits]

    ans_list = []

    def backtrack(curr_path: list[str], digits_list_idx: int):
        if len(curr_path) == len(digits):
            ans_list.append("".join(curr_path))
            return

        # subtract 2 from element in digits list to translate from button to index in digits_list
        for ltr in buttons[digits_list[digits_list_idx] - 2]:
            curr_path.append(ltr)
            backtrack(curr_path, digits_list_idx + 1)
            curr_path.pop()

    backtrack([], 0)

    return ans_list


digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# digits = ""
# # # Output: []

# digits = "2"
# Output: ["a","b","c"]

print(letterCombinations(digits))

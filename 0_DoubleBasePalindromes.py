# 0. Double Base Paliindromes
# The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.
# Hence, we call 585 a double base palindrome number.
# Write a program to find the sum of all double base palindrome numbers
# which are less than a given number (starting from 1, including the given number).
# As an example, if the given number is 5, the double base palindromes less than or equal to 5
# are 1 (binary 1), 3 (binary 11), and 5 (binary 101). The sum is 1 + 3 + 5 = 9.
# Please note that the palindromic number, in either base, may not include leading zeros.


def doubleBasePalindromes(num: int) -> int:
    def isPalindrome(text: str) -> bool:
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1

        return True

    curr_sum = 0

    for i in range(1, num + 1):
        n = str(i)
        b = bin(i)[2:]

        if isPalindrome(n) and isPalindrome(b):
            curr_sum += i

    return curr_sum


print(doubleBasePalindromes(5))

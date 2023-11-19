import sys
import time

text = "Saved souls are thankful souls"


def slowPrint(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


slowPrint(text)

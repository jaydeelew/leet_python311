import time

from Formatting import color


def banner(msg: str):
    print("\033[?25l", end="")

    while True:
        try:
            for next in [color.RED, color.GREEN, ""]:
                for c in msg:
                    print(next + c + color.END, end="", flush=True)
                    time.sleep(0.04)
                print("", end="\r")
        except KeyboardInterrupt:
            print("\033[?25h", end="")
            print("")
            break


def formatBinarySearch(arr, left, mid, right):
    print("[", end="")
    for i in range(len(arr)):
        if i == mid:
            if i == len(arr) - 1:
                print(color.GREEN + str(arr[i]) + color.END, end="")
            else:
                print(color.GREEN + str(arr[i]) + color.END, end=", ")
        elif i == left or i == right:
            if i == len(arr) - 1:
                print(color.RED + str(arr[i]) + color.END, end="")
            else:
                print(color.RED + str(arr[i]) + color.END, end=", ")
        elif i == len(arr) - 1:
            print(arr[i], end="")
        else:
            print(arr[i], end=", ")
    print("]")

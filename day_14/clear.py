import os


def clear():
    if "TERM" in os.environ:
        os.system("clear" if os.name != "nt" else "cls")
    else:
        print("\033[H\033[J", end="")

import os
import time

from getkey import getkey, keys

#
# Escape codes
#
BLACK: str = "30"
RED: str = "91"
GREEN: str = "92"
YELLOW: str = "93"
BLUE: str = "94"
MAGENTA: str = "95"
CYAN: str = "96"
WHITE: str = "97"
RESET: str = "0"

#
# Block dimension
#
ROW: int = 6
COL: int = 12


def e(code: str) -> str:
    return f'\033[{code}m'


def up(row: int = ROW) -> str:
    return "\033[F" * (row + 2)


def print_frame() -> None:
    os.system("clear")
    print(f"┌{'─' * (COL + 2)}┐")
    for i in range(ROW):
        print(f"│{' ' * (COL + 2)}│")
    print(f"└{'─' * (COL + 2)}┘")


def print_block(color: str = WHITE, clear: bool = False) -> None:
    print(f"{up()}{e(color)}")
    for i in range(ROW):
        print(f"\033[C\033[C{(' ' if clear else '█') * COL}")
    print(f"{e(RESET)}")


def main():
    print_frame()

    sequence: list = [RED, GREEN, BLUE, YELLOW]

    for color in sequence:
        print_block(color)
        time.sleep(1)
    print_block(clear=True)

    #
    # Get the keyboard input and print the colored block
    #
    while True:
        key = getkey()

        if key == 'q':
            print_block(clear=True)
            break
        elif key == 'r':
            print_block(RED)
        elif key == 'g':
            print_block(GREEN)
        elif key == 'b':
            print_block(BLUE)
        elif key == 'y':
            print_block(YELLOW)
        else:
            pass


#
# Everything starts here
#
if __name__ == '__main__':
    main()

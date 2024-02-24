import os
import random
import time
import json
from getkey import getkey, keys

from score import Scoreboard

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

COLORS: list = [RED, GREEN, YELLOW, BLUE,]

#
# Block dimension
#
ROW: int = 4
COL: int = 24


def clear():
    '''
    Clear the terminal
    '''
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')


class Game:

    def __init__(self) -> None:
        clear()
        self.player_name = input("Enter your name: ")
        clear()
        print(f"Hi {self.player_name} 👋🏻")
        self.sequence: list = []
        self.score: int = 0


    def e(self, code: str) -> str:
        """
        Returns an ANSI escape sequence to set the text color.
        Args:
            code: A string representing the ANSI escape code for the desired color.
        Return:
            The ANSI escape sequence as a string
        """
        return f'\033[{code}m'

    def up(self, row: int = ROW) -> str:
        """
        Returns an ANSI escape sequence to move the cursor up a specified number of rows.
        Args:
            row: An integer representing the number of rows to move the cursor up.
        Return:
            The ANSI escape sequence to move the cursor up.
        """
        if not row: row = ROW
        return "\033[F" * (row + 2)


    # Print the outside frame
    def print_frame(self) -> None:
        os.system("clear")
        print(f"┌{'─' * (COL + 2)}┐")
        for i in range(ROW):
            print(f"│{' ' * (COL + 2)}│")
        print(f"└{'─' * (COL + 2)}┘")

    # Print the colored block
    def print_block(self, color: str = WHITE, clear: bool = False) -> None:
        print(f"{self.up()}{self.e(color)}")
        for i in range(ROW):
            print(f"\033[C\033[C{(' ' if clear else '█') * COL}")
        print(f"{self.e(RESET)}")

    # Play the sequence of colors
    def play_sequence(self) -> None:
        self.print_frame()
        for color in self.sequence:
            self.print_block(color=color)
            time.sleep(0.8)
            self.print_block(clear=True)
            time.sleep(0.2)
        self.print_block(clear=True)

    # Add color to the sequence
    def add_color(self) -> None:
        self.sequence.append(random.choice(COLORS))

    # Check answer
    def check(self, answer: list) -> bool:
        if answer == self.sequence:
            self.score += 1
            return True
        else:
            return False


def main():
    game = Game()
    sb = Scoreboard(player_name=game.player_name)

    record = sb.get_score()

    if record: print(f"Current record -> {record}")
    time.sleep(1.5)
    clear()


    while True:
        game.add_color()
        game.play_sequence()

        answer: list = []
        for color in game.sequence:
            key = getkey()

            if key == 'q':
                game.print_block(clear=True)
                sb.update_record(game.score)
                break
            elif key == 'r':
                game.print_block(RED)
                answer.append(RED)
            elif key == 'g':
                game.print_block(GREEN)
                answer.append(GREEN)
            elif key == 'b':
                game.print_block(BLUE)
                answer.append(BLUE)
            elif key == 'y':
                game.print_block(YELLOW)
                answer.append(YELLOW)
            else:
                pass

        time.sleep(1)
        if game.check(answer):
            clear()
            print("Nice")
            time.sleep(0.8)
            clear()
        else:
            clear()
            sb.update_record(game.score)
            if game.score > int(record):
                print("Nice, you beat your record !")
                print(f"You scored {game.score} points")
            else:
                print("You lost :(")
                print(f"you lost you reached a score of {game.score} points")
                print(f"The record you have to beat is {record} points")
            break






if __name__ == "__main__":
    main()

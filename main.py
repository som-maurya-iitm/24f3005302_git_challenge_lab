from __future__ import annotations

import os

from add import add
from divide import divide
from multiply import multiply
from subtract import subtract
from sqaure import square
from power import power


def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


def greet() -> None:
    user_name = os.getlogin()
    print("""########## Calculator ##########""")
    print("#", f"Hello {user_name}! 👋".center(27), "#")
    print("#", " " * 28, "#")
    print("#", "*** Commands: ***", "#".rjust(12))
    print("#", f"\tQuit: {bold('q')}", "#".rjust(20))
    print("#", f"\tAdd: {bold('a')} x y", "#".rjust(17))
    print("#", f"\tSubtract: {bold('s')} x y", "#".rjust(12))
    print("#", f"\tMultiply: {bold('m')} x y", "#".rjust(12))
    print("#", f"\tDivide: {bold('d')} x y", "#".rjust(14))
    print("#", f"\tSquare: {bold('sqr')} x", "#".rjust(14))
    print("#", f"\tPower: {bold('p')} x y", "#".rjust(15))
    print("#" * 32)


def get_x_y(text: str) -> tuple[float, float]:
    s = text.strip().split()
    return float(s[1]), float(s[2])


def main() -> None:
    greet()
    while True:
        user_input = input("> ").casefold()
        if user_input == "q":
            break
        elif user_input.startswith("a "):
            print(bold(str(add(*get_x_y(user_input)))))
        elif user_input.startswith("s "):
            print(bold(str(subtract(*get_x_y(user_input)))))
        elif user_input.startswith("m "):
            print(bold(str(multiply(*get_x_y(user_input)))))
        elif user_input.startswith("d "):
            x, y = get_x_y(user_input)
            if y == 0:
                print("Cannot divide by zero")
                continue
            print(bold(str(divide(x, y))))
        elif user_input.startswith("sqr "):
            user_input += " 0"
            x, _ = get_x_y(user_input)
            print(bold(str(square(x))))
        elif user_input.startswith("p "):
            print(bold(str(power(*get_x_y(user_input)))))
        else:
            print("Unknown Command!")


if __name__ == "__main__":
    main()

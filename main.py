from __future__ import annotations

import os

from add import add
from subtract import subtract


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
        else:
            print("Unknown Command!")


if __name__ == "__main__":
    main()

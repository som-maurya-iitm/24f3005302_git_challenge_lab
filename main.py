import os


def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


def greet() -> None:
    user_name = os.getlogin()
    print("""########## Calculator ##########""")
    print("#", f"Hello {user_name}! 👋".center(27), "#")
    print("#", " "*28, "#")
    print("#", "*** Commands: ***", "#".rjust(12))
    print("#", f"\tQuit: {bold('q')}", "#".rjust(20))
    print("#" * 32)


def main() -> None:
    greet()
    while True:
        user_input = input("> ")
        if user_input == "q":
            break
        else:
            print("Unknown Command!")



if __name__ == "__main__":
    main()

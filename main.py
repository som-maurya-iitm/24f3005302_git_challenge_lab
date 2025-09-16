import os


def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


def greet() -> None:
    user_name = os.getlogin()
    print("""########## Calculator ##########""")
    print("#", f"Hello {user_name}! 👋".center(27), "#")
    print("#" * 32)


def main() -> None:
    greet()


if __name__ == "__main__":
    main()

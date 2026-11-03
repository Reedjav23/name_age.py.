
from datetime import date


def main() -> None:
    """Run the name-age program."""
    name = input("What is your name: ")
    age = int(input("How old are you: "))

    current_year = date.today().year
    birth_year = current_year - age

    print(f"\nHello {name}! You were born in {birth_year}.")


if __name__ == "__main__":
    main()

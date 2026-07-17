def get_number(prompt: str) -> float:
    """Prompt the user until they enter a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def show_menu() -> None:
    """Display the calculator options."""
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main() -> None:
    """Run the calculator loop."""
    print("Welcome to the Python Calculator!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5" or choice.lower() == "exit" or choice.lower() == "q":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")


if __name__ == "__main__":
    main()

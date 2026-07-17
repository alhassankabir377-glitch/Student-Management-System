
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

        if choice in {"1", "2", "3", "4"}:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

        if choice == "1":
            def add(a, b):
                return a + b
            result = add(num1,num2)
            print(f"The result is: {result}")
        elif choice == "2":
            def subtract(a, b):
                return a - b
            result = subtract(num1, num2)
            print(f"The result is: {result}")
        elif choice == "3":
            def multiply(a, b):
                return a * b
            result = multiply(num1, num2)
            print(f"The result is: {result}")
        elif choice == "4":
            def divide(a, b):
                if b == 0:
                    return None
                return a / b
            if num2 != 0:
                result = divide(num1, num2)
                print(f"The result is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == "5":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid option. Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()

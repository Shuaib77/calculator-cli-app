def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("    COMMAND LINE CALCULATOR")
    print("="*50)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("="*50)

def get_numbers():
    """Get two numbers from user input with error handling"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    """Main function to run the calculator"""
    print("Welcome to the Command Line Calculator!")

    while True:
        display_menu()

        try:
            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '5':
                print("\nThank you for using the calculator!")
                print("Goodbye! 👋")
                break

            if choice in ['1', '2', '3', '4']:
                num1, num2 = get_numbers()

                if num1 is None or num2 is None:
                    continue

                if choice == '1':
                    result = add(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = "/"

                print(f"\nResult: {num1} {operation} {num2} = {result}")

                # Ask if user wants to continue
                continue_calc = input("\nDo you want to perform another calculation? (y/n): ")
                if continue_calc.lower() != 'y':
                    print("\nThank you for using the calculator!")
                    print("Goodbye! 👋")
                    break
            else:
                print("Error: Invalid input! Please select a valid option (1-5).")

        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user.")
            print("Goodbye! 👋")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()

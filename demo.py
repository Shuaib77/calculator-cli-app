
Purpose: Provides a quick way to see the calculator's functionality without needing manual user input.

Details:

Demonstrates each calculator operation (add, subtract, multiply, divide) with preset values.

Includes division by zero to show error handling.

Useful for reviewers to confirm logic without interactive use.

Sample Content:
def demo_calculator():
    print("Demo Calculations:")
    print("15 + 25 =", 15 + 25)
    print("50 - 20 =", 50 - 20)
    print("8 * 6 =", 8 * 6)
    print("100 / 4 =", 100 / 4)
    print("10 / 0 =", "Error: Division by zero is not allowed!")
if __name__ == "__main__":
    demo_calculator()

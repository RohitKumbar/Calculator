# display.py

def show_welcome_message():
    print("Welcome to the Simple Calculator!")
    print("---------------------------------")

def show_menu():
    print("\nPlease choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("---------------------------------")

def show_result(operation_name, num1, num2, result):
    print(f"\nResult of {operation_name} {num1} and {num2}: {result}")

def show_error(message):
    print(f"\nError: {message}")

def show_goodbye_message():
    print("\nThank you for using the Simple Calculator. Goodbye!")
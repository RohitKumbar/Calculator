# main.py

from operations import add, subtract, multiply, divide
from display import show_welcome_message, show_menu, show_result, show_error, show_goodbye_message

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            show_error("Invalid input. Please enter numbers only.")

def main():
    show_welcome_message()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            show_goodbye_message()
            break
        elif choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()

            if choice == '1':
                result = add(num1, num2)
                show_result("addition of", num1, num2, result)
            elif choice == '2':
                result = subtract(num1, num2)
                show_result("subtraction of", num1, num2, result)
            elif choice == '3':
                result = multiply(num1, num2)
                show_result("multiplication of", num1, num2, result)
            elif choice == '4':
                result = divide(num1, num2)
                show_result("division of", num1, num2, result)
        else:
            show_error("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
import os
os.system('cls' if os.name =='nt' else 'clear')

def menu():
    print("=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def two_numbers():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        a, b = two_numbers()
        print("Result:", a + b)
    elif choice == '2':
        a, b = two_numbers()
        print("Result:", a - b)
    elif choice == '3':
        a, b = two_numbers()
        print("Result:", a * b)
    elif choice == '4':
        a, b = two_numbers()
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", a / b)
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
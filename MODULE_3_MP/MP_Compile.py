import os
import random

def Calculator():
    os.system('cls' if os.name == 'nt' else 'clear')

    def two_numbers():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2

    while True:
        print("\n=== Calculator Menu 🔢 ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
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
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice.")

def Temperature():
    os.system('cls' if os.name == 'nt' else 'clear')

    def TemperatureConverter(x):
        while True:
            print("\n=== Python Temperature Converter ===")
            print("1. Convert Celsius to Fahrenheit")
            print("2. Convert Fahrenheit to Celsius")
            print("3. Exit to Main Menu")

            choice = input("Enter your operation: ")
            if choice == '1':
                fahrenheit = (9 / 5) * x + 32
                print(f"{x}°C = {fahrenheit:.2f}°F")
            elif choice == '2':
                celsius = (5 / 9) * (x - 32)
                print(f"{x}°F = {celsius:.2f}°C")
            elif choice == '3':
                break
            else:
                print("Invalid choice.")

    while True:
        try:
            x = float(input("Enter a temperature value: "))
            TemperatureConverter(x)
        except ValueError:
            print("Invalid number.")
        again = input("Try again? (1 for yes / 0 for no): ")
        if again != '1':
            break

def To_Do():
    os.system('cls' if os.name == 'nt' else 'clear')
    tasks = []

    while True:
        print("\n=== To-Do List Menu 📝 ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("Tasks:")
            for task in tasks:
                print("-", task)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def Number_Guess():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("\n=== Number Guessing Game 🎮 ===")
        print("1. Play")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            number = random.randint(1, 100)
            attempts = 0
            while True:
                guess = input("Guess the number (1-100): ")
                if not guess.isdigit():
                    print("Enter a valid number.")
                    continue
                guess = int(guess)
                attempts += 1
                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"You guessed it in {attempts} tries!")
                    break
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

def Student_Grade():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    total_score = 0
    score_count = 0
    grades = []

    def menu():
        print("\n=== Student Grade Calculator 🎓 ===")
        print("1. Add Score")
        print("2. View All Scores and the Calculated General Average")
        print("3. Exit")

    while True:
        menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            subject = input("Enter the subject: ")
            score = input("Enter the score: ")

            if score == "":
                print("Score cannot be empty.")
            else:
                score = float(score)
                total_score += score
                score_count += 1
                grades.append((subject, score))
                print("Score added.")

        elif choice == "2":
            print("\nFinal List of Subjects and Scores with the General Average Calculated:")
            for subject, score in grades:
                print(f"- {subject}: {score}")
            if score_count > 0:
                average = total_score / score_count
                print("\nYour General Average Grade is:", round(average, 2))

        elif choice == "3":
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========")
        print("MAIN MENU")
        print("==========")
        print("1. Simple Calculator")
        print("2. Temperature Converter")
        print("3. To-Do List")
        print("4. Number Guessing Game")
        print("5. Student Grade Calculator")
        print("6. Exit")

        choice = input("Select your program (1-6): ")

        if choice == '1':
            Calculator()
        elif choice == '2':
            Temperature()
        elif choice == '3':
            To_Do()
        elif choice == '4':
            Number_Guess()
        elif choice == '5':
            Student_Grade()
        elif choice == '6':
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1–6.")
            input("Press Enter to continue...")

main()
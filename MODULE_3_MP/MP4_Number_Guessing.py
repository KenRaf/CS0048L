import random
import os
os.system('cls' if os.name =='nt' else 'clear')

def menu():
    print("=== Guessing Game ===")
    print("1. Play Number Guessing Game")
    print("2. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = input("Guess the number (1-100): ")
            if guess == "":
                print("Please enter a number.")
            else:
                guess = int(guess)
                attempts = attempts + 1

                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1 or 2.")
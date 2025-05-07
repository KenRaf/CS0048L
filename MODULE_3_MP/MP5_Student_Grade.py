import os
os.system('cls' if os.name =='nt' else 'clear')

total_score = 0
score_count = 0
grades = []

def menu():
    print("=== Student Grade Calculator ===")
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
        
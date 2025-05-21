# Membership operator = used to check whether a value or variable is found in a sequence
# str, list, tuple, set, dict
# 1. in
# 2. not in

def word_guessing_game(word="hello"):
    playing = True

    while playing:
        letter = input("Guess a letter in the secret word: ")

        if letter in word:
            count = word.count(letter)
            if count == 1:
                print(f"There is {count} {letter}")
            else:
                print(f"There are {count} {letter}")
        else:
            print(f"{letter} not found")

        if not input("Continue? (Y/N): ").upper() == "Y":
            break

    print("Thanks for playing!")


# word_guessing_game("secret")

def search_student_grade():
    grades = {
        "Alice": "C",
        "Bob": "A",
        "Charlie": "D",
        "Danny": "B"
    }

    student = input("Enter student name: ")

    if student in grades:
        print(f"{student}: {grades.get(student)}")
    else:
        print(f"{student} not found")


search_student_grade()

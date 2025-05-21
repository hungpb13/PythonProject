# Exercise: Quiz Game

questions = ("What is the capital of France?",
             "Which language is used to build web apps?",
             "What does CPU stand for?",
             "Who developed Python?")

options = (
    ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. Python", "B. C", "C. Java", "D. All of above"),
    ("A. Central Plug Unit", "B. Control Power Unit", "C. Central Processing Unit", "D. Compute Program Unit"),
    ("A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Tim Berners-Lee")
)

answers = ("C", "D", "C", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Choose (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print(f"INCORRECT! {answers[question_num]} is the correct answer!")

    question_num += 1

print("--------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

print("--------------------")

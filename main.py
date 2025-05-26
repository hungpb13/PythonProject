# Writing files (.txt, .json, .csv)
import csv
import json

txt_data = "I like pizza!\n"

students = ["Alice", "Bob", "Charles", "Dutch"]

txt_file = "resources/output.txt"

# Mode
# w = overite
# a = append
# x = exclusive creation (try except FileExistsError)
# r = read (default)
try:
    # with statement = automatic file closing
    with open(file=txt_file, mode="w") as file:
        file.write(txt_data)

        # Write a list
        file.write("Students: ")
        for student in students:
            file.write(student + " ")
        print(f"Text file {txt_file} was created")
except FileExistsError:
    print("That file already exists")

# Write JSON file
student = {
    "name": "Alice",
    "age": 20,
    "email": "alice@gmail.com",
    "gpa": 3.5
}

json_file = "resources/output.json"

try:
    with open(json_file, "w") as file:
        json.dump(student, file, indent=4)
        print(f"JSON file '{json_file}' was created")
except FileExistsError:
    print("That file already exists")

# Write CSV file
data = [
    ["Name", "Age", "Email"],  # Header row
    ["Alice", 25, "alice@example.com"],
    ["Bob", 30, "bob@example.com"],
    ["Charlie", 28, "charlie@example.com"]
]

csv_file = "resources/output.csv"

try:
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)

        print(f"CSV file '{csv_file}' was created")
except FileExistsError:
    print("That file already exists")

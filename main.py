# Writing a List of Dictionaries

import csv

data = [
    {"Name": "Alice", "Age": 25, "Email": "alice@example.com"},
    {"Name": "Bob", "Age": 30, "Email": "bob@example.com"}
]
dict_csv_file = "resources/dict.csv"

with open(dict_csv_file, "w", newline="") as file:
    fieldnames = ["Name", "Age", "Email"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Writes the header row
    writer.writerows(data)

# Read files (.txt, .json, .csv)
import csv
import json

txt_file = "resources/input.txt"

try:
    with open(txt_file, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Do not have permission to read")

# JSON file
json_file = "resources/input.json"

try:
    with open(json_file, "r") as file:
        content = json.load(file)
        print(content)

        # Content = dict
        # print(content["name"])
        # for key, value in content.items():
        #     print(f"{key}: {value}")

        # Content = list
        for item in content:
            print(item)
            for key, value in item.items():
                print(f"{key}: {value}")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Do not have permission to read")
except json.decoder.JSONDecodeError:
    print("Invalid JSON format")

# CSV file
csv_file = "resources/input.csv"

try:
    with open(csv_file, "r") as file:
        # reader = csv.reader(file)
        # print(reader)

        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        print(fieldnames)
        for row in reader:
            for i in range(len(fieldnames)):
                fieldname = fieldnames[i]
                print(f"{fieldname}: {row[fieldname]}", end=" ")
            print()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Do not have permission to read")

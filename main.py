# String Methods

name = "bro Code"
number = "2"
phone_number = "1-234-567-8901"

print(f"Length: {len(name)}")
print(f"First index of: {name.find(" ")}") # return -1 if not found
print(f"Last index of: {name.rfind("o")}")
print(f"Capitalize the first character: {name.capitalize()}")
print(f"Capitalize each word: {name.title()}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Is digit: {number.isdigit()}")
print(f"Is alpha: {"name".isalpha()}")
print(f"Is alpha and number: {"Bro123".isalnum()}")
print(f"Count: {phone_number.count("-")}")
print(f"Replace: {phone_number.replace("-", " ")}")

split_numbers = phone_number.split("-")
print(f"Numbers: {split_numbers}")
print(f"Join numbers: {"-".join(split_numbers)}")
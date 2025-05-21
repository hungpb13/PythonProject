# Keyword argument = an argument preceded by an identifier
# Help with readability
# Order of keyword arguments doesn't matter
# Argument: Positional --> Default --> KEYWORD --> Arbitrary

def hello(greeting, title, first, last):
    return f"{greeting} {title}{first} {last}"


print(hello(greeting="Hi", title="Mr.", last="Bro", first="Code"))

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country=1, area=123, first=456, last=7890)
print(phone_number)

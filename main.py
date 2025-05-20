# Variable = a container for a value (string, integer, float, boolean)

# String
first_name = "Bro"
food = "pizza"
email = "bro123@gmail.com"
print(f"Type: {type(email)}")
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integer
age = 25
quantity = 3
num_of_students = 30
print(f"Type: {type(age)}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} student(s)")

# Float
price = 10.99
gpa = 3.2
distance = 5.5
print(f"Type: {type(price)}")
print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

# Boolean = True of False
# is_student = False
is_student = True
print(f"Type: {type(is_student)}")
print(f"Are you a student?: {is_student}")

# Use in if statement
if is_student:
    print("You are a student")
else:
    print("You are NOT a student")
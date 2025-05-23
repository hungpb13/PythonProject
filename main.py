# filter(function, collection) = return all elements that pass a condition

def is_passing(grade):
    return grade >= 50


grades = [63, 45, 23, 85, 99, 74, 56, 88]

# pass_grades = filter(is_passing, grades)

# Lambda
pass_grades = list(filter(lambda grade: grade >= 50, grades))

print(grades)

for grade in pass_grades:
    print(grade)

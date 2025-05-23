# Class method = allows operations related to the Class itself
# @classmethod
# def method_name(cls):
# cls --> first parameter represents the class itself

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} - {self.gpa}"

    # Class method
    @classmethod
    def get_count(cls):
        return f"Total number of students = {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            average_gpa = cls.total_gpa / cls.count
            return f"Average GPA = {average_gpa:.2f}"


alice = Student("Alice", 3.4)
bob = Student("Bob", 2.3)
charles = Student("Charles", 3.2)

print(Student.get_count())
print(Student.get_average_gpa())

# Static method = a method that belongs to a class rather than any object from that class (instance)
# Usually used for general utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ("Manager", "Cook", "Cashier", "Staff")
        return position in valid_positions


def main():
    employees = []

    while True:
        name = input("Enter employee name: ").capitalize()
        position = input("Enter position: ").capitalize()

        if Employee.is_valid_position(position):
            employee = Employee(name, position)
            employees.append(employee)
        else:
            print("Invalid position!")
            continue

        print("List of employees:")
        for employee in employees:
            print(employee.get_info())

        if input("Add more employees? (press Q to quit) ").upper() == "Q":
            break


if __name__ == "__main__":
    main()

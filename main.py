# Nested class = a class defined within another class

# class Outer:
#   class Inner:
# Benefits:
# 1. Logically group classes that are closely related
# 2. Encapsulate private details that aren't relevant outside the outer class
# 3. Keep namespace clean --> reduce the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} - {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details()
                for employee in self.employees]


company = Company("KFC")
company.add_employee("Alice", "Manager")
company.add_employee("Bob", "Cook")
company.add_employee("Charles", "Cashier")

print(company.company_name)
print(company.list_employees())

for employee in company.list_employees():
    print(employee)

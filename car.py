class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive a {self.color} {self.year} {self.model}")

    def stop(self):
        print(f"You stop a {self.color} {self.year} {self.model}")
# Composition = the composed object directly owns its components, which cannot exist independently
# "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, maker, model, horse_power, wheel_size):
        self.maker = maker
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display(self):
        return f"{self.maker} {self.model} with {self.engine.horse_power}(hp) engine and {self.wheels[0].size}(in) wheels"


car = Car(maker="Ford", model="Mustang", horse_power=500, wheel_size=18)
print(car.display())

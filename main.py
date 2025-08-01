class Car:
    def __init__(self, model, color, horse_p, wheel_s):
        self.model = model
        self.color = color
        self.wheels = [Wheel(19) for _ in range(4)]
        self.engine = Engine(500)

    def __str__(self):
        return f'This car is a {self.color} {self.model}, which has {len(self.wheels)}, {self.wheels[0].wheel_size}in wheels, and has an engine with {self.engine.horse_power} HP.'

        

class Wheel:
    def __init__(self, wheel_s):
        self.wheel_size = wheel_s

    def print_size(self):
        print(f"My wheel size is {self.wheel_size}in.")


class Engine:
    def __init__(self, horse_p):
        self.horse_power = horse_p

    def print_hp(self):
        print(f"Vroom! My horsepower is {self.horse_power}")

my_car = Car("Ford Focus", "Red", "900", 19)

print(my_car)


        


class Car:
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

    def __init__(self, model, color, horse_p, wheel_s):
        self.model = model
        self.color = color
        self.wheels = [Car.Wheel(wheel_s) for _ in range(4)]
        self.engine = Car.Engine(horse_p)

    def __str__(self):
        return f'This car is a {self.color} {self.model}, which has {len(self.wheels)}, {self.wheels[0].wheel_size}in wheels, and has an engine with {self.engine.horse_power} HP.'  

    @staticmethod
    def drive_car():
        print("Vroom! You drive the car.")

    @staticmethod
    def stop_car():
        print("You stopped the car.")

    @staticmethod
    def is_valid_wheel_number(num):
        if num < 3 or 4 < num:
            return print("Invalid number of wheels")
        
        return print("Valid number of wheels")


Car.drive_car()
Car.stop_car()

my_car = Car("Ford Focus", "Red", 900, 19)

print(my_car)


        


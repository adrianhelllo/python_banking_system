class Animal():
    is_alive = True

class Dog(Animal):
    def speak(self):
        print('Woof!')

class Cat(Animal):
    def speak(self):
        print('Meow!')

class Car():
    is_alive = False
    def speak(self):
        print("duda")

objects = [Dog(), Cat(), Car()]

for object in objects:
    if object.is_alive:
        object.speak()


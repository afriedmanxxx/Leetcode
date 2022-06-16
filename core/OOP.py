class Tuna:

    def __init__(self, x):
        self.energy = x
        print("Blblb")

    def swim(self):
        print("I am swimming")

    def get_energy(self):
        print(self.energy)

flipper = Tuna(12)
flipper.swim()
flipper.get_energy()

# inheritance
class Parent():

    def print_last_name(selfs):
        print("Roberts")

class Child(Parent):

    def print_first_name(self):
        print("Alex")
# we can ovveride parent method by creating the same method in child class
    def print_last_name(selfs):
        print("X")
alex = Child()
alex.print_first_name()
alex.print_last_name()

# Property decorators - getter setter deleter
# If we add @property above method - we can call a method
# as a variable without ()
class Employee:

    # Constructor
    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + "." + last + "@email.com"

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("John", "Smith")
#emp_1.fullname = "John Travolta"

print("\t New Class *******\n")
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())


class Loop:
    max_iter = None

    def __init__(self, max_iter):
        self.max_iter = max_iter

    def loop(self):
        counter = 0
        while counter < self.max_iter:
            counter += 1
            print(counter)
        return False


l = Loop(max_iter=5)
print(l.loop())

class Human:
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print(f"Hello, I am {self.age}")

human = Human(age=35)
human.say_hello()

class HumanExtended(Human):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.age} and I am {self.name}")

human2 = HumanExtended(age=40,name="Bob")
human2.say_hello()

class Car:
    def __init__(self, brand, color, engine):
        self.brand = brand
        self.color = color
        self.engine = engine

    # Static methods - don't depend on tributes of class and can exist by itesf without
    # an object of class
    @staticmethod
    def drive_forward():
        print("Car is driving forward")

    @staticmethod
    def drive_backward():
        print("Car is driving backward")


car = Car(brand="Audi", color="Black", engine=2.4)
car.drive_forward()
Car.drive_backward()

class Car2(Car):
    @staticmethod
    def turn_left():
        print("Turn left")

    @staticmethod
    def turn_right():
        print("Turn right")

car = Car2("Audi", "white", 3.5)
car.turn_left()
car.drive_forward()

class Airplane:
    def __init__(self, model):
        self.airplane_model = model

    @staticmethod
    def up():
        print("Going up")

    @staticmethod
    def land():
        print("Landing in progress")

class FlyingCar(Car2, Airplane):
    def __init__(self, brand, color, engine, model):
        Car2.__init__(self, brand, color, engine)
        Airplane.__init__(self, model)

fc = FlyingCar(brand="Tesla", color="Black", engine=10, model="F")
fc.up()
fc.drive_backward()
fc.turn_left()
fc.land()






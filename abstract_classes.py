# Prevents user from creating an object of that class.
# compels a user to override abstract methods in a child class.

# abstract class = A class which contains one or more abstract methods.
# abstract method = A method that has a declaration but does not have an implementation.

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):  # Even one abstract method can turn a class into a abstract class.
        print("You turned on the engine.")
    
    def stop(self):
        print("The vehicle has stopped.")

class Car(Vehicle):
    def go(self):
        super().go()
        print("You are driving a car.")

class Motorcycle(Vehicle):
    def go(self):
        super().go()
        print("Yor are riding a motorcycle.")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
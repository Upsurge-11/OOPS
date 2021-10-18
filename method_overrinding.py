class Animal:
    def eat(self):
        print("This Animal is eating.")

class Rabbit(Animal):
    def eat(self):
        print("This Rabbit is eating.")

bunny = Rabbit()

bunny.eat()
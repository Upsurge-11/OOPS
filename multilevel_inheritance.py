class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating.")

class Dog(Animal):
    def bark(self):
        print("This dog is barking.")

sheru = Dog()

print(sheru.alive)
sheru.eat()
sheru.bark()
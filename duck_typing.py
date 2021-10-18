# Duck typing is a concept where the class of an object is less important than the methods/attributes. Class type is not checked
# if minimum methods/attributes are present. If it walks like a duck, and it quacks like a duck, then it is a duck.

class Duck:
    def walk(self):
        print("The duck is walking.")
    def talk(self):
        print("The duck is qwuacking.")
    
class Chicken:
    def walk(self):
        print("The chicken is walking.")
    def talk(self):
        print("The chicken is clucking.")
    
class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the bird.")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)
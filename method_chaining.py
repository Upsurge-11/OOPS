# Method chaining is calling multiple methods sequentially, each call performs an action on the same object and returns self.
# \ is a line continuation character.
class Car:
    def turn_on(self):
        print("You started the engine.")
        return self
    
    def drive(self):
        print("You are driving the car.")
        return self
    
    def brake(self):
        print("You stepped on the brakes.")
        return self
    
    def turn_off(self):
        print("You turned off the engine.")
        return self

benz = Car()

# benz.turn_on().drive().brake().turn_off() this can also be written as,

benz.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
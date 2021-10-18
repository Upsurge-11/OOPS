class Animal:
    alive = True

    def eat(self):
        print("This animal can eat.")

    def sleep(self):
        print("This animal can sleep.")

class Rabbit(Animal):

    def run(self):
        print("This rabbit is running.")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying.")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming.")

bunny = Rabbit()
nemo = Fish()
drino = Hawk()

print(bunny.alive)
nemo.eat()
drino.sleep()
bunny.run()
drino.fly()
nemo.swim()
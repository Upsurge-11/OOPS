from car import Car

car_1 = Car("Mercedes","Benz",2021,"Black")
car_2 = Car("Lamborghini","Gallardo",2021,"Yellow")

car_1.wheels = 8
Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
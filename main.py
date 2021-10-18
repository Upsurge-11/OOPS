from car import Car

car_1 = Car("Mercedes","Benz",2021,"Black")

print(car_1.make, end = " ")
print(car_1.model, end = " ")
print(car_1.year, end = " ")
print(car_1.color)

car_1.drive()
car_1.stop()

car_2 = Car("Lamborghini","Gallardo",2021,"Yellow")

print(car_2.make, end = " ")
print(car_2.model, end = " ")
print(car_2.year, end = " ")
print(car_2.color)

car_2.drive()
car_2.stop()
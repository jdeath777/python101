#simple variable usage

#declaring variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

#doing operations on variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#print statements

print("Expected output")

print(cars)
print( drivers)
print(cars_not_driven)
print(carpool_capacity)
print(passengers)
print(average_passengers_per_car)

print("Actual output")

print("There are", cars, "cars available.")
print("There are only", drivers, "driveres available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive())
my_new_car.update_odometer(1000)
my_new_car.read_odometer()
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()

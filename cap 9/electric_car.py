class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has {} km on it.".format(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not reduce an odometer!!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class EletricCar(Car):
    """Representa aspectos de um carro especificos de veiculos eletricos"""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai"""
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a {} KWh battery".format(self.battery_size))

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go aprox. " + str(range)
        message += "km on a full charge"
        print(message)

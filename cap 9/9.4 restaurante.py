class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is {}.".format(self.restaurant_name.title()))
        print("The cousine type is {}".format(self.cuisine_type.title()))

    def cuisine_open(self):
        print("The {} is now open!!".format(self.restaurant_name.title()))

    def total_served(self):
        print("\tThe amount of costumer was {}".format(self.number_served))

    def set_number_served(self, set_served):
        self.number_served = set_served

    def increment_served(self, increment):
        self.number_served += increment


rest1 = Restaurant("cavalo murcho", "trash food")
rest1.describe_restaurant()
rest1.cuisine_open()
rest1.total_served()
rest1.set_number_served(200)
rest1.total_served()
rest1.increment_served(10)
rest1.total_served()

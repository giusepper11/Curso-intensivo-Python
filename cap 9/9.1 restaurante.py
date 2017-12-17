class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is {}.".format(self.restaurant_name.title()))
        print("The cousine type is {}".format(self.cuisine_type.title()))

    def cuisine_open(self):
        print("The {} is now open!!".format(self.restaurant_name.title()))


rest1 = Restaurant("cavalo murcho","trash food")
rest1.describe_restaurant()
rest1.cuisine_open()

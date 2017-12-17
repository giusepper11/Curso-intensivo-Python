class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe restaurant name is {}.".format(self.restaurant_name.title()))
        print("The cousine type is {}".format(self.cuisine_type.title()))

    def cuisine_open(self):
        print("The {} is now open!!".format(self.restaurant_name.title()))


rest1 = Restaurant("cavalo murcho","trash food")
rest1.describe_restaurant()
rest1.cuisine_open()

rest2 = Restaurant("sushimo","japanese food")
rest2.describe_restaurant()
rest2.cuisine_open()

rest3 = Restaurant("habbis","arabe")
rest3.describe_restaurant()
rest3.cuisine_open()

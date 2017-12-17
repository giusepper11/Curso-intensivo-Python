class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is {}.".format(self.restaurant_name.title()))
        print("The cousine type is {}".format(self.cuisine_type.title()))

    def cuisine_open(self):
        print("The {} is now open!!".format(self.restaurant_name.title()))


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors=[], cuisine_type='ice cream store'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavor(self):
        print("Os sabores disponiveis são:")
        for flavor in self.flavors:
            print("\t" + flavor.title())


rest1 = IceCreamStand("cavalo murcho", ['abaxaci', 'limão', 'flocos'])
rest1.describe_restaurant()
rest1.cuisine_open()
rest1.describe_flavor()

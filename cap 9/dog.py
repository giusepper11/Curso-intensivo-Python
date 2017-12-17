class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("{} is now sitting".format(self.name.title()))

    def roll(self):
        print("{} is now rolling".format(self.name.title()))


my_dog = Dog("willie", 4)
print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(my_dog.age))
my_dog.sit()
my_dog.roll()

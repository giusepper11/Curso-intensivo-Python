class User():
    def __init__(self, first_name, last_name, age, hobbie):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobbie = hobbie

    def describe_user(self):
        print("\nThe user first name is {}.".format(self.first_name.title()))
        print("The user last name is {}.".format(self.last_name.title()))
        print("The user age is {}.".format(self.age))
        print("The user fav hobbie is {}.".format(self.hobbie.title()))

    def greet_user(self):
        print("Hello, {} {}!".format(self.first_name.title(), self.last_name.title()))


user1 = User('giuseppe', 'rosa', 25, 'program')
user1.describe_user()
user1.greet_user()

user2 = User('debora', 'paganini', 27, 'read')
user2.describe_user()
user2.greet_user()

user3 = User('test', 'test1', 99, 'test')
user3.describe_user()
user3.greet_user()

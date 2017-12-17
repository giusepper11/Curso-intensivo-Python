class User():
    def __init__(self, first_name, last_name, age, hobbie):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobbie = hobbie
        self.login_attempts = 0

    def describe_user(self):
        print("\nThe user first name is {}.".format(self.first_name.title()))
        print("The user last name is {}.".format(self.last_name.title()))
        print("The user age is {}.".format(self.age))
        print("The user fav hobbie is {}.".format(self.hobbie.title()))

    def greet_user(self):
        print("Hello, {} {}!".format(self.first_name.title(), self.last_name.title()))

    def read_login_attempts(self):
        print("\nLogin Attempts = {}".format(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('giuseppe', 'rosa', 25, 'program')
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()

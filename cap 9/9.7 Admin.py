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


class Admin(User):
    def __init__(self, first_name, last_name, age, hobbie,
                 privileges=('can add post', 'can delete post', 'can ban user')):
        super().__init__(first_name, last_name, age, hobbie)
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges are: ")
        for privilege in self.privileges:
            print("\t{}".format(privilege.capitalize()))


admin1=Admin('giuseppe','rosa',25,'develop')
admin1.show_privileges()

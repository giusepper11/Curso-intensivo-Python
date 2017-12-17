class Employee():
    def __init__(self, first, last, anual_salary):
        self.first = first
        self.last = last
        self.anual_salary = anual_salary

    def give_rise(self, moneyrise=5000):
        self.moneyrise = moneyrise
        self.anual_salary += moneyrise


employee1 = Employee('Giuseppe', 'rosa', 10000)
print("O salario atual de {} {} é {} reais".format(employee1.first.title(), employee1.last.title(),
                                                   employee1.anual_salary))
employee1.give_rise()
print(employee1.anual_salary)

"""Exibe a lista de ingredientes pedidos"""


def make_pizza(size, *toppings):
    print("\nMaking a {} inches pizza with the following toppings:".format(size))
    for topping in toppings:
        print("- {}.".format(topping.title()))

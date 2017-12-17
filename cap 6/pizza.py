pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print('You ordered a {} crusted pizza with the following toppings:'.format(pizza['crust']))
for topping in pizza['toppings']:
    print("\t{}".format(topping))

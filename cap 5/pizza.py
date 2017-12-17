available_toppings = ['mushrooms', 'olives', 'green pepper', 'pepperoni', 'pinapple', 'extra cheese']
requested_toppings = ['mushrooms', 'extra cheese', 'french fries']

# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')
#
for requested_topping in requested_toppings:

    if requested_topping in available_toppings:
        print('Adding {} as requested'.format(requested_topping.title()))
    else:
        print('Nao temos  {}'.format(requested_topping.title()))

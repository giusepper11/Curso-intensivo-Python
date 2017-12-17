my_pizzas = ['portuguesa', 'calabresa', 'baiana']
f_pizza = my_pizzas[:]

my_pizzas.append('4 queijos')
f_pizza.append('chocolate')

print('\nMinhas pizzas favoritas sao:')
for n in my_pizzas:
    print(n.title())

print('\nAs pizzas favoritas do meu amigo sao:')
for n in f_pizza:
    print(n.title())

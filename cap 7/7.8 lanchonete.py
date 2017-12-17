sandwich_orders = ['atum', 'calabresa', 'hamburguer', 'frango']
finished_orders = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\nPreparando seu sanduiche de {}'.format(sandwich.title()))
    finished_orders.append(sandwich)

print('\nSanduiches prontos')
for sandwich in finished_orders:
    print('Sanduiche de {} esta pronto.'.format(sandwich.title()))

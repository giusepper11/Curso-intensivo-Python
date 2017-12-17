sandwich_orders = ['atum', 'calabresa', 'hamburguer', 'frango', 'pastrami', 'pastrami', 'pastrami']
finished_orders = []

print('Estamos sem pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\nPreparando seu sanduiche de {}'.format(sandwich.title()))
    finished_orders.append(sandwich)

print('\nSanduiches prontos')
for sandwich in finished_orders:
    print('Sanduiche de {} esta pronto.'.format(sandwich.title()))

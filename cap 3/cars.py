car = ['bmw', 'audi', 'toyota', 'subaru']
print(car)

car.sort()
print(car)

car.sort(reverse=True)
print(car)

car = ['bmw', 'audi', 'toyota', 'subaru']

print('\nA lista original')
print(car)

print('\nA lista em ordem')
print(sorted(car))

print('\nA lista em ordem novamente')
print(car)

print('\n A ordem reversa da lista')
print(car)
car.reverse()
print(car)

print('\n' + str(len(car)))

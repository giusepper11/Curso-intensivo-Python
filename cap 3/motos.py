moto = ['honda', 'yamaha', 'suzuki']
print(moto)

moto[0] = 'ducati'
print(moto)

print('---------------------')
moto = []

moto.append('yamaha')
moto.append('honda')
moto.append('suzuki')
print(moto)

moto.insert(0, 'ducati')
print(moto)

print('-------------------')

moto = ['honda', 'yamaha', 'suzuki']
print(moto)
del moto[0]
print(moto)

print('-------------------')

moto = ['honda', 'yamaha', 'suzuki']
print(moto)
pooped_moto = moto.pop()
print(pooped_moto)
print(moto)

print('-------------------')

moto = ['honda', 'yamaha', 'suzuki']
print(moto)
pooped_moto = moto.pop(0)
print(pooped_moto)
print(moto)

print('-------------------')

moto = ['honda', 'yamaha', 'suzuki', 'ducati']
print(moto)
impossible = 'ducati'
moto.remove(impossible)
print(moto)
print('\n A ' + impossible.title() + ' é muito cara para mim')

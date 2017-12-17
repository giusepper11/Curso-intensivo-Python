cachorro = {'tipo': 'cachorro', 'dono': 'joe'}
gato = {'tipo': 'gato', 'dono': 'marta'}
passaro = {'tipo': 'passaro', 'dono': 'ana'}
tartaruga = {'tipo': 'tartaruga', 'dono': 'ed'}

pets = [cachorro, gato, passaro, tartaruga]
for pet in pets:
    print('O/A {} pertence a/ao {} '.format(pet['tipo'].title(), pet['dono'].title()))

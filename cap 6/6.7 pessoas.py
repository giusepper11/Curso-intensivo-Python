pessoa1 = {'first_name': 'giuseppe', 'last_name': 'rosa', 'age': 25, 'city': 'sao paulo'}
pessoa2 = {'first_name': 'debora', 'last_name': 'paganini', 'age': 27, 'city': 'sao paulo'}
pessoa3 = {'first_name': 'gerald', 'last_name': 'grabner', 'age': 44, 'city': 'graz'}

pessoas = [pessoa1, pessoa2, pessoa3]

for pessoa in pessoas:
    print('\nNome completo é {} {}'.format(pessoa['first_name'].title(), pessoa['last_name'].title()))
    print('A idade é {}'.format(pessoa['age']))
    print('Sua cidade natal é {}'.format(pessoa['city'].title()))

favorite_places = {
    'giuseppe': ['munique', 'orlandia', 'saltsburg'],
    'debora': ['gramado', 'campos', 'rio'],
    'ed': ['paris', 'londres', 'campinas']
}

for nome, lugares in favorite_places.items():
    print("\n Os lugares favoritos de {} são:".format(nome.title()))
    for lugar in lugares:
        print('\t{}'.format(lugar.title()))


rivers = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'ganges': 'india'
}

for river, country in rivers.items():
    print('O {} percorre pelo(a) {}'.format(river.title(), country.title()))

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

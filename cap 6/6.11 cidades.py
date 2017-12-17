cities = {
    'sao paulo': {
        'pais': 'brasil',
        'populacao': "12 milhoes",
        'fact': 'cidade suja',
    },
    'buenos aires': {
        'pais': 'argentina',
        'populacao': "10 milhoes",
        'fact': 'cidade horrivel',
    },

    'monterey': {
        'pais': 'mexico',
        'populacao': "11 milhoes",
        'fact': 'cidade grande',
    },
}

for city, city_info in cities.items():
    print("\n{}".format(city.title()))
    print("\tPais : {}".format(city_info['pais'].title()))
    print("\tPopulacao : {}".format(city_info['populacao'].title()))
    print("\tFato : {}".format(city_info['fact'].capitalize()))

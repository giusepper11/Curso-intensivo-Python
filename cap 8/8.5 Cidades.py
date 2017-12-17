def describe_city(name, country='brasil'):
    print('{} esta localizada no {}'.format(name.title(), country.title()))


describe_city('sao paulo')
describe_city('rio de janeiro')
describe_city(country='uruguai', name='montevideu')

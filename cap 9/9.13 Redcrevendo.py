from collections import OrderedDict

glossario = OrderedDict()

glossario['casa'] = 'moradia, residencia'
glossario['carro'] = 'meio de transporte'
glossario['tv'] = 'televisao'
glossario['livro'] = 'um conglomerado de palavras'
glossario['mesa'] = 'apoio'

for k, v in glossario.items():
    print("{} > {}".format(k.title(), v.capitalize()))

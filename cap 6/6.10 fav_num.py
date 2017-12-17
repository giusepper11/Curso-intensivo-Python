fav_num = {'giuseppe': [11, 2, 3], 'debora': [5], 'paulo': [32, 23], 'pedro': [15]}

for name, numbers in fav_num.items():
    if len(numbers) > 1:
        print('Os numeros favoritos de {} é:'.format(name.title()))
        for number in numbers:
            print('\t{}'.format(number))
    else:
        for number in numbers:
            print('O numero favorito de {} é {}'.format(name.title(), number))

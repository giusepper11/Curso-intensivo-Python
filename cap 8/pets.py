def pets(pet_name, animal_type='dog'):
    '''Exibe informacoes sobre um animal de estimacao'''
    print('\nI have a {}.'.format(animal_type))
    print('My {}`s name is {}.'.format(animal_type, pet_name.title()))


pets(pet_name='nina')
pets(animal_type='turtle', pet_name='no name')


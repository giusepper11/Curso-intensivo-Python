favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

empregados = ['jen', 'robert', 'phil', 'sarah', 'edward', 'maria']

for empregado in empregados:
    if empregado in favorite_languages.keys():
        print('{}, obrigado por participar'.format(empregado.title()))
    else:
        print('{}, por favor votar !!'.format(empregado.title()))

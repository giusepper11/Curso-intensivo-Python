age = int(input('\nDigite idade '))
while age >= 0:

    if age <= 2:
        print('Bebê')
    elif 2 < age <= 4:
        print('Crianca')
    elif 4 < age <= 13:
        print('garota(o)')
    elif 13 < age <= 20:
        print('Adolescente')
    elif 20 < age <= 65:
        print('Adulto')
    elif age > 65:
        print('Idoso')
    age = int(input('\nDigite idade '))

while True:
    try:
        n1 = int(input('\nDigite um numero inteiro '))
        n2 = int(input('Digite outro numero inteiro '))

    except ValueError:
        print("Devem apenas ser digitados numeros inteiros")
        continue
    else:
        r = int(n1) + int(n2)
        print(r)

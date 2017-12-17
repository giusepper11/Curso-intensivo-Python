i = True
while i:
    n = input('\nDigite sua idade: ')
    if n == 'quit':
        break
    else:
        n = int(n)
        if n <3:
            print('\tIngresso gratuito!')
        elif 3<=n<12:
            print("Ingresso custará 10 doletas")
        elif n>=12:
            print("Ingresso custará 15 doletas")

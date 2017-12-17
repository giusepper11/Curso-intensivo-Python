i = True
while i:
    ingrediente = input("\nDigite um ingrediente para sua pizza: ")
    if ingrediente == 'quit':
        break
    else:
        print('\n{} sera acrescentado a sua pizza '.format(ingrediente.title()))

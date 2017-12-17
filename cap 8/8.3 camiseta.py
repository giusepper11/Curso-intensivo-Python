def make_skirt(size, message):
    print('\nO tamanho da camiseta será {}'.format(size))
    print('A mensagem a ser estampada é :')
    print('{}'.format(message.capitalize()))


make_skirt('P', 'foda-se')
make_skirt(message='foda-se', size='P')

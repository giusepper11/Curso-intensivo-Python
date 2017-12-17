ativar = True
while ativar:
    mensagem = input('Digite qualquer coisa que o papagaio repete! ')
    if mensagem == 'quit':
        ativar = False
    else:
        print(mensagem)

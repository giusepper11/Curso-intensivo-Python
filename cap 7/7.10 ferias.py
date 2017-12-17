ferias = {}
i = True
while i:
    nome = input('\nDigite seu nome ')
    local = input('Qual suas ferias do sonho? ')
    ferias[nome] = local
    repitir = input('Deseja continuar com a pesquisa? s/n')
    if repitir == "n":
        break
print('\nO resultado da pesquisa: ')

for nome, local in ferias.items():
    print('{} deseja conhecer {}'.format(nome.title(), local.title()))

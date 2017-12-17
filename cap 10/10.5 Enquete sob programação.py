nome = input('Digite seu nome: ')
linguagem = input('Digite sua linguagem favorita ')
opiniao = input("opicional, digite o motivo: ")
while nome != '' and linguagem != '':
    with open('opinao.txt', 'a') as file_object:
        if opiniao:
            print("{} gosta de {} pois, {}".format(nome.title(), linguagem.title(), opiniao))
            file_object.write("{} gosta de {} pois, {}\n".format(nome.title(), linguagem.title(), opiniao))
        else:
            print("{} gosta de {}".format(nome.title(),linguagem.title()))
            file_object.write("{} gosta de {}.\n".format(nome.title(), linguagem.title()))
        file_object.close()
    nome = input('Digite seu nome: ')
    linguagem = input('Digite sua linguagem favorita ')
    opiniao = input("opicional, digite o motivo: ")

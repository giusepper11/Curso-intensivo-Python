nome_convidado = input("Digite seu nome: ")

filename = 'guest.txt'
with open(filename,"a") as file_object:
    file_object.write('{}\n'.format(nome_convidado.title()))


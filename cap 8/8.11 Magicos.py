def show_magicians(nomes):
    print(nomes)


def make_great(nomes, nomesmod):
    while nomes:
        magico_atual = 'O grande ' + nomes.pop()
        nomesmod.append(magico_atual)
        print(magico_atual)


magicos = ['1', '2', '3', '4']
magicos_grande = []

make_great(magicos[:], magicos_grande)
show_magicians(magicos)

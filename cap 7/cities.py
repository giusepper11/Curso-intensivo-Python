while True:
    cidade = input('Digite os lugares que vc ja visitou: ')

    if cidade == 'quit':
        break
    else:
        print("I'd love to go to {}!".format(cidade.title()))

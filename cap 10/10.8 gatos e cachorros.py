def read_file(filename):
    try:
        with open(filename) as f_obj:
            text = f_obj.read()
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado".format(filename))
    else:
        print(text)


read_file('cachorros.txt')

read_file('gatos1.txt')

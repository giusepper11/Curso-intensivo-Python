import json


def get_new_number():
    n = int(input("Digite seu numero favorito: "))
    filename = 'fav_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(n, f_obj)


def get_saved_number():
    filename = 'fav_num.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def remember_number():
    number = get_saved_number()
    if number:
        print("Seu numero favorito é {} ".format(number))
    else:
        get_new_number()


remember_number()

import json


def get_new_user():
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

    except FileNotFoundError:
        return None

    else:
        return username


def greet_user():
    username = get_stored_username()

    if username:
        r = input("Voce é o {} ? [s/n]".format(username))
        if r.lower() == 's':
            print("Welcome back, {}!".format(username))
        else:
            username = get_new_user()
            print("We'll remember you when you come back, {}!".format(username))
    else:
        username = get_new_user()
        print("We'll remember you when you come back, {}!".format(username))


greet_user()

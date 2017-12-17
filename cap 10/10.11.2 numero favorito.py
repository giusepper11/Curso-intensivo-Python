import json

filename = 'fav_num.json'
with open(filename) as f_obj:
    number = json.load(f_obj)
    print("Seu numero favorito é {} ".format(number))

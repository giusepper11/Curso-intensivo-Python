import json

n = int(input("Digite seu numero favorito: "))
filename = 'fav_num.json'
with open(filename, 'w') as f_obj:
    json.dump(n, f_obj)

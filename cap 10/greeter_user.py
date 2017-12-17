import json

with open('username.json') as f_obj:
    username = json.load(f_obj)
    print("Welcome back, {}!".format(username))
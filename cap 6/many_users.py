users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername : {}".format(username))
    fullname = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print("\tFull name : {}".format(fullname.title()))
    print("\tLocation : {}".format(location.title()))

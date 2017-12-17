responses = {}

polling_active = True
while polling_active:
    name = input('\nWhats your name? ')
    response = input("Which mountain would you like to climb? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print('\nPoll results:')
for name, response in responses.items():
    print("{} wants to climb {}".format(name.title(), response.title()))

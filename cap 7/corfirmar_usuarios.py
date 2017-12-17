user_nc = ['alice', 'brian', 'candace']
user_c = []

while user_nc:
    user = user_nc.pop()

    print("Verifying user: {}".format(user.title()))
    user_c.append(user)

print('\nThe following users have been confirmed: ')
for user in user_c:
    print(user.title())

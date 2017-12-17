current_users = ['Giuseppe', 'pedro', 'debora', 'Paulo', 'admin']

new_users = ['giuseppe', 'joao', 'debora', 'jose', 'paula']

current_users_lowe = []
for current_user in current_users:
    current_users_lowe.append(current_user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lowe:
        print('Usuario {} em uso, use outro'.format(new_user.title()))
    else:
        print('Usuario disponivel')

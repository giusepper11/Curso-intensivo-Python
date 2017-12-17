users = ['giuseppe', 'pedro', 'debora', 'paulo', 'admin']

for user in users:
    if user == 'admin':
        print('Ola {}, deseja relatorio de status?'.format(user))
    else:
        print('Ola {}, obrigado por fazer login novamente!'.format(user.title()))

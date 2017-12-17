users = []

if users:
    for user in users:
        if user == 'admin':
            print('Ola {}, deseja relatorio de status?'.format(user))
        else:
            print('Ola {}, obrigado por fazer login novamente!'.format(user.title()))
else:
    print('Precisamos de novos usuarios!!')

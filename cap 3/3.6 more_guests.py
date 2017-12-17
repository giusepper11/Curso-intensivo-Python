guest = ['joao', 'maria', 'pedro', 'ana']

print(guest)

guest.insert(0, 'paulo')
guest.insert(2, 'debora')
guest.append('giuseppe')

for i in range(len(guest)):
    print('Voce , ' + guest[i].title() + ' , esta convidado para meu jantar')

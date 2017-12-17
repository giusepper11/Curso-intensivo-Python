guest = ['joao', 'maria', 'pedro', 'ana']

print(guest)

pop_guest = guest.pop(2)
print(guest)
print(pop_guest)
guest.append('jose')
print(guest)

for i in range(len(guest)):
    print('Voce , ' + guest[i].title() + ' , esta convidado para meu jantar')

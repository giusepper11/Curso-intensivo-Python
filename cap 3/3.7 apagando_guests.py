guest = ['joao', 'maria', 'pedro', 'ana']
pop_guest = []
print(guest)

guest.insert(0, 'paulo')
guest.insert(2, 'debora')
guest.append('giuseppe')
print(guest)

while len(guest) >= 3:
    pop_guest.append(guest.pop())
print(pop_guest)

for i in range(len(pop_guest)):
    print('Voce , ' + pop_guest[i].title() + ' , nao esta mais convidado para meu jantar')

for i in range(len(guest)):
    print('Voce , ' + guest[i].title() + ' , esta convidado para meu jantar')

del guest[0]
del guest[0]

print(guest)

alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'fast'}
print('X inicial é : {}'.format(alien_0['x_pos']))

# move o alienigena para a direita
# Determina a distancia que o alienigina deve se deslocar de acordo com sua velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # esse alienigena eh rapido
    x_increment = 3

# A nova posicao eh a posicao antiga somada ao incremento
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print('Nova posicao é : {}'.format(alien_0['x_pos']))

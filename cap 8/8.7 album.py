def make_album(nomear, nometi, nrf=''):
    album = {'Artista': nomear, 'titulo': nometi}
    if nrf:
        album['Nro de faixas'] = nrf
    return album


while True:
    print('\nDigite info sob album ou digite "q" para encerrar')
    artista = input('Artista: ')
    if artista=='q':
        break
    titulo = input('Album: ')
    if titulo=='q':
        break
    nro = input('Numero de faixas')
    if nro=='q':
        break
    album1 = make_album(artista, titulo, nro)
    print(album1)

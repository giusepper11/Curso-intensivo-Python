def build_profile(first, last, **user_info):
    """Construi um dicionario contendo tudo que sabemos sobre um usuario"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


meu_cadastro = build_profile('giuseppe', 'rosa', idade="25", sexo='m', estado_civil='casado')
for key, value in meu_cadastro.items():
    print("{} : {}".format(key.capitalize(), value.capitalize()))

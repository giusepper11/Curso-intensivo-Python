def build_profile(first, last, **user_info):
    """Construi um dicionario contendo tudo que sabemos sobre um usuario"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

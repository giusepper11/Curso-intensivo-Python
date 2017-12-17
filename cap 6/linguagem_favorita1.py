from _collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for nome, linguagen in favorite_languages.items():
    print("\t A linguagem favorita de {} é {}.".format(nome.title(), linguagen.title()))

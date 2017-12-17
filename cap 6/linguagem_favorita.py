favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for k, v in favorite_languages.items():
    print("{}'s favorite language is {}.".format(k.title(), v.title()))
print('\n')
for name in favorite_languages.keys():
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print('Erin, vote seu fdp !')

for name in sorted(favorite_languages.keys()):
    print("{}, thanks for taking the poll.".format(name.title()))

for language in set(favorite_languages.values()):
    print(language)

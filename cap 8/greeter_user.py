def greet_users(names):
    """Exibe uma saudacao simples para cada usuario"""
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)


usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)

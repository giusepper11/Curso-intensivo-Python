def get_formated(first, last, middle=''):
    """Gera um nome completo formatado"""
    if middle:
        # full_name = first + ' ' + middle + ' ' + last
        full_name = "{} {} {}".format(first, middle, last)
    else:
        # full_name = first + ' ' + last
        full_name = "{} {}".format(first, last)
    return full_name.title()


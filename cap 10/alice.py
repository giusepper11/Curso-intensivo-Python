filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file '{}' was not found!".format(filename))
else:
    # conta  o numero aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)
    print("The file '{}' has about {} words.".format(filename, num_words))

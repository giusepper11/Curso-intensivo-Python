def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file '{}' doesn't exist.".format(filename))
    else:
        words = contents.split()
        num_words = len(words)
        print("The file '{}' has about {} words".format(filename, num_words))


filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

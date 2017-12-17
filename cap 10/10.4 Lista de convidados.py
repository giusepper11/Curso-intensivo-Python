r = input('Digite seu nome ')
while r != "0":
    with open('guest_book.txt', 'a') as file_object:
        file_object.write("{}\n".format(r))
        print("\nOlá, {}".format(r.title()))
        file_object.close()
        r = input('Digite seu nome ')


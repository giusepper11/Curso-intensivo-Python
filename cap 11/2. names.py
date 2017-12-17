from name_function import get_formated

print("Print 'q' at any time to quit.")
while True:
    first = input("\nPlease give your first name: ").rstrip()
    if first == 'q':
        break
    last = input("Please give your last name: ").rstrip()
    if last == 'q':
        break

    formatted_name = get_formated(first, last)
    print("Formated name : {}.".format(formatted_name))

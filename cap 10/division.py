print("Give 2 numbers, I ll divide them")
print("type 'q' to quit")

while True:
    n1 = input("\nFirst number: ")
    if n1 == 'q':
        break
    n2 = input("Second number: ")
    if n2 == 'q':
        break
    try:
        r = int(n1) / int(n2)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(r)

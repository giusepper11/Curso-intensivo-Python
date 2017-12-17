n1 = input('Digite um numero inteiro ')
n2 = input('Digite outro numero inteiro ')
try:
    r = int(n1)+int(n2)
except ValueError:
    print("Devem apenas ser digitados numeros inteiros")

else:
    print(r)

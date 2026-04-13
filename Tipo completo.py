n = int(input("Digite um número: "))

if n == 0:
    print("Neutro")
elif n % 2 == 0 and n > 0:
    print("Par positivo")
elif n % 2 == 0 and n < 0:
    print("Par negativo")
elif n % 2 != 0 and n > 0:
    print("Ímpar positivo")
else:
    print("Ímpar negativo")
n = int(input("Digite um número: "))

if n % 2 == 0 and n > 0:
    print("Par positivo")
elif n % 2 == 0 and n < 0:
    print("Par negativo")
else:
    print("Ímpar")
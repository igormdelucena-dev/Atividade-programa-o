n = int(input("Digite um número: "))
maior = 0

while n > 0:
    if n > maior:
        maior = n

    n = int(input("Digite um número: "))

print (maior)
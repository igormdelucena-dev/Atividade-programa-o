negativos = 0
positivos = 0

while True:
    numero = float(input("Digite um número: "))

    if numero == 0:
        break

    if numero > 0:
        positivos += 1

    else:
        negativos += 1

    print ("Positivos:", positivos)
    print ("Negativos:", negativos)
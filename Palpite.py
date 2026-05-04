numero_secreto = 20

while True:
    palpite = int(input("Advinhe o número: "))

    if palpite == numero_secreto:
        print ("Parabéns, você acertou!")
        break

    if palpite < numero_secreto:
        print ("O número é maior")
    else:
        print ("O número é menor")
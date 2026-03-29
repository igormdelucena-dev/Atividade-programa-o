# Recebe peso e altura

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC

imc = peso / (altura ** 2)

# Mostra o resultado

print("O IMC é:", imc)
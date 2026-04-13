valor = input("Digite algo: ")

try:
    n = float(valor)
    print("Numérico")
    print(n ** 2)
except:
    print("Não é numérico")
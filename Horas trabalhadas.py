# Recebe horas trabalhadas e valor da hora

horas = float(input("Digite a quantidade de horas trabalhadas: ").replace(",", "."))

valor_hora = float(input("Digite o valor da hora trabalhada: R$ ").replace(",", "."))

# Calcula o salário total

salario = horas * valor_hora

# Mostra o resultado final

print("O salário total é: R$", salario)
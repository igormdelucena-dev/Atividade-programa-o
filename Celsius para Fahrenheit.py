# Recebe a temperatura em graus Celsius

celsius = float(input("Digite a temperatura em °C: ").replace(",", "."))

# Converte para Fahrenheit

fahrenheit = celsius * 9/5 + 32

#Mostra o resultado final

print("A temperatura em Fahrenheit é:", fahrenheit, "°F")
import decimal #para quando precisarmos de muita precisão

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
numero4 = decimal.Decimal(numero1 + numero2)
print(numero3)
print(f"{numero3:.2f}")
print(round(numero3, 2)) #round funciona como o de cima mas ele corta o 0
print(numero4)
numeroStr = input("Digite um número: ")

try:
    numeroFloat = float(numeroStr)
    print(f"O dobro de {numeroStr} e {numeroFloat * 2}")
except:
    print("Isso não é um número")
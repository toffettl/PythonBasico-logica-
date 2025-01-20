condicao = True
while condicao:
    nome = input("Qual o seu nome? ")
    print(f"Seu nome é {nome}")

    if nome == "sair":
        break

print("Saiu!")

contador = 0

while contador < 10:
    contador += 1

    if contador == 6: #pulando o seis
        continue

    print(contador)

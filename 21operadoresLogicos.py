entrada = input("[E]ntrar [S]air: ")
senhaDigitada = input("Senha: ")

senha = "1234"

if (entrada == "E" or entrada == "e") and senhaDigitada == senha:
    print("Entrar")
else:
    print("Sair")







#avaliação de curto circuito
print(True and False and True)
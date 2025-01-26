frase = "Olha só que, coisa interessante"
listaPalavras = frase.split(",") #divide a str conforme o parametro 

for i, frase in enumerate(listaPalavras):
    print(listaPalavras[i])
    print(listaPalavras[i].strip()) #strip tira os espaços
    print(listaPalavras[i].lstrip()) #lstrip tira os espaços da esquerda
    print(listaPalavras[i].rstrip()) #rstrip tira os espaços da direita


print(listaPalavras)
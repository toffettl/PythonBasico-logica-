frase = "O Python é uma linguagem de programação "\
    "multiparadigma. "\
    "Python foi criado por guido van Rossum." # \ para quebrar linha

i = 0
apareceuMais = 0
letraApareceuMais = ""

while i < len(frase):
    letraAtual = frase[i]

    if letraAtual == "." or letraAtual == " ":
        i += 1
        continue

    quantasVezesApareceu = frase.count(letraAtual)

    if apareceuMais < quantasVezesApareceu:
        apareceuMais = quantasVezesApareceu
        letraApareceuMais = letraAtual

    i += 1

print(f"A letra que mais apareceu foi {letraApareceuMais}")


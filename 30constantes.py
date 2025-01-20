velocidade = 60
localCarro = 90

RADAR1 = 2 #usamos letras maíusculas para definir variaveis constantes
LOCAL1 = 100
RADAR_RANGE = 1

if velocidade > RADAR1:
    print("Velocidade carro passou do radar 1")

if localCarro >= (LOCAL1 + RADAR_RANGE) and localCarro <= (LOCAL1 + RADAR_RANGE) and velocidade > RADAR1:
    print("Carro multado em radar 1")
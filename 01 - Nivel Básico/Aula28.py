"""
CONSTANTE = "variáveis" que não vão mudar
Muitas condições no memso if (ruim)

       <- Contagem de complexibilidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1.')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if  carro_multado_radar_1:
    print('Carro multado em radar 1.')
#aprofundando sobre if, elif e else

condicao = True

if condicao:
    print("Este é o código if") #podemos ter um if sozinho
else:
    print("else")

print('Fora do if')

#Não podemos executar if e else ao memso tempo
#não podemos ter else e elif sozinhos

condicao1 = True
condicao2 = True
condicao3 = False
condicao4 = False

if condicao1:
    print("codigo condição 1")
elif condicao2:
    print("codigo condição 2")
elif condicao3:
    print("codigo condição 3")
elif condicao4:
    print("codigo condição 4")
else:
    print("Nenhuma das condições foi satisfeita!")
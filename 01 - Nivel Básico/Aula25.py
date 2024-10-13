"""
Fatiamento de Strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a função len retorna a quantidade de caracteres da str


"""

variavel = 'Olá mundo'
print(variavel[4:]) #imprime mundo
print(len(variavel)) #imprime 9
print(variavel[0:len(variavel):1]) #checa os caracteres de 1 em 1.
print(variavel[0:len(variavel):2]) #checa os caracteres de 2 em 2.
#Podemos fazer o passo com números negativos, então ele conta de trás pra frente.
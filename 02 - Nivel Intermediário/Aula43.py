# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1),len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]
 
print(zipper(l1, l2))

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2))) #leva em consideração a lista maior 
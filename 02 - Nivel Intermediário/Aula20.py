# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort()
lista.sort(reverse=True)# reordena de traz para frente
#podemos usar o sort
print(lista)
lista_new = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#como ordenar dicionários?

#precisamos ensinar o python a ordenar essa estrutura de dados 
#criando uma função pra ordenar 


def ordena(item):
    return item['nome']

lista_new.sort(key = ordena)

for item in lista_new:
    print(item)

lista_new.sort(key=lambda item: item['nome'])
print(lista_new)

l1 = sorted(lista_new, key=lambda item: item['nome'])
print(l1)
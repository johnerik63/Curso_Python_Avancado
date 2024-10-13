'''
enumerate - enumera iteráveis (indices)

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)

print('O que tem na minha lista enumerada: ', lista_enumerada)

#Podemos usar o iterator várias vezes se não jogarmos ele em uma variável

lista_2 = ['Maria', 'Helena', 'Luiz', 8]

for i in enumerate(lista_2):
    print(i)

for indice, nome in enumerate(lista_2):
    print(indice, nome)

#podemos transformar o enumerate em uma lista, que me mostrará o indice e o elemento daquele indice
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, *
create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    extend - estende a lista
    + - concatena as listas 

"""

#concatenação de listas

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # mexe diretamente na lista_a

print(lista_c)
print(lista_d)
print(lista_a)
"""
Cuidados com dados mutáveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutavel)

"""

# nome = 'Pedro'
# noutra_variável = nome
# nome  = 'joão'
# print(nome)
# print(noutra_variável)

# esses valores tem ID diferentes

lista_a = ['Pedro', 'Marta', 1, True, 1.2]
lista_b = lista_a.copy()
lista_a[0] = 'qualquer coisa'

print(lista_b)
print(lista_a)
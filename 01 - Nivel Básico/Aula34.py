"""
Iterando Strings em Python

"""

nome = 'Pedro Henrique' # Iteráveis 

# contador = 0
# while contador < len(nome):
#     nova_string = nome[contador]
#     contador += 1
#     print(f'*{nova_string}', end='')

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'

print(novo_nome)


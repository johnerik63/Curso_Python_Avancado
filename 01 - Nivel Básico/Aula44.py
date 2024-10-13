"""
Introdução ao desempacotamento + tuples (tuplas)

"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

nome_1, *_ = ['Kaio', 'Matheus', 'José', 'Marcos']
print(_)
# O underline serve pra dizer que não vou usar o resto da lista

# tuplas: uma lista imutável

nomes = ['Maria', 'Helena', 'Marcos']
print(nomes)
nomes = tuple(nomes)
print(nomes)
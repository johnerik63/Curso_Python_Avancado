"""
Retorno de valores das funções (return)
"""

variavel = print('Pedro')
print(variavel) #retorna none

def soma(x, y):
    ...

variavel = soma(1, 2)
variavel = int('1')
print(variavel)

def soma(x, y):
    return x + y

soma1 = soma(1, 3)
soma2 = soma(5, 7)
print(soma1)
print(soma2)
print(soma1 + soma2)

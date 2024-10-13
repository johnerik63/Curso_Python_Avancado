"""
Exercícios de funções:

Crie uma função que multiplique todos os argumentos não nomeados recebidos
Retorna o total para uma variável e mostre o valor da variável.

Crie uma função fala se um número é par ou impar
Retorne se o numero é par ou impar 

"""

def multiplica(*args):
    multiplica = 1
    for numeros in args:
        multiplica *= numeros
    return multiplica

n = input("quantos valores você quer multiplicar? ")
lista_numeros = []
if n.isnumeric() == True:
    n = int(n)
    for i in range(n):
        numeros_recebidos = input(f"Digite o {i+1}° numero: ")
        numeros_recebidos = int(numeros_recebidos)
        lista_numeros.append(numeros_recebidos)


resultado = multiplica(*lista_numeros)
print("--------------------------------------------------------------------------")
print(f"O resultado da multiplicação de todos os valores digitados é: {resultado}")
print("--------------------------------------------------------------------------")

def par_impar(x):
    if x % 2 == 0:
       return print(f"O numero {x} é par!")
    return print(f"O número {x} é ímpar!")

numero = input("digine um número para saber se ele é par ou impar: ")
numero = int(numero)
par_impar(numero)




"""
args -  Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

"""

x, y, *resto = 1, 2, 3, 4

print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

soma_args = soma(1, 2, 3, 4, 5)

soma_args_2= soma(1, 4, 3, 4, 7)

print(soma_args)
print(soma_args_2)

#Agora podemos passar quantos argumentos não nomeados quisermos
#Existe uma função pronta no Python que ja faz isso

#print(sum((1, 4, 6, 5, 7, 4, 3)))

numeros = 1, 52, 46, 52, 6, 7, 8, 9, 10, 99
outra_soma = soma(*numeros)
print(numeros)
print(outra_soma)
print(sum(numeros))
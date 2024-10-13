"""
introdução a funções (def) em Python
Funções são trechos de códigos usados para replicar determinada ação ao longo do código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específic. Por padrão, funçoes em python retorna none (nada)

"""

# def Print():
#     print('varias1')
#     print('varias2')
#     print('varias3')
#     print('varias4')

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)

def saudacao(nome='sem nome'):
    print(f'Olá, {nome}.')

saudacao('Pedro')
saudacao('Maria')
saudacao()

#podemos dar um valor ao nome para poder chamar a função sem parâmetros.


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

# empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

print(a, b)

pessoa = {
    'nome': 'Aline',
    'Sobrenome': 'Souza'
}

a, b = pessoa.values()
a, b = pessoa.items()
#Se eu não trago values a, b vai ser igual as keys
print(a, b)
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)


pessoa = {
    'nome': 'Aline',
    'Sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6

}

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa) #aqui temos um dicionário completo

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
#gera um dicionário

mostro_argumentos_nomeados(**pessoas_completa)

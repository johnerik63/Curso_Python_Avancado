"""
Higer Order Functions
Funções de primeira Classe

"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom Dia', 'Pedro')
    )
print(
    executa(saudacao, 'Bom Noite', 'Maria')
    )

#Resumindo: Podemos jogar funções dentro de outras funções.


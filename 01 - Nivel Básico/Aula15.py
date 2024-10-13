#Como coletar dados em Python 
nome = input('Qual o seu nome? ')
print(f'Olá {nome} como vai?')# imprime 'Olá "nome do usuário" como vai?'
print(f'Olá {nome=} como vai?')#{nome=} imprime nome='nome do usuário'.

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'A soma dos números {numero_1} e {numero_2} é = {numero_1 + numero_2}')
# O problema de colocar o int no input é que você fica sem saber o que o usuário digitou.
# Ou seja, impossibilita a checagem da entrada do dado fornecida pelo usuário.

# O correto seria:

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números {numero_1} e {numero_2} é = {int_numero_1 + int_numero_2}')

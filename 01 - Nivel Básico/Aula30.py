"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print('------------------------------------------')
numero =  input('Digite um número inteiro: ')
if '.' not in numero and numero.isdigit():
    num = int(numero)
    if num % 2 == 0:
        print('Seu número é par!')
    else:
        print('Seu número é impar!')
else:
    print('O número digitado não é inteiro!')
print('------------------------------------------')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('------------------------------------------')
print('ESCREVA AS HORAS NO FORMATO HH:MM')
hora = input('Que horas são? ')
hora = str(hora).replace(':','.')
hora = float(hora)
if 0 <= hora <= 11:
    hora = str(hora).replace('.',':')
    print(f'São {hora} da manhã. Bom Dia!')
elif 12 < hora <= 17:
    hora = str(hora).replace('.',':')
    print(f'São {hora} da tarde. Boa Tarde!')
else:
    hora = str(hora).replace('.',':')
    print(f'São {hora} da noite. Boa Noite!')
print('------------------------------------------')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('------------------------------------------')
nome = input('Digite seu nome: ')
qtd_letras = len(nome)
if qtd_letras <= 4:
    print(f'Prazer {nome}, seu nome tem {qtd_letras} letras e é considerado curto! ')
elif 5 <= qtd_letras <= 6:
    print(f'Prazer {nome}, seu nome tem {qtd_letras} letras e é considerado normal! ')
elif qtd_letras > 6:
    print(f'Prazer {nome}, seu nome tem {qtd_letras} letras e é considerado grande! ')
else:
    print('Por Favor digite algo!')
print('------------------------------------------')




"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

while True:
    cont_2 = 0
    vetor_digitos = []
    vetor_onze = [11, 10,  9,  8,  7,  6,  5,  4,  3,  2]
    vetor_dez_primeiros_digitos = []
    cpf = input("Digite o aqui seu CPF [apenas numeros]: ")
    if cpf.isnumeric():
        for i in cpf:
            i = int(i)
            vetor_digitos.append(i)
        for j in range(0, 10):
            vetor_dez_primeiros_digitos.append(vetor_digitos[j])
            soma_dos_produtos = vetor_dez_primeiros_digitos[j] * vetor_onze[j]
            cont_2 += soma_dos_produtos
    else:
        print('por favor, digite apenas números!')
    digito_2 = (cont_2 * 10) % 11
    if digito_2 > 9:
        digito_2 = 0
    else:
        digito_2 = digito_2
    print('----------------------------------')
    print(f'o segundo digito do CPF é: {digito_2}')
    print('----------------------------------')
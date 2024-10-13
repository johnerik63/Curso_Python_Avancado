"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:
    cont = 0
    vetor_digitos = []
    vetor_dez = [10,  9,  8,  7,  6,  5,  4,  3,  2]
    vetor_nove_primeiros_digitos = []
    cpf = input("Digite o aqui seu CPF [apenas numeros]: ")
    if cpf.isnumeric():
        for i in cpf:
            i = int(i)
            vetor_digitos.append(i)
        for j in range(0, 9):
            vetor_nove_primeiros_digitos.append(vetor_digitos[j])
            soma_dos_produtos = vetor_nove_primeiros_digitos[j] * vetor_dez[j]
            cont += soma_dos_produtos
        print(vetor_nove_primeiros_digitos)
    else:
        print('por favor, digite apenas números!')
    res = (cont * 10) % 11
    if res > 9:
        res = 0
    else:
        res = res
    print('----------------------------------')
    print(f'o primeiro digito do CPF é: {res}')
    print('----------------------------------')














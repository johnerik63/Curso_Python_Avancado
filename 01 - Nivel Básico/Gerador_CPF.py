import random

#GERADOR DE CPF's

while True:
    cpf_nove_digitos = ''
    for i in range(9):
        cpf_nove_digitos += str(random.randint(0, 9))
    cont = 0
    cont_2 = 0
    vetor_digitos = []
    vetor_onze = [11, 10,  9,  8,  7,  6,  5,  4,  3,  2]
    vetor_dez_primeiros_digitos = []
    vetor_dez = [10,  9,  8,  7,  6,  5,  4,  3,  2]
    vetor_nove_primeiros_digitos = []
    if cpf_nove_digitos.isnumeric() and len(cpf_nove_digitos) == 9:
        for i in cpf_nove_digitos:
            i = int(i)
            vetor_digitos.append(i)
        for j in range(0, 9):
            vetor_nove_primeiros_digitos.append(vetor_digitos[j])
            soma_dos_produtos = vetor_nove_primeiros_digitos[j] * vetor_dez[j]
            cont += soma_dos_produtos
        digito_1 = (cont * 10) % 11
        if digito_1 > 9:
            digito_1 = 0
        else:
            digito_1 = digito_1
        vetor_digitos.append(digito_1)
        for j in range(0, 10):
            vetor_dez_primeiros_digitos.append(vetor_digitos[j])
            soma_dos_produtos = vetor_dez_primeiros_digitos[j] * vetor_onze[j]
            cont_2 += soma_dos_produtos
        digito_2 = (cont_2 * 10) % 11
        if  digito_2 > 9:
            digito_2 = 0
        else:
            digito_2 = digito_2
    
        digito = str(digito_1) + str(digito_2)
        cpf_valido = cpf_nove_digitos + '-' + digito
        print('-------------------------------')
        print('Geramos um CPF para você:')
        print(f'O CPF gerado é: {cpf_valido}')
        print('-------------------------------')
    else:
        print('por favor, digite apenas números!')
    gerar_outro = input('Quer gerar outro?[s/n] ').lower()
    if gerar_outro[0] == 's':
        continue
    else:
        print('--------------------')
        print('programa encerrado!')
        print('--------------------')
        break
    
    
    
    
    


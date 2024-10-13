while True:
    cont = 0
    cont_2 = 0
    vetor_digitos = []
    vetor_onze = [11, 10,  9,  8,  7,  6,  5,  4,  3,  2]
    vetor_dez_primeiros_digitos = []
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
        for j in range(0, 10):
            vetor_dez_primeiros_digitos.append(vetor_digitos[j])
            soma_dos_produtos = vetor_dez_primeiros_digitos[j] * vetor_onze[j]
            cont_2 += soma_dos_produtos
    else:
        print('por favor, digite apenas números!')
    digito_2 = (cont_2 * 10) % 11
    digito_1 = (cont * 10) % 11
    if digito_1 and digito_2 > 9:
        digito_1 = digito_2 = 0
    else:
        digito_1 = digito_1
        digito_2 = digito_2
    
    digito = str(digito_1) + str(digito_2)
    digito_real = cpf[9:]
    if digito_real == digito:
        print('----------------------------------')
        print(f'CPF VÁLIDO!')
        print(f'Os digitos do seu CPF são: {digito}')
        print('----------------------------------')
    else:
        print('----------------------------------')
        print(f'CPF INVÁLIDO!')
        print(f'Os digitos do seu CPF são: {digito_real}. Porém, pelo critério da Receita Federal, deveria ser {digito}.')
        print('----------------------------------')
    
    
    


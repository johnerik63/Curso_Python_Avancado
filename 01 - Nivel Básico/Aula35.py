"""
Calculadors com While

"""
# while True:
#     numero_1 = input('Digite o primeiro número: ')
#     numero_2 = input('Digite o segundo número: ')
#     operador = input('Digite um operador [+, -, *, /]: ')
#     if numero_1.isdigit() or numero_2.isdigit():
#         numero_2 = float(numero_2)
#         numero_1 = float(numero_1)
#         if operador == '+':
#             soma = numero_1 + numero_2
#             print(f'Resultado: {soma}.')
#         elif operador == '-':
#             diferença = numero_1 - numero_2
#             print(f'Resultado: {diferença}.')
#         elif operador == '*':
#             produto = numero_1*numero_2
#             print(f'Resultado: {produto}.')
#         elif operador == '/':
#             quociente = numero_1/numero_2
#             print(f'Resultado: {quociente}.')
#         else:
#             print('Desculpa, não entendi a operação que você deseja!')
#     else:
#         print('Você precisa digitar um número!')
#     sair = input('Quer Sair? [s]sim: ').lower().startswith('s')

#     if sair is True:
#         break

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('o operador digitado está inválidos.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    print('Realizando a sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_2_float + num_1_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else: 
        print('Nunca deveria chegar aqui')

    sair = input('Quer Sair? [s]sim: ').lower().startswith('s')

    if sair is True:
         break

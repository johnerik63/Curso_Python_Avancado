"""
Operador lógico "not" usado para inverter expressões

not True = False
not False = True

"""

senha = input('Senha: ')
if not senha:
    print('você não digitou nada!.')

print(not 0) #imprime True
print(not 1) #imprime False
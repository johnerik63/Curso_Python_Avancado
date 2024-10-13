"""
Operadores Lógicos
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras. Se qualquer valor for falso, a expressão inteira será falso.
Também existe o None que é usado para representar um não valor

"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha_permitida):
    print('Entrar')
elif senha_digitada != senha_permitida:
    print('Senha incorreta!')
else:
    print('Sair')

senha = input('Senha: ') or 'Sem senha'
print(senha)


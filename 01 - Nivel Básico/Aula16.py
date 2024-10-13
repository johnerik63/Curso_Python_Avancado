# if/ elif....../else
#se/ se não se../se não

entrada = input('você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print("Você entrou no sistema")
elif entrada == 'sair':
    print("Você saiu do sistema.")
else:
    print("Desculpe, não entendi!")
print('Fora dos blocos!') # esse código está fora dos blocos condicionais, então ele será executado!
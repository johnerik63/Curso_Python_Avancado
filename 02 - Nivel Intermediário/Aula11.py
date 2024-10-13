#Manipulando chaves em dicionários

pessoa = {}
chave = 'nome_completo'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'



print(pessoa[chave])

pessoa[chave] = 'Marcos'

print(pessoa)

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print("Não Existe!")
else:
    print("Existe!")

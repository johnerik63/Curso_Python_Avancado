# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}

#len retorna a quantidade de chaves do dicionários

print(pessoa.keys()) #retorna as chaves
print(pessoa.values()) #retorna os valores
print(list(pessoa.items())) #retorna os valores
pessoa.setdefault('idade', 25)


for chave, valor in pessoa.items():
    print(chave, valor)
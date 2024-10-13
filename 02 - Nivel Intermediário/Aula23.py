# List comprehension em Python
#List comprehension é uma forma rápida para criar listas a partir de iterávies

# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)

# print(lista)

lista_2 = [num*2 for num in range(10)]
#eu passo um iterável pra minha lista e agora posso trabalhar com lógica dentro dela.
# print(lista_2)

#Mapeamento de dados em List Comprehension
#O mapeamento pega dados de um lado de um iterável e coloca em outra lista 
#e esses doisiteráveis tem o mesmo tamanho

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, }
]

novos_produtos = [
    {**produto, 'preco': produto['preco']* 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos  
]

# print(*novos_produtos, sep='\n')
# print(novos_produtos)

#filtro é algo (if/else) que vem depois do for.

lista = [n for n in range(10) if n < 5]
#inclui algo se a afirmação for verdadeira e não inclui se for falsa 
print(lista)

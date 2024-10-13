lista = ['a', 1, 1.1, True,
          [0, 1, 2], (1, 2), 
          {0, 1}, {'nome': 'Luiz'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))
        
    if isinstance(item, str):
        print(item.upper(), isinstance(item, set))

    if isinstance(item, (int, float)): #(int, float) é um OU
        print(item, item * 2)
        
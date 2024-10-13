"""
Faça uma lista de compas com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de indices existentes na lista.

"""
lista_produtos = []

while True:
    print('------------------------------')
    opcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ").lower()
    print('------------------------------')
    try:
        if opcao[0] == 'i':
            lista_produtos = list(lista_produtos)
            produto = input('Produto: ')
            lista_produtos.append(produto)
            print(f'Produto adicionado: {produto}')
            continue
        else:
            if opcao[0] == 'a':
                if len(lista_produtos) == 0:
                    print('Não temos produtos para apagar!')
                    continue
                else:
                    indice_apagar = input('Escolha o indice do item que deseja apagar: ')
                    indice_apagar = int(indice_apagar)
                    lista_produtos = list(lista_produtos)
                    apagado = lista_produtos.pop(indice_apagar)
                    print(f'Produto apagado: {apagado}')
                    continue
            elif opcao[0] == 'l': 
                if len(lista_produtos) == 0:
                    print('Não temos itens na lista ainda!')
                    continue
                else:
                    lista_produtos = tuple(lista_produtos)
                    print('Sua lista tem os seguintes itens:')
                    for indice, produto_adicionado in enumerate(lista_produtos):
                        print(indice, produto_adicionado)
                        continue
            else:
                print('Digite apenas [i], [a] ou [l].')
                continue
    except:
        print('Você não digitou nada! Por favor escolha algo dentre as opções [i], [a] ou [l].')
        continue
    


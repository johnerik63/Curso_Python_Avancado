"""
EXERCICIO

Peça ao usuário para digitar seu nome e depois sua idade.
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nme tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if nome != '' and idade != '':
    n = int(len(nome) + 1)
    nome_invertido = nome[-1: - n: -1]
    espaco_nome = ' ' in nome
    
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    print(f'Seu nome contém espaços: {espaco_nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios")
        

    

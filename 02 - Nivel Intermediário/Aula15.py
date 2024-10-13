# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0

print('|=======================================|')
print('|        ❓ QUIZ DE PERGUNTAS ❓        |')
print('|=======================================|')

for i in range(len(perguntas)):
    for chave, valor in perguntas[i].items():
        if valor == 'Quanto é 2+2?':
            print(f'{chave}: {valor}')
            print("\n")
            for j, opcao in enumerate(perguntas[0]['Opções']):
                print(f'{j}) {opcao}')
            print("\n")
            resposta = input("escolha uma alternativa: ")
            if resposta.isnumeric():
                resposta = int(resposta)
                if resposta == 4:
                    print("=================================================")
                    print("Meus parabéns!! 🥳🥳🥳 Você acertou..  👏👏👏")
                    print("=================================================")
                    print("\n")
                    acertos += 1
                else:
                    print("=======================================")
                    print("Que pena!😪😪😪 Você errou.. ❎❎❎")
                    print("=======================================")
                    print("\n")
                    erros += 1
            else:
                print("=======================================")
                print("Que pena!😪😪😪 Você errou.. ❎❎❎")
                print("=======================================")
                print("\n")
                erros += 1
        if valor == 'Quanto é 5*5?':
            print(f'{chave}: {valor}')
            print("\n")
            for j, opcao in enumerate(perguntas[1]['Opções']):
                print(f'{j}) {opcao}')
            print("\n")
            resposta = input("escolha uma alternativa: ")
            if resposta.isnumeric():
                resposta = int(resposta)
                if resposta == 25:
                    print("=================================================")
                    print("Meus parabéns!! 🥳🥳🥳 Você acertou..  👏👏👏")
                    print("=================================================")
                    print("\n")
                    acertos += 1
                else:
                    print("=======================================")
                    print("Que pena!😪😪😪 Você errou.. ❎❎❎")
                    print("=======================================")
                    print("\n")
                    erros +=  1
            else:
                print("=======================================")
                print("Que pena!😪😪😪 Você errou.. ❎❎❎")
                print("=======================================")
                print("\n")
                erros += 1
        if valor == 'Quanto é 10/2?':
            print(f'{chave}: {valor}')
            print("\n")
            for j, opcao in enumerate(perguntas[2]['Opções']):
                print(f'{j}) {opcao}')
            print("\n")
            resposta = input("escolha uma alternativa: ")
            if resposta.isnumeric():
                resposta = int(resposta)
                if resposta == 5:
                    print("=================================================")
                    print("Meus parabéns!! 🥳🥳🥳 Você acertou..  👏👏👏")
                    print("=================================================")
                    print("\n")
                    acertos += 1
                else:
                    print("=======================================")
                    print("Que pena!😪😪😪 Você errou.. ❎❎❎")
                    print("=======================================")
                    print("\n")
                    erros += 1
            else:
                print("=======================================")
                print("Que pena!😪😪😪 Você errou.. ❎❎❎")
                print("=======================================")
                print("\n")
                erros += 1
print(f"Você acertou {acertos} de 3 perguntas!", end="") 
if acertos <= 1:
    print("😪")
elif acertos == 2:
    print("😊")
else:
    print("🥳")
print("\n")



        

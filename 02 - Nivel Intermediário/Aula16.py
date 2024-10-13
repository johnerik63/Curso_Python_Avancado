# Exercício - sistema de perguntas e respostas

def acertou_errou(resposta, i):
    print("=================================================")
    frase(resposta, i)
    print("=================================================")
    print("\n")

def frase(resposta, i):
    if resposta == perguntas[i]['Resposta']:
        print("Meus parabéns!! 🥳🥳🥳 Você acertou..  👏👏👏")
    else:
        print("Que pena!😪😪😪 Você errou.. ❎❎❎")

def emoji(acertos):
    emoji = " "
    if acertos <= 1:
        emoji = "😪"
    elif acertos == 2:
        emoji = "😊"
    else:
        emoji = "🥳"
    return print(emoji)

def contagem_acertos_erros(resposta, i, acertos = 0, erros = 0):
    if resposta == perguntas[i]['Resposta']:
        acertou_errou(resposta, i)
    else:
        acertou_errou(resposta, i)
    
perguntas = [
    {   'id': 0,
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {   'id': 1,
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {   'id': 2,
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


print('|=======================================|')
print('|        ❓ QUIZ DE PERGUNTAS ❓        |')
print('|=======================================|')

acertos = 0
erros = 0

for i in range(len(perguntas)):
    if perguntas[i]['id'] == i:
        print("\n")
        print(f'{perguntas[i]['Pergunta']}: ')
        print("\n")
        for j, opcao in enumerate(perguntas[i]['Opções']):
            print(f'{opcao}')
        print("\n")
        resposta = input("escolha uma alternativa: ")
        if resposta == perguntas[i]['Resposta']:
            acertos += 1
        contagem_acertos_erros(resposta, i, acertos = 0, erros = 0)

print(f"Você acertou {acertos} de 3 perguntas!", end=" ")
emoji(acertos) 
print("\n")





        

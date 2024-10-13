"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Após o usuáriio digitar uma letra você vai verificar se els está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se não estiver; Exiba *;

Faça a contagem de tentativas do seu usuário.

"""

palavra_secreta = 'banana'
letras_acertadas = ''
cont = 0

while True:
    print('--------------------------------------------')     
    letra = input('Digite uma letra: ')
    cont += 1
    if len(letra) == 1 or letra == ' ':
        if letra in palavra_secreta:
            letras_acertadas += letra
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print(f'Palavra formada:{palavra_formada}')
        if letra not in palavra_secreta:
            if letra.isnumeric():
                print('Você digitou um número. Digite apenas letras! ')        
    else: 
        print('Você digitou mais de uma letra ou nenhuma. Por Favor, digite apenas uma letra!!')
        continue
    if palavra_formada == palavra_secreta:
        print('--------------------------------------------')      
        print('PARABÉNS! Você Acertou!!!')
        print('A palavra era:', palavra_secreta)
        print('Número de tentativas:', cont)
        print('--------------------------------------------')     
        break

        
























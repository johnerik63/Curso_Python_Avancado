#Exercício: Crie um programa que receba dois valores e analise 
#qual deles é maior exibindo isso na tela.

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

pri = int(primeiro_valor)
si = int(segundo_valor)

if pri > si:
    print(f"O valor {pri} é maior que  {si}")
elif pri < si:
    print(f"O valor {pri} é menor que {si}")
else:
    print("Os valores digitados são iguais")
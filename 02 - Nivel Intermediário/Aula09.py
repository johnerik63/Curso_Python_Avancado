"""
Exercício:
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
faça isso usando o conceito de closure

"""
while True:
    numero = input("Digite um numero inteiro para ver seu dobro, triplo e quádruplo: ")
    numero = int(numero)

    def function(multiplo):
        def numero(numero):
            return numero * multiplo
        return numero

    dobro = function(2)
    triplo = function(3)
    quadruplo = function(4)

    print("----------------------------------------------")
    print(f"O dobro de {numero} é {dobro(numero)}")
    print(f"O triplo de {numero} é {triplo(numero)}")
    print(f"O quadruplo de {numero} é {quadruplo(numero)}")
    print("----------------------------------------------")

    continuar = input("Deseja continuar?[s/n] ").lower()
    if continuar[0] == 's':
        print("\n")
        continue
    else:
        print("\n")
        print("PROGRAMA ENCERRADO!!")
        break






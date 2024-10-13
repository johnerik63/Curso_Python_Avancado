"""
Repetições
while (enquanto)
Execura uma aão enquanto uma condição for verdadeira
loop infinito -> quando um cógigo não tem fim.

"""

#quando a condição é verdadeira, ele entra no while e quando falsa não entra no while.

contador = 0

while contador <= 40:
        contador += 1

        if contador == 6:
                print('não vou mostrar o 6')
                continue
        print(contador)

        if contador == 40:
                break
        
        
print('acabou')
import importlib

import Aula35_m

print(Aula35_m.variavel)

for i in range(10):
    importlib.reload(Aula35_m)
    print(i)


print('Fim')

# O python não importa o módulo apenas uma unica vez. Não adianta você tentar solicitar o impore várias vezes, que ele não faz..

# Caso você queita fazer vários importes (o que não é comuum).. você pode usar a biblioteca importlib com a função importlib.reload()
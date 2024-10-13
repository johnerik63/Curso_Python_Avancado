# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# print(sys.platform)


# partes - from nome_modulo import objeto1, objeto2
from sys import exit, platform

# temos que ter cuidado com os nomes das variáveis e não escolher o mesmo nome das importações.

# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo


# alias 1 - import nome_modulo as apelido
import sys as s

#Podemos dar um apelido para sys.. faço muito isso com pandas 
# import panas as pd
from sys import platform as pf
from sys import exit as ex

print(pf)

# podemos fazer dessa maneira também 



# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex


# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import exit, platform
# tem a desvantagem de importar tudo de dentro do módulo

# print(platform)
# exit()
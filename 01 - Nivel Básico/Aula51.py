"""
Desempacotamento em chamadas de métodos e funções

"""

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [['Maria', 'Helena'], ['Elaine'], ['Luiz', 'joão', 'Eduarda']]

print(*lista)
print(*string)
print(*salas, sep='\n')

#desempacotamento nas chamas das funções
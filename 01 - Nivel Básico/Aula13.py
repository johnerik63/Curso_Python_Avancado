# Strings

nome = 'Pedro Henrique'
altura = 1.68
peso = 78
imc = peso/(altura**2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso}kg, e seu IMC é {imc:.2f}.'

print(linha_1, linha_2)

#Saída: Pedro tem 1.68 de altura pesa 78kg e seu IMC é 27.64
#f-string serve pra formatar texto. f significa formatação.


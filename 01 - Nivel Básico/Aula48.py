"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEE 754
...

"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3) #imprime 0.7999999....
print(f'{numero_3:.2f}') #imprime 0.80
print(round(numero_3, 2)) #imprime 0.8 (float)
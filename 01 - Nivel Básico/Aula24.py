"""
Formatação de Strings 
s - string
d - int
f - float

.<numero de digitos>f
x ou X - Hexadecimal

(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro
= força o numero a aparecer depois do sinal
Sinal - + ou  -
Ex.: 0 > -100, 1f
Conversion flags - !r !s !a

"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.215456984566:0=+10,.1f}')

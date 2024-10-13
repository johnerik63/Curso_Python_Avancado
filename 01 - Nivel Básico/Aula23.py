'''
Interpolação básica de strings 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

'''

#Trata-se de um sistema de numeração posicional que representa os números em base 16, sendo assim, utilizando 16 símbolos. Este sistema utiliza os símbolos 0, 1, 2, 3, 4, 5, 6, 7, 8 e 9 do sistema decimal, além das letras A, B, C, D, E e F.




nome = 'Pedro'
preco = 1000.9854856
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))

#X maiúsculo me da o hexadecimal em maiúsculo
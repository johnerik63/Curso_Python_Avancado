# Função Format

a = 'A'
b = 'B'
c = 1.1
string = 'a = {}, b = {}, c = {:.2f}.'
formato = string.format(a, b, c)
print(formato) # imprime a = A, b = B, c = 1.10.
#Podemos utilizar os indices para não dependermos de colocar na ordem da tupla as variáveis que queremos chamar. 

string = 'b = {1}, a = {0}, c = {2:.2f}.'
formato = string.format(a, b, c) 
print(formato) #imprime b = B, a = A, c = 1.10.

#podemos nomear o parâmetro, mas a partir do momento que nomeamos o parâmetros, podemos chamar ele apenas pelo nome e não mais pelo indice

string = 'b = {1}, a = {0}, c = {nome3:.2f}.'
formato = string.format(a, b, nome3 = c) 
print(formato) #imprime b = B, a = A, c = 1.10.


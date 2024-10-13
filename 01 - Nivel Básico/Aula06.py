"""
Conversão de tipos, coerção type convertion, typecasting, coercion
é o ato de converter um tipo em outro tipos imutáveis e primitivos:
str, int, float, bool (são tipos imutáveis)

"""
print(int('1'), type(int('1'))) # Mudei o tipo de str pra inteiro
print(int('1') + 1)
print(float('1') + 1) # Retorna um float
print(type(float('1') + 1)) 
print(bool(' ')) #True
print(bool('')) #False
print(str(11) + 'b')
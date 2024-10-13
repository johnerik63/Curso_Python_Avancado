# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.
# Criando um set

s1 = set('Luiz')
s1 = set()
s1 = set = {'Luiz', 1, 2, 3} 

#só funciona para valores multaveis

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)

s2 = {1, 2, 4, 5, 6}
for numero in s2:
    print(numero)

# Métodos úteis:
# add, update, clear, discard
s3 = set()
s3.add('Luiz')
s3.update(('Olá Mundo!', 1, 2, 3, 4))
# s3.clear()
s3.discard('Olá Mundo!')
print(s3)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2 #itens que não estão em ambos
print(s3)
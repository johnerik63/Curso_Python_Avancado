import sys

# hasattr, getattr

string = 'Luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe Upper')
    print(getattr(string, metodo)())
    print(string.upper())
else:
    print("Não existe o método digitado")

print(string)

#Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem__iter__e__next

print(next(iterator))

#generator: São funções que sabem pausar. Todo o generator é um iterator mas o contrário não é verdadeiro

lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for i in generator:
    print(i)

#As vantagens da lista é que podemos acessar o indice. Porém ela consome muita memória ao contrário do generator.
#Com o generator não podemos acessar nem tamanho e nem indice.
# Decoradores com parâmetros 

# a fabrica de decoradores pega os parâmetros do decorador, isso é uma tentativa de ter um novo escopo???
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores()(lambda x, y: x*y)
dez_vezes_cinco = multiplica(10, 5)
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
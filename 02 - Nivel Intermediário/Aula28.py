# introdução a generator functions em Python

# generator = (n for n in range(100000))

def generator(n=0):
    yield 1 #pausar
    print('continuando....')
    yield 2 #pausar
    print('Mais uma vez...')
    yield 3 #pausar
    print('Vou terminar!')
    return 'ACABOU'



gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))


for n in gen:
    print(n) #imprime de uma vez

def generator(n=0, maximum=10):
    while True:
        yield n
        if n > maximum:
            return
        n += 1

gen = generator()
for n in gen:
    print(n) #imprime de uma vez
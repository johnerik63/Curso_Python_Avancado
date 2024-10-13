# Métodos em instancias de classes em Python
#Hard codded - Algo escrito diretamente no código.
class Carro:
    def __init__(self, nome = 'sei lá'):
        self.nome = nome #hard coded
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome = 'Celta')
print(celta.nome)
celta.acelerar()




        
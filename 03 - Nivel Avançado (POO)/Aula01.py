"""
class - Classes são moldespara criar novos objetos. As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de Classes.

"""

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Pedro', 'Henrique')
#p1.nome = 'Pedro'
#p1.sobrenome = 'Henrique'

p2 = Pessoa('Marcio', 'Silva')
# p2.nome = 'Marcio'
# p2.sobrenome = 'Silva'


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
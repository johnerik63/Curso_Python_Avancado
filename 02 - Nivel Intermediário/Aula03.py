"""
Escopo de funções em Python
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas npmes do mesmo local podem ser alcançados.
Não temos acessos a nome de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno

"""

x = 1 #normalmente vamos definir a variável antes de definir a função
def escopo():
    #global x
    x = 10
    def outra_funcao():
        #global x
        y = 2
        x = 11
        print(x, y)
    outra_funcao()
    print(x)

escopo()
print(x)
# Try, Except, else e finally

# a = 18
# b = 0
# c = a/b

try:
    a = 18
    b = 0
    print('linha 1'[1000])
    c = a/b
    print('linha 2')
except ZeroDivisionError:
    print('dividiu por zero')
except NameError:
    print('B não está definido')
#podemos colocar uma tupla no exception 
except (IndexError, TypeError) as error:
    print('IndexError + TypeError')
    print('MSG:', error)
    print('Nome', error.__class__.__name__)
#se quisermos saber o erro podemos atribuir error à tupla com o alias
except Exception:
    print('Erro Desconhecido!!')

print('continuar')

"""
Você precisa informar qual erro você ta tratando na exception
Excessão são erros, o certo é colocar o erro no exception para podermos tratar os dados recebidos pelo usuário
O erro máximo é o exception
Como pode-se ver podemos usar vários exceptions para um unico try

"""

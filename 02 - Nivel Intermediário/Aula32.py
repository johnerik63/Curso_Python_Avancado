# raise - lançando exceçõe (erros)

# print(123)
# raise ValueError('Deu Erro')
# # Um erro que lançamos
# print(456)

def divide(n, d):
    try:
        return n/d
    except ZeroDivisionError:
        raise
# isso me da o mesmo erro que o python me daria, é um código redundante
    
# print(divide(8, 0))

def nao_zero(d):
    if d == 0 or d == '0' :
        raise ZeroDivisionError('você ta tentando dividir por zero!')
    True

def divisao(n, d):
    nao_zero(d)
    return n / d
# Lançamos nosso próprio erro

print(divisao(8, '0'))

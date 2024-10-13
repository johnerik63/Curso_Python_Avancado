# try, except, else e finally

try:
    print('Abrir o Arquivo')
    # 8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('Não deu erro!')

finally:
    print('Fechar o Arquivo')

# O finally sempre vai ser executado independente do try e erro que tiver no try.
# Podemos ter tantos except quanto  quisermos 

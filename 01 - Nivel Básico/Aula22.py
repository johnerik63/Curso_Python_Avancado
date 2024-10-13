"""
Operadores IN e NOT IN
Strings são iteraveis 
0.1.2.3.4. (indices positivos)
P.e.d.r.o
-5-4-3-2-1 (indices negativos)
ou seja, você pode navegar em todas as letras da string através dos seus indices

"""

#nome = 'Pedro'

# print(nome[2]) #imprime a letra d
# print(nome[-3]) #imprime a letra d

# print('P' in nome) #True
# print('z' in nome) #False
# print('dro' not in nome) #False
# print('ka' not in nome) #True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

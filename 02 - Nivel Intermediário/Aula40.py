# Funções decoradoras e decoradores 
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções 
# Decoradores são usados para fazer o python usar as funçõe sdecoradoras em outras funções

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('Ok, sua função foi decorada!')
        return resultado
    return interna
    
@criar_funcao
def inverte_instring(string):
    print(f'{inverte_instring.__name__}')
    return string[::-1]

def e_string(param): 
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')



invertida = inverte_instring('123')
print(invertida)





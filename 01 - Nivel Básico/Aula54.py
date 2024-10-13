
#Resolução do Professor:

cpf = '74682489070'
nove_digitos = cpf[0:9]
contador_regressivo = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito)*contador_regressivo
    contador_regressivo -= 1

digito_1 = (resultado_digito_1 * 10) % 11
if digito_1 > 9:
    digito_1 = 0
else:
    digito_1 = digito_1
print('----------------------------------')
print(f'o primeiro digito do CPF é: {digito_1}')
print('----------------------------------')


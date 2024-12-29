# Escopo Global e Local

var_global = 'Curso Completo de Python'

def escreve_texto():
    global var_global
    var_global = 'Bancos de Dados com SQL'
    var_local = "Jarbas Peixoto"
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

print(f'Executa a função escreve_texto()')
escreve_texto()

print('Tentar acessar as variáveis diretamente')
print(f'Variável Global: {var_global}')
#print(f'Variável Local: {var_local}')

# Módulo com funções variadas

# Função que exibe mensagem de boras-vindas:
def mensagem():
    print('Bóson Treinamentos em Tecnologia!\n')

# Função para cálculo de fatoria de um número:
def fatorial(numero):
    if numero < 0:
        return 'Digite um valor maior ou igual à zero'
    else:
        if numero==0 or numero==1:
            return 1
        else:
            return numero * fatorial(numero - 1)
        
# Função para retornar uma série de Fibonacci até # um valor X:
def fibo(n):
    resultado = []
    a, b = 0, 1
    while b <= n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
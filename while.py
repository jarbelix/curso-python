# num = 1
# while (num <= 10000):
#     print(f'{num}, ',end='')
#     num += 1
# print('Laço encerrado!')

nome = None
while (True):
    print('Digite seu nome, ou x para parar: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo, {nome}')
print('Até logo!')
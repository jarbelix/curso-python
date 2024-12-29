import random

# valor = random.randint(1,20)
# print(valor)

# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n=random.randint(1,50)
#     print(f'Número gerado: {n}')

# valor = random.random() # gera um aleatório entre 0 e 1
# print(f'Número gerado: {round(valor*10,2)}')    # aleatório entre 1 e 10 com duas casas decimais

# valor = random.uniform(1,100)
# print(f'Número: {round(valor,4)}')  # entre 1 e 100 com duas decimais

L=[2,4,6,9,10,13,14,16,18,20,21,27,33]
# n=random.choice(L)
# print(f'Número escolhido: {n}') # um aleatório de uma lista

# n = random.sample(L,3)  # três valores da lista L
# print(f'Números escolhidos: {n}')

# Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibí-la:')
n=random.shuffle(L)
print(L)
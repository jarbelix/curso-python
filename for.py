# lista = [2,6,9,4,0,12,3,7]
# for item in lista:
#     print(f'O valor de item = {item}')

# palavra = 'Tiozão'
# for letra in palavra:
#     print(f'O valor da letra = {letra}')

# for numero in range(1,11):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final +1, incremento)
# for x in range(21,2,-3):
#     print(x)

# Tuplas
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamente', 'Turmalina')
for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)

# Compreensões de lista
# Sintaxe
# expressão for item in lista

# criar uma lista de quadrados de outra lista
numeros = [1,4,7,9,10,12,21]

# método utilizando list e map com lambda
quadrados = list(map(lambda num: num**2, numeros))
print(quadrados)

# método utilizando compreensão de lista
quadrados = [num**2 for num in numeros]
print(quadrados)

# criar uma lista de números pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]
print(pares)

# contar qtde de vogais numa frase
frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
vogais = ['a','e','i','o','u','á','é','í','ó','ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase "{frase}" possui {len(lista_vogais)} vogais')

# distributiva entre valores de duas listas
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)

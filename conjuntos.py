# Set são conjuntos (não tem valores duplicados)

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
# print(len(planeta_anao))

# print('Ceres' in planeta_anao)
# print('Lua' not in planeta_anao)

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
print(astros)
astros_set = set(astros)
print(astros_set)

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua', 'Io'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua', 'Cometa Halley'}
print(astros1 != astros2)

# união de conjuntos
print(astros1 | astros2)
print(astros1.union(astros2))

# intersecção de conjuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))

# diferença simétrica
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

# adicionar elementos
astros1.add('Urano')
astros1.add('Sol')
print(astros1)

# remover elementos
astros1.remove('Io')
print(astros1)

# se não existir não dá erro na remoção
astros1.discard('Plutão')
print(astros1)

# remoção aleatoriamente
astros1.pop()
print(astros1)







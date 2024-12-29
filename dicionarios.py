# Dicionários permitem armazenar dados em pares (chaves, valor) - "arrays associativos"

elemento = {
    'z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento)

print(f"Elemento: {elemento['nome']}")
print(f"Densidade: {elemento['densidade']}")
print(f'O dicionário possui {len(elemento)} elementos')

# Atualizar uma entrada
elemento['grupo']='Alcalinos'
print(elemento)

# Adicionar uma entrada
elemento['periodo']=1
print(elemento)

# Exclusão de entrada
del elemento['periodo']
print(elemento)

# # Limpar dicioinario
# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

# Desempacotar itens e chaves
for i, j in elemento.items():
    print(f'{i}: {j}')
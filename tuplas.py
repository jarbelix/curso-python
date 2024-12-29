# Tuplas são imutáveis

tupla = (2,4,6,7,9)
print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(halogenios)
print(len(halogenios))
print(halogenios[3])
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios+gases_nobres
print(elementos)
t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(t1.count(4))

# Slice
print(halogenios[0:2])
print('Cl' in halogenios)
print(sum(t1))

# Operações não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop() por ser IMUTÁVEL

for elemento in elementos:
    print(f'Elemento químico: {elemento}')

groupo17 = list(halogenios)
groupo17[0] = 'H'
print(groupo17)

grupo1 = ['Li', 'Na', 'k', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(sorted(alcalinos))
# Lista: representa uma sequência de valores

# Sintaxe: nome_lista = [valores]

alunos = []

for i in range(2):
    print("Informações do aluno[",i+1,"]:")
    matricula = input("  Matricula: ")
    nota = float(input("  Nota: "))
    aluno = [ matricula, nota ]
    alunos.append(aluno)


for aluno in alunos:
    matricula = aluno[0]
    nota = aluno[1]
    print("O aluno", matricula, "tirou a nota:", nota)
    
#notas = [5,7,8,6,9]
#print(notas)

n1=[4,6,7,8,0,3]
n2=[1,6,3,0,12,11]
valores=n1+n2
valores[0]=9
# #print(valores[-2:])
# print(len(valores))
# print(sorted(valores,reverse=True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

# valores.append(13)
# print(valores)
# valores.pop()
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21)
# print(valores)
# print(12 in valores)


# # Planetas
# planetas=['Mercúrio','Vênus', 'Marte', 'Saturno', 'Urano', 'Neturo']
# for planeta in planetas:
#     print(planeta)

# Crie um script que peça para o usuário digitar o nome
# de 5 bebidas favoritas dele, armazenando esses valores em uma lista
# Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por linna, usando um laço de repetição for.

bebidas=[]
for i in range(5):
    #print(f'Digite uma bebida favorita: ')
    bebida=input(f'Digite uma bebida favorita: ')
    bebidas.append(bebida)

bebidas.sort()
print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)
print('Saude')
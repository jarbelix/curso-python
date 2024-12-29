# nome = 'Curso de Python'
# instrutor = 'Fábio'
# letra = nome[2]
# print(letra)
# print(len(nome))
# print(nome+' com '+instrutor)

# frase = 'Vamos aprender Python hoje.'
# palavras = frase.split()
# print(palavras[1])
# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)

# print(frase[7:19])
# print(frase[-3:])

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)

# usuario=email[0:arroba]
# dominio=email[arroba+1:]

# print(usuario)
# print(dominio)

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste.upper())
# print(objeto_celeste.lower())
# print(objeto_celeste.capitalize())
# print(objeto_celeste.title())

# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio','zinco')
# print(suplemento)
# print(n_suplemento)

## Remoção de 'espaços'
# frase = '    Ômega 3 é bom para a saúde!   '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# ## Alinhamento
# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20,'-'))
# print(fruta.center(20,'-'))

# p = 'Bóson Treinamentos'
# print(p.startswith('Bó'))
# print(p.endswith('tos'))

## Docstrings
texto="""
Geralmente utilizada para documentação
Pode ser inserida dentro de um módulo, função
ou classe no Python, entre outros locais
    Respeita deslocamento do texto e é multilinhas
"""
print(texto)

# Mais sobre manipulação de strings em Python:
# https://docs.python.org/3/library/stdtypes.html#string-methods

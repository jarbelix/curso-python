'''
1. Conceitos Básicos -> OK
2. Estruturas de Controle -> OK
3. Funções -> OK
4. Listas e Dicionários -> OK
5. Trabalhando com Arquivos -> OK (VIDEO INDICADO NO CARD)
6. Tratamento de exceções (try, except)
7. Módulos e Bibliotecas
'''

# TRATAMENTO DE EXCECOES
# try / except / finally
dictPessoas = {
  "nome": "Cícero"
}

try:
  print(dictPessoas["idade"])
except KeyError as e:
  print("Erro ao acessar a chave escolhida!", e)
except Exception as e:
  print("Ocorreu um erro desconhecido!")
finally:
  print("Fim da execução.")
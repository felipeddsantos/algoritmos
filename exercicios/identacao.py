'''

Algoritmos - Identação
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Função para eliminar espaços desnecessários de uma linha
def eliminarEspacos(linha):

  linha_final = ""
  tam_linha = len(linha)

  #Eliminando espaços à esquerda
  for i in range(tam_linha):

    if linha[i] != ' ':

      break

  #Eliminando espaços múltiplos entre palavras
  for j in range(i, tam_linha):

    if linha[j] == ' ' and linha[j - 1] == ' ':

      continue

    linha_final += linha[j]

  #Eliminando um possível espaço no fim da linha
  if linha[j] == ' ':

    linha_final = linha_final[:len(linha_final) - 1]

  return linha_final

#Função para adicionar espaços extras à esquerda de cada linha
def adicionarEspacos(linha, maior_linha):

  return (len(maior_linha) - len(linha)) * ' ' + linha

#Função principal
def identacao():

  texto_final = ""

  while True:

    #Quantidade de linhas do texto atual
    N = int(input())

    #Finaliza se a entrada de linhas for 0
    if N == 0:

      break

    texto_atual = []
  
    #Inserção de todas as linhas do texto atual
    for i in range(N):

      #Eliminação dos espaços desnecessários de cada linha do texto atual e inserção de todas as linhas em uma lista
      texto_atual.append(eliminarEspacos(input()))

    #Obtenção da maior linha do texto atual
    maior_linha = max(texto_atual, key = len)

    #Percorrendo todas as linhas do texto atual e adicionado os espaços à esquerda para completar a identação e concatenando tudo na string final
    for linha in texto_atual:

      texto_final += adicionarEspacos(linha, maior_linha) + '\n'

    #Adicionando quebra de linha entre os textos
    texto_final += '\n'

  #A última linha do texto final possui duas quebras de linha (entre linhas e entre textos). Deve-se eliminar isso
  print(texto_final[:-2])

#Chamando a função principal
identacao()

'''

Algoritmos - O Curinga
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

import re

#Função que recebe um padrão e transforma em expressão regular
def obterExpReg(padrao):

  exp = ""

  #A expressão é construída substituíndo todo curinga por [\w\d.]*, isto é, uma sequência de 0 ou mais símbolos
  for i in range(len(padrao)):

    if padrao[i] == '*':

      exp += "[\w\d.]*"
    
    else:

      exp += padrao[i]
  
  return exp

#Função principal
def curinga():

  while True:

    #Obtendo o padrão da vez
    padrao = input()

    print("ACHOU PARA:", padrao)

    while True:

      #Obtendo o nome do arquivo a ser processado
      try:
    
        arquivo = input()
      
      #Se as entradas acabarem, o programa encerra
      except EOFError:

        exit()

      #Se for obtida uma linha vazia, imprimir linha vazia e receber o próximo padrão
      if arquivo.strip() == "":
      
        print()
        
        break
      
      #Transforma o padrão em uma expressão regular e verifica se o nome do arquivo pode ser obtido através da mesma
      if arquivo in re.findall(obterExpReg(padrao), arquivo):
        
        print(arquivo)

#Chamando a função principal
curinga()

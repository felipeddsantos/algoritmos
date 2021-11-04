'''

Algoritmos - Censo
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from sys import stdin, stdout

#Função principal
def censo():
  
  while True:
  
    #Obtendo linha de configuração e armazenando os valores em uma lista
    linha = stdin.readline().split()
  
    #Se a configuração possui valor zero, encerra
    if linha[0] == '0':

      break
  
    #Obtendo a linha seguinte, isto é, os valores de idades e armazenando em uma lista  
    idades = stdin.readline().split()
  
    #Ordenando as idades
    idades.sort(key = int)
  
    #Deletando as idades abaixo do limite estabelecido
    del(idades[:int(linha[1])])
  
    #Imprimindo todos os valores separados por espaço
    print(" ".join(idades))

#Chamando função principal
censo()

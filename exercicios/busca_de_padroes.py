'''

Algoritmos - Busca de Padrões
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Função principal
def buscaPadroes():

  #Inserindo a quantidade de casos de teste
  k = int(input())

  for i in range(k):

    #Inserindo a string atual
    S = input()

    #Inserindo a quantidade de substrings a serem buscadas em S
    q = int(input())

    for j in range(q):

      #Inserindo a substring atual
      T = input()

      #Se a substring T pertence a S, adiciona 's' na lista resultante. Caso contrário, adiciona 'n'
      if T in S:
        
        print("s")
      
      else:
        
        print("n")

#Chamando a função principal
buscaPadroes()

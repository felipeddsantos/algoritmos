'''

Algoritmos - DNA Periódico
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Função que processa uma cadeia de DNA, retornando seu menor período
def processarCadeia(cadeia):

  subcadeias = []
  tam = len(cadeia)

  #Obtendo subcadeias de DNA de mesmo tamanho e verificando se são iguais, iniciando com subcadeias de comprimento 1, e assim por diante
  for i in range(1, tam):
  
    for j in range(0, tam, i):

      subcadeias.append(cadeia[j:i + j])

    #A primeira vez em que todas as subcadeias de mesmo comprimento forem iguais, a função encontrou o menor período da cadeia de DNA
    if len(set(subcadeias)) == 1:

      #Nesse caso, o período é igual ao comprimento de alguma subcadeia
      return len(subcadeias[0])
  
    subcadeias = []

  #Se nenhum caso for válido, o menor período é o próprio comprimento da cadeia
  return tam
  
#Função principal
def dnaPeriodico():

  #Obtendo quantidade de casos de teste
  N = int(input())

  for i in range(N):

    #Pulando uma linha  
    input()  

    #Obtendo cadeia de DNA da vez
    cadeia = input()

    #Processando cadeia atual e inserindo o resultado na lista atual
    print(processarCadeia(cadeia))
    
    #Imprime linha vazia somente entre resultados
    if i < N - 1:
      
      print()

#Chamando a função principal
dnaPeriodico()

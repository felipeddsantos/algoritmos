'''

Algoritmos - Redundância Proteica
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Função que processa uma sequência, retornando o menor nível de redundância
def processarSeq(seq):

  subseq = []
  tam = len(seq)

  #Obtendo subsequências de mesmo tamanho e verificando se são iguais, iniciando com subsequências de comprimento 1, e assim por diante
  for i in range(1, tam):
  
    for j in range(0, tam, i):

      subseq.append(seq[j:i + j])

    #A primeira vez em que todas as subsequências de mesmo comprimento forem iguais, a função encontrou o menor nível de redundância da sequência
    if len(set(subseq)) == 1:

      #Nesse caso, o menor nível é igual ao comprimento de alguma subsequência
      return len(subseq[0])
  
    subseq = []

  #Se nenhum caso for válido, o menor nível é o próprio comprimento da sequência
  return tam
  
#Função principal
def redundanciaProteica():

  #Obtendo quantidade de casos de teste
  N = int(input())

  for i in range(N):

    #Pulando uma linha  
    input()  

    #Obtendo sequência da vez e eliminando os espaços redundantes
    seq = input().strip()

    #Processando sequência atual e imprimindo o resultado
    print(processarSeq(seq))
    
    #Imprimindo linha vazia somente entre resultados
    if i < N - 1:
      
      print()

#Chamando a função principal
redundanciaProteica()

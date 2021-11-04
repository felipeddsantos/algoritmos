'''

Algoritmos - Lista Telefônica
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Processando uma lista de telefones
def processarTel(tel):

  tam = len(tel)

  for i in range(tam):

    tam1 = len(tel[i])

    for j in range(tam):

      tam2 = len(tel[j])

      if tam1 < tam2:

        if tel[i] == tel[j][0:tam1]:
                
          return False

  return True

#Função principal
def listaTelefonica():

  t = int(input())

  for i in range(t):

    n = int(input())

    tel = list()

    #Colocando todos os telefones de entrada em uma lista
    for j in range(n):

      tel.append(input().strip())

    #Imprimindo "SIM" se a lista de telefones é consistente e "NÃO" caso contrário
    if processarTel(tel):

      print("SIM")
    
    else:

      print("NÃO")

#Chamando função principal
listaTelefonica()

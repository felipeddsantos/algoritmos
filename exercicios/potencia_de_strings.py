'''

Algoritmos - Potência de Strings
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Processando uma string e retornando o maior n tal que s = a^n
def processarString(string):

  tam = len(string)

  lista = list()

  for i in range(tam):

    lista.append(string[i])

    n = int(tam / (i + 1))

    if n * ("".join(lista)) == string:

      return n

  return 1

#Função principal
def potenciaString():

  while True:

    string = input().strip()

    if string == '.':

      break
    
    #Imprimindo o resultado do processamento de cada string de entrada
    print(processarString(string))

#Chamando função principal
potenciaString()

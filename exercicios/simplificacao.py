'''

Algoritmos - Simplificação
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

import re

#Função principal
def simplificacao():

  #Expressão regular responsável pela simplificação
  regex = r"(\w)\1*"

  while True:
  
    #Obtendo o padrão a ser processado
    try:
    
      padrao = input().strip()
      
    #Se as entradas acabarem, o programa encerra
    except EOFError:

      break

    #Obtendo todos os padrões que casam com a expressão, isto é, uma lista contendo os caracteres simplificados. Ao fim, a lista é concatenada e forma-se uma string simplificada
    print("".join(re.findall(regex, padrao)))
            
#Chamando a função principal
simplificacao()

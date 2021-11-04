'''

Algoritmos - IP Detector
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

import re

#Função principal
def ipDetector():

  #Expressão regular para IPs
  regex = r"^(((0{1,3})|(0{0,2}[1-9])|(0{0,1}[1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])).){3}((0{1,3})|(0{0,2}[1-9])|(0{0,1}[1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))(/(([1-2][0-9])|(3[0-1])|([1-9]))){0,1}$"
  
  while True:
  
    #Obtendo o padrão a ser processado
    try:
    
      padrao = input().strip()
      
    #Se as entradas acabarem, o programa encerra
    except EOFError:

      break

    #Verifica se padrão pode ser obtido através da expressão regular
    if bool(re.match(regex, padrao)):
        
      print("IP")
    
    else:

      print("OUTRO")

#Chamando a função principal
ipDetector()

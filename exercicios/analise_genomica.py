'''

Algoritmos - Análise Genômica
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Classe de definição de um nó de uma trie, contendo o valor, a lista de filhos e a quantidade de nós da trie, no caso do nó ser uma raíz
class NoTrie(object):
    
    def __init__(self, valor):
        
        self.valor = valor
        self.filhos = []
        self.qnt_nos = 0

    #Adicionando uma palavra na trie, a partir da raíz
    def adicionarPalavra(self, palavra):
    
        #Começando a adição a partir da raíz
        no_atual = self
    
        #Analisando cada caractere da palavra
        for c in palavra:
        
            #Variável para verificar se o caractere foi encontrado em algum dos filhos do nó atual
            existe_c = False
        
            #O caractere atual é procurado em cada filho do nó atual
            for filho in no_atual.filhos:
            
                #Caso seja encontrado, o nó atual passa a ser o filho e não existe necessidade da criação de um novo nó
                if filho.valor == c:
                
                    no_atual = filho
                    existe_c = True        
                    break
        
            #Se nenhum dos filhos do nó atual contém o valor do caractere da vez, um novo nó com esse valor é criado. Além disso, a quantidade de nós da trie e a lista de filhos do nó atual são incrementadas
            if not existe_c:
            
                novo_no = NoTrie(c)
                no_atual.filhos.append(novo_no)
                no_atual = novo_no
                self.qnt_nos += 1

#Função principal
def analiseGenomica():
    
    #Construindo uma trie
    trie = NoTrie("")

    cadeia = input().strip()

    #Adicionando todos os sufixos da cadeia na trie, construindo uma árvore de sufixos
    for i in range(len(cadeia)):
  
        trie.adicionarPalavra(cadeia[i:])

    #A quantidade de distintas substrings da cadeia é igual a quantidade de nós da árvore de sufixos
    print(trie.qnt_nos)

#Chamado a função principal
analiseGenomica()

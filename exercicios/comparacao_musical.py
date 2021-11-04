'''

Algoritmos - Comparação Musical
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

#Classe de definição de um nó de uma trie, contendo o valor e a lista de filhos
class NoTrie(object):
    
    def __init__(self, valor):
        
        self.valor = valor
        self.filhos = []

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
            
                #Caso seja encontrado, o nó atual passa a ser o filho e não existe necessidade da criação 
                #de um novo nó
                if filho.valor == c:
                
                    no_atual = filho
                    existe_c = True        
                    break
        
            #Se nenhum dos filhos do nó atual contém o valor do caractere da vez, um novo nó com esse valor é criado. Além disso, a quantidade de nós da trie e a lista de filhos do nó atual são incrementadas
            if not existe_c:
            
                novo_no = NoTrie(c)
                no_atual.filhos.append(novo_no)
                no_atual = novo_no
    
    #Calculando a profundidade de uma palavra na trie, a partir da raíz
    def profundidade(self, palavra):
    
        no_atual = self
        prof = 0
    
        #Se a raíz não tem filhos, a trie é vazia. Logo, nenhuma palavra pode ser encontrada
        if not self.filhos:
        
            return prof
    
        #Procurando cada caractere da palavra na trie
        for c in palavra:
        
            encontrado = False
        
            #Procurando o caractere em cada filho do nó atual
            for filho in no_atual.filhos:
            
                #Se o caractere da vez foi encontrado, a procura continua nos filhos do no atual. Nesse caso, a profundidade aumenta em uma unidade
                if filho.valor == c:
        
                    encontrado = True
                    no_atual = filho
                    prof += 1
                    break
        
            #Se o caractere da vez não é encontrado na lista de filhos, a palavra não existe. De qualquer forma, é possível que alguma substring da palavra exista na trie, nesse caso, a profundidade dessa substring é retornada
            if not encontrado:
        
                return prof
    
        return prof

#Função principal
def comparacaoMusical():
    
    #Construção da trie
    trie = NoTrie("")
    
    qnt = 0

    seq1 = input().strip()

    #Adicionando todos os sufixos da primeira sequência na trie, construindo uma árvore de sufixos
    for i in range(len(seq1)):
  
        trie.adicionarPalavra(seq1[i:])
    
    seq2 = input().strip()
    
    #Para cada sufixo de seq2, calculamos a profundidade na árvore de sufixos construída com seq1. Essa profundidade denota a quantidade de substrings do sufixo da vez que existe na árvore, isto é, em seq1. A soma de todas as profundidades denota a quantidade total de substrings de seq2 que existem em seq1.
    for i in range(len(seq2)):
  
        qnt += trie.profundidade(seq2[i:])

    print(qnt)

#Chamado a função principal
comparacaoMusical()

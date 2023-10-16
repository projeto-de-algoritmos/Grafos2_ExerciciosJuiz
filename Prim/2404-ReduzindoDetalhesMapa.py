import sys 

class Celula:
    def __init__(self, noh_destino, custo_aresta):  
        self.noh_conectado = noh_destino           
        self.custo_aresta = custo_aresta            
        self.prox = None                            

class ListaEncadeada:
    def __init__(self):             
        self.prox_cabeca = None     


    def inserir_no_inicio(self, noh, custo):
        nova_celula = Celula(noh, custo)    
        nova_celula.prox = self.prox_cabeca 
        self.prox_cabeca = nova_celula      


    def imprimir(self, noh_origem):
        if self.prox_cabeca is None:                
            print()   
        else:
            celula_atual = self.prox_cabeca         
            while celula_atual is not None:         
                print('{:>2}, ({:>1}), {:>1}'.format(celula_atual.custo_aresta, celula_atual.noh_conectado, noh_origem))
                                
                celula_atual = celula_atual.prox    

class VetorDeListasEncadeadas:
    def __init__(self, tam):    
        self.tamanho = tam      
        self.vetor_LE = [ListaEncadeada() for i in range(tam)] 

class Heap:
    def __init__(self, valor_custo, aresta, noh_de_onde_veio):   
        self.custo = valor_custo                     
        self.aresta = aresta
        self.noh_de_onde_veio = noh_de_onde_veio 

class Hash:
    def __init__(self, posicao):                
        self.posicao = posicao                

class VetorHeap:
    def __init__(self, tam):        
        self.tamanho_heap = tam          
        self.tamanho_hash = tam          
        self.vetor_heap = [Heap(0, 0, 0) for i in range(tam+1)] 
        self.vetor_hash = [Hash(0) for i in range(tam+1)] 
                                    
    
    def imprimir_heap(self):
        for i in range(1, self.tamanho_heap + 1):
            print(f'{self.vetor_heap[i][0]}, {self.vetor_heap[i][1]}')
        return 

   
    def imprimir_hash(self):
        for i in range(1, self.tamanho_hash + 1):
            print(f'{i} - {self.vetor_hash[i]}')
        return 
    
    def inicializar_heap(self, qtde_nohs):
        for j in range(1, qtde_nohs+1):
            self.vetor_hash[j] = j
        for i in range(1, qtde_nohs+1):
            self.vetor_heap[i] = [sys.maxsize, chr(i+64)+chr(i+64), i]
        return

    def inserir_no_heap(self, valor_custo, aresta, noh_onde_esta):
        indice_inserir = self.vetor_hash[noh_onde_esta]
        if self.vetor_heap[indice_inserir][0] > valor_custo:
            self.vetor_heap[indice_inserir] = [valor_custo, aresta]
        else:
            return
        self.shift_up_no_heap(indice_inserir)
        return

    def shift_up_no_heap(self, indice_shift):
       
        pai = indice_shift // 2
        if pai == 0:
            return
        elif self.vetor_heap[indice_shift][0] < self.vetor_heap[pai][0]:
          
            self.vetor_heap[indice_shift], self.vetor_heap[pai] = self.troca(self.vetor_heap[indice_shift], self.vetor_heap[pai])
            indice = ord(self.vetor_heap[indice_shift][1][1:])-64
            indice_pai = ord(self.vetor_heap[pai][1][1:])-64
            self.vetor_hash[indice] = indice_shift
            self.vetor_hash[indice_pai] = pai
            indice_shift = pai
            self.shift_up_no_heap(indice_shift)
        else:
            return

    def troca(self, origem, destino):
        aux = origem
        origem = destino
        destino = aux
        return origem, destino

    def reorganizar_heap(self, indice_reorganizar):
        self.vetor_heap[indice_reorganizar][0] = sys.maxsize
        self.heapify_no_heap(indice_reorganizar)
        return
        
    def heapify_no_heap(self, indice_heapify):
        if (indice_heapify * 2) > self.tamanho_heap:
            return
        filho_esquerdo = indice_heapify * 2
        filho_direito = (indice_heapify * 2) + 1
        if (indice_heapify * 2) + 1 <= self.tamanho_heap:
            if self.vetor_heap[filho_esquerdo][0] < self.vetor_heap[filho_direito][0]:
                menor_dos_dois_filhos = filho_esquerdo
            else:
                menor_dos_dois_filhos = filho_direito
        else:
            menor_dos_dois_filhos = filho_esquerdo
        if (self.vetor_heap[indice_heapify][0] > self.vetor_heap[menor_dos_dois_filhos][0]):
            self.vetor_heap[indice_heapify], self.vetor_heap[menor_dos_dois_filhos] = self.troca(self.vetor_heap[indice_heapify], self.vetor_heap[menor_dos_dois_filhos])
            indice = ord(self.vetor_heap[indice_heapify][1][1:])-64
            indice_menor_filho = ord(self.vetor_heap[menor_dos_dois_filhos][1][1:])-64
            self.vetor_hash[indice] = indice_heapify
            self.vetor_hash[indice_menor_filho] = menor_dos_dois_filhos
            indice_heapify = menor_dos_dois_filhos
            self.heapify_no_heap(indice_heapify)
        else:
            return

    def prim_com_heap(self, noh_escolhido, qtde_nohs, custo_total):

            if grafo.vetor_LE[noh_escolhido].prox_cabeca is not None:           
                prox_noh_vizinho = grafo.vetor_LE[noh_escolhido].prox_cabeca        
                while prox_noh_vizinho is not None:             
                    if conjunto_S[prox_noh_vizinho.noh_conectado] is None:
                        self.inserir_no_heap(prox_noh_vizinho.custo_aresta, 
                                                chr(noh_escolhido+64) + chr(prox_noh_vizinho.noh_conectado+64), prox_noh_vizinho.noh_conectado)
                    prox_noh_vizinho = prox_noh_vizinho.prox                           
            
            menor_custo = self.vetor_heap[1][0]
            aresta_escolhida = self.vetor_heap[1][1]
            noh_que_vai_para_S = self.vetor_heap[1][1][1:]
            noh_escolhido = ord(noh_que_vai_para_S)-64
            if (conjunto_S[noh_escolhido] is not None):
                conjunto_S[noh_escolhido] = noh_que_vai_para_S
                arestas_T.append(aresta_escolhida)
            else:
                conjunto_S[noh_escolhido] = noh_que_vai_para_S
                arestas_T.append(aresta_escolhida)
            self.reorganizar_heap(1)
            custo_total = custo_total + menor_custo
        
            if len(arestas_T) == qtde_nohs-1:
                return custo_total
            else:
                return self.prim_com_heap(noh_escolhido, qtde_nohs, custo_total)

if __name__ == "__main__":

        N, M = input().split()
        N_qtd_nohs = int(N)
        M_qtd_arestas = int(M)
        noh_inicial = 1
        grafo = VetorDeListasEncadeadas(N_qtd_nohs + 1)

        for i in range(1, M_qtd_arestas + 1):
            noh_origem, noh_destino, custo_aresta = input().split()
            grafo.vetor_LE[int(noh_origem)].inserir_no_inicio(int(noh_destino), int(custo_aresta))
            grafo.vetor_LE[int(noh_destino)].inserir_no_inicio(int(noh_origem), int(custo_aresta))

        conjunto_S = [None] * (N_qtd_nohs + 1)
        conjunto_S[noh_inicial] = chr(noh_inicial+64)
        arestas_candidatas = VetorHeap(N_qtd_nohs)  
        arestas_candidatas.inicializar_heap(N_qtd_nohs)
        arestas_T = []
        noh_escolhido = noh_inicial
        custo_total = 0
        custo_total = arestas_candidatas.prim_com_heap(noh_escolhido, N_qtd_nohs, custo_total)
        print(custo_total)

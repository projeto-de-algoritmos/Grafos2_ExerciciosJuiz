def iniciarLista(N):
    global C                    
    C = [0]*N
    for i in range(N):
        C[i] = i

def encontrar(i):               
    global C                    
    if (C[i] == i):
        return i
    C[i] = encontrar(C[i])
    return C[i]

def comparar(i, j):                       
    return encontrar(i) == encontrar(j)   

def unir(i, j):                        
    C[encontrar(i)] = encontrar(j)

while True:                                             

    x, y = map(int, input().split())                    

    if (x == 0 and y == 0):
        break
    
    Lista = []

    custo_iluminacao = 0                                

    for i in range(y):                                  
        a, b, custo = map(int, input().split())        
        Lista.append((custo, (a, b)))
        custo_iluminacao = custo + custo_iluminacao
    
    Lista.sort()                                                                        

    custo_total = 0
    iniciarLista(x)                                     
    
    for i in range(y):                                  
        custo, (a, b) = Lista[i]                        
        
        if not comparar(a, b):
            unir(a, b)                                 
            
            custo_total += custo                       
    
    print(custo_iluminacao - custo_total)               
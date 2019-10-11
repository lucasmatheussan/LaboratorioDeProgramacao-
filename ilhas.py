import copy
linha1 = input().split(" ")
dicl = {}
for i in range(1,int(linha1[0]) +1):
  dicl[str(i)]={}
for i in range(1,int(linha1[1])+1):
    p,q,d = input().split(" ")
    dicl[p][q] = int(d)
    dicl[q][p] = int(d)
servidor = input("")
def MenorCaminho(a,grafo):
    distancia_curta = {}
    copia_grafo = copy.deepcopy(grafo)
    for n in grafo: # Faz todos os nós ter um valor no infinito
        distancia_curta[n] = float("Inf")
    distancia_curta[a] = 0 #Escolhe um para ser o valor meno, que nosso caso vai ser a cidade a
    while copia_grafo: # Realizei a copia do grafo, para não perde os dados dela, pois vamos retirar dele alguns elementos
        Menor = None
        for p,n in copia_grafo.items():
          if():
            if Menor == None:
                Menor = n
            elif(distancia_curta[n] < distancia_curta[Menor]):
                Menor = n
        for vizinho, peso in grafo[Menor].items():
            if(peso + distancia_curta[Menor] < distancia_curta[vizinho]):
                distancia_curta[vizinho] = peso + distancia_curta[Menor]
        copia_grafo.pop(Menor)
    print(distancia_curta) # menor distancia possivel
for i in range(0,len(dicl)+1):
    MenorCaminho(str(i),dicl)

#usando o algoritmo de dasjkin para percorrer o menor caminho, como pode ir de um caminho ao outro, mas com algumas mudanças.

def MenorCaminho(a,b,grafo):
    distancia_curta = {}
    copia_grafo = grafo
    for n in grafo: # Faz todos os nós ter um valor no infinito
        distancia_curta[n] = float("Inf")
    distancia_curta[a] = 0 #Escolhe um para ser o valor meno, que nosso caso vai ser a cidade a
    while copia_grafo: # Realizei a copia do grafo, para não perde os dados dela, pois vamos retirar dele alguns elementos
        Menor = None
        for n in copia_grafo:
            if Menor == None:
                Menor = n
            elif(distancia_curta[n] < distancia_curta[Menor]):
                Menor = n
        for vizinho, peso in grafo[Menor].items():
            if(peso + distancia_curta[Menor] < distancia_curta[vizinho]):
                distancia_curta[vizinho] = peso + distancia_curta[Menor]
        copia_grafo.pop(Menor)
    print(distancia_curta[b]) # menor distancia possivel

dic = {}
n,a,b = input().split(" ")
for i in range(int(n)+1):
    dic[str(i)] = {}
for i in range(1,int(n)):
    p,q,d = input().split(" ")
    dic[p][q] = int(d)
    dic[q][p] = int(d)
MenorCaminho(a,b,dic)

class ColorindoMapa():
    def __init__(self):
        self.grafo_colorido = {}
        self.grafo = {}
        self.cor = ["Azul", "Preto","Vermelho","marrom"]
    #set as cores que deseja colorir (OPCIONAL)
    def setCores(self,cor):
        self.cor = cor.split(";")
    #Vai realizar o set de cada estado e seus vizinhos
    def setGrafos(self,grafo, vizinhos):
        self.grafo[grafo] = vizinhos.split(";")
        self.grafo_colorido[grafo] = ""
    #Realiza a verificação da cor do vizinho
    def VerificarACorDoVizinho(self,cor, vizinhos):
        for i in vizinhos:
            if(self.grafo_colorido[i]==cor):
                return False
        return True
    #Processo de escolha de cor de cada estado
    def EscolherCor(self):
       for p, i in self.grafo.items():
           for k in self.cor:
               respota = self.VerificarACorDoVizinho(k,i)
               if(respota == True):
                   self.grafo_colorido[p] = k
                   break
    def Contagem(self):
        lista = []
        for i in self.grafo_colorido.values():
                if(i not in lista):
                    lista.append(i)
        return len(lista)

teste = ColorindoMapa()
estados = input("Digite o nome dos estados seprado por ; : ").lower().split(";")
for k in estados:
    vizinhos = input("Digite os vizinhos do estado %s seprado por ; " % k).lower()
    teste.setGrafos(k,vizinhos)
teste.EscolherCor()
print(teste.grafo_colorido)
print("Foram utilizidas %d cores"%teste.Contagem())

class RL2():
    def __init__(self):
        self.lista = []

    def setListaDeComandos(self,comandos):
        self.lista = [x for x in comandos]

    def Processamento(self):
        lista_copia = self.lista[::]
        if ("f" in self.lista and "t" in self.lista):
            for i in lista_copia:
                if "t" == i and "f" in self.lista:
                  self.lista.remove("t")
                  self.lista.remove("f")
                elif "t" == i and "f" not in self.lista:
                    break
        return len(self.lista)

teste = RL2()
entrada = input().lower()
teste.setListaDeComandos(entrada)
resultado = teste.Processamento()
print("%d metro(s) de distância  entre a posição inicial e a posição final do robô RL2" % resultado)





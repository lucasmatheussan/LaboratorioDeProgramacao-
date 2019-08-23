# Mapa

## Problema
Dado um mapa plano, dividido em regiões, qual o número mínimo de cores que são necessárias para colorir cada província com uma cor diferente, de
modo que duas províncias vizinhas não tenham a mesma cor?

## Solução

Usando o teorema de quatros cores, Quatro cores são suficientes para pintar qualquer mapa plano. Mas note-se que, ao dizer-se
que quatro cores são suficientes para qualquer mapa, isto não significa que sejam necessárias para cada mapa. Isto é, no máximo
são precisas quatro cores. Por exemplo, se considerarmos um tabuleiro de xadrez como sendo um mapa, e cada "casa" do tabuleiro 
representar um país, então a coloração habitual de um tabuleiro de xadrez mostra-nos que, nesse caso, bastam apenas duas cores. [Veja mais aqui](https://www.atractor.pt/matviva/geral/t5cores/index.htm)

## Implementação
Na implementação escolhi a linguagem python, primeiro criei uma class e seu construtor. Iniciamos no construtor a lista **cor** ( Que vai ser a cores a serem utilizadas, podendo ser mudado caso seja da escolha) e dois dicionários **grafo** (Que tem como estrutura como exemplo ```{"regiao":["viznho1", "vizinho2"]}```) que vai ter a entrada do usuário e **grafo_colorido**(Tendo como exemplo de estrutura ``` {"regiao":"azul"}```)  que vai ser o grafo já colorido. 

```
class ColorindoMapa():
    def __init__(self):
        self.grafo_colorido = {}
        self.grafo = {}
        self.cor = ["Azul", "Preto","Vermelho","marrom"]
```
Se for escolher as cores a serem utilizadas de forma manual, é importante saber que a ordem do elemento da lista vai ser sua prioridade para as cores a serem mais utilizadas . A função ```setCores``` recebe uma lista de cor como parâmetro.  
```
  def setCores(self,cor):
        self.cor = cor.split(";")
```

A função ```setGrafos``` realiza a inserção da região como KEY no dicionário  **grafo** e uma lista de vizinhos como seus valores. Além de criar as keys do dicionário **grafo_colorido**. 

```
    def setGrafos(self,grafo, vizinhos):
        self.grafo[grafo] = vizinhos.split(";")
        self.grafo_colorido[grafo] = ""
 ```
A função abaixo é responsável por receber como parâmetros uma cor e seus vizinhos de certa região, Nisso vai ser rodado um ```for``` para saber se alguns dos vizinhos tem a mesma cor, caso sim retorna ```False``` caso ninguém  tenha  retorna ```True```.

```
   def VerificarACorDoVizinho(self,cor, vizinhos):
        for i in vizinhos:
            if(self.grafo_colorido[i]==cor):
                return False
        return True
```
A função ```EscolherCor``` é responsável por escolher a cor de cada região e chamar a função ``` VerificarACorDoVizinho ``` para verificar as cores de seus vizinhos e gerar o dicionário **grafo_colorido** com seu resultado.  

```
    def EscolherCor(self):
       for p, i in self.grafo.items():
           for k in self.cor:
               respota = self.VerificarACorDoVizinho(k,i)
               if(respota == True):
                   self.grafo_colorido[p] = k
                   break
```

A Função ```Contagem``` é responsável por contar quantas cores foram utilizadas durante o processo de coloração do mapa.

```
def Contagem(self):
        lista = []
        for i in self.grafo_colorido.values():
                if(i not in lista):
                    lista.append(i)
        return len(lista)
``

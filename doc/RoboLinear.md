# Robô Linear
RL2 é um robô que se move apenas em linha reta, sobre um trilho. Ele é utilizado dentro de uma
fábrica para realizar diversas tarefas, como distribuir peças e ferramentas para os trabalhadores.

O RL2 é comandado utilizando uma linguagem de programação que tem apenas dois comandos:

- F: ao receber esse comando, o robô move-se 1 metro para a frente;
- T: ao receber esse comando, o robô move-se 1 metro para trás;

Após receber e executar um comando, o robô permanece parado até receber o próximo comando.

## Problema 
Implementar um algoritmo que desmotre sequência de comandos para saber a distância em metros entre a posição inicial e a posição final do robô.

## Resolução

Usando um conceito semelhante ao de pilha de estrutura de dados, vamos resolver esse problema removendo algumas caracteres da entrada recebida e seu tamanho final, vai ser sua distância que foi percorrido. 

Primeiro foi realizado a criação da classe RL2 e seu construtor, iniciamos a lista ```self.lista = []``` onde vai ser armazenada os comandos que usuário digitar. E a função ```def setListaDeComandos``` realiza a inserção dos comandos na variável lista. 

```
class RL2():
    def __init__(self):
        self.lista = []

    def setListaDeComandos(self,comandos):
        self.lista = [x for x in comandos]
```

A função responsável por realizar o processo de verificar a distância percorrida pelo robô é ```def Processamento```, usando uma teoria semelhante a de pilha, porém aqui vai retirado os primeiras linhas inseridas. Caso os comandos ```F``` e ```T``` esteja juntos na entrada, a função vai retirar um de cada comando da lista até ficar somente um tipo de comando e resultado vai ser o tamanho da lista.

```
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

```


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

Usando um conceito semelhante ao de pilha de estrutura de dados, vamos resolver esse problema removendo algumas caracteres da entrada recebida e seu tamanho final, vai ser sua distancia que foi percorrido. 

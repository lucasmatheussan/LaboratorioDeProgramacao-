def Corte(pedacos):
 lista = []
 for i in range(len(pedacos)):
   lista.append(teste(pedacos,pedacos[i]))
 return max(lista)

def teste(pedacos,corte):
  total = 1
  for p,i in enumerate(pedacos):
    if(corte > i):
      try:
        if(pedacos[p+1]-corte >= 0):
            total += 1
        continue
      except:
        continue
    if(total == 1):
      total += 1
  return total
n = input()
pedacos = input("")
pedacos = list(map(int, pedacos.split(" ")))
print(Corte(pedacos))

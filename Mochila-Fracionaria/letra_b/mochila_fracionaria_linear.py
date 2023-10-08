from select_pivot_v1 import select_pivot_v1
from partition_v1 import partition_v1

def fractional_knapsack_linear(obj, sumOfWeights, maximumCapacity):
  size=len(obj)

  # Caso a soma de todos os pesos da mochila seja menor que a capacidade maxima posso colocar todos os item dentro da mochila
  if sumOfWeights <= maximumCapacity:
    k = size - 1
  else: #Caso não seja chamos o partionAndFindK
    k = partitionAndFindK(obj, 0, size-1, maximumCapacity)

  totalVal = 0.0
  totalW = 0

  # Fazemos a soma de todos os pesos até k-1 por que o range do python funciona assim
  for i in range(k):
    obj[i] = (obj[i][0], obj[i][1], 1.0)
    totalVal += obj[i][0]
    totalW += obj[i][1]

  #Aqui pegamos só a parte fracionaria do k-esimo elemento (Colocamos na mochila uma fração desse objeto)
  obj[k] = (obj[k][0], obj[k][1], min(1.0, (maximumCapacity - totalW) / obj[k][1]))
  totalVal += obj[k][2] * obj[k][0]

  return totalVal


def partitionAndFindK(obj, start, end, maximumCapacity):
  #Selecionando pivot
  pivot = select_pivot_v1(obj, start, end)

  #Colocando pivô no fim do array
  obj[end], obj[pivot] = obj[pivot], obj[end]

  # Particionando o array em tono deste pivô
  [sumW, pivot] = partition_v1(obj, start, end)

  # Verificamos se o soma de pesos até o piso - 1 cabe na mochila por completo
  if sumW >= maximumCapacity and (sumW - obj[pivot][1]) <= maximumCapacity:
    return pivot
  elif sumW < maximumCapacity:
    # Chamamos o partitionAndFindK para a parte superior ao pivô
    return partitionAndFindK(obj, pivot + 1, end, maximumCapacity - sumW)
  
  # Chamamos a partitionAndFindK para a parte inferior ao pivô
  return partitionAndFindK(obj, start, pivot - 1, maximumCapacity)
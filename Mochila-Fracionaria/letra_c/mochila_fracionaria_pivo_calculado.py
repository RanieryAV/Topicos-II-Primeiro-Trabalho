from select_pivot_v2 import select_pivot_v2
from partition_v2 import partition_v2

def fractional_knapsack_pivot_calculation(obj, sumOfWeights, maximumCapacity):
  size=len(obj)

  if sumOfWeights <= maximumCapacity:
    k = size - 1
  else:
    k = partitionAndFindK(obj, 0, size-1, maximumCapacity)

  totalVal = 0.0
  totalW = 0

  for i in range(k):
    obj[i] = (obj[i][0], obj[i][1], 1.0)
    totalVal += obj[i][0]
    totalW += obj[i][1]

  obj[k] = (obj[k][0], obj[k][1], min(1.0, (maximumCapacity - totalW) / obj[k][1]))
  totalVal += obj[k][2] * obj[k][0]

  return totalVal


def partitionAndFindK(obj, start, end, maximumCapacity): 
  #Selecionando pivot
  pivot = select_pivot_v2(obj, start, end)

  # Particionando o array em tono deste pivô
  [sumW, pivot] = partition_v2(obj, start, pivot)

  # Verificamos se o soma de pesos até o piso - 1 cabe na mochila por completo
  if sumW >= maximumCapacity and (sumW - obj[pivot][1]) <= maximumCapacity:
    return pivot
  elif sumW < maximumCapacity:
    # Chamamos o partitionAndFindK para a parte superior ao pivô
    return partitionAndFindK(obj, pivot + 1, end, maximumCapacity - sumW)
  
  # Chamamos a partitionAndFindK para a parte inferior ao pivô
  return partitionAndFindK(obj, start, pivot - 1, maximumCapacity)
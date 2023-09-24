from select_pivot import select_pivot
from partition import partition

def fractional_knapsack_linear(obj, sumOfWeights, maximumCapacity):
  size=len(obj)

  if sumOfWeights <= maximumCapacity:
    k = size - 1
  else:
    k = partitionAndFindK(obj, 0, size, maximumCapacity)

  totalVal = 0.0
  totalW = 0

  for i in range(k):
    obj[i] = (obj[i][0], obj[i][1], 1.0)
    totalVal += obj[i][0]
    totalW += obj[i][1]

  obj[k] = (obj[k][0], obj[k][1], min(1.0, (maximumCapacity - totalW) / obj[k][1]))
  totalVal += obj[k][2] * obj[k][0]

  return totalVal


def partitionAndFindK(obj, ini, fim, W):
  print("ini", ini)
  print("fim", fim)
  print("-----")
  print("\n")
  pivot = select_pivot(obj, ini, fim)
  [sumW, pivot] = partition(obj, pivot)

  print(pivot)
  print(obj)
  print(sumW)
  print("here", W)
  print("----")
  print("\n")



  if sumW >= W and (sumW - obj[pivot][1]) <= W:
    return pivot
  elif sumW < W:
    return partitionAndFindK(obj, pivot + 1, fim, W - sumW)
  
  return partitionAndFindK(obj, ini-2, pivot - 1, W)
def partition(obj, pivotIndex):
  size = len(obj)

  for i in range(size):
    obj[i] = (obj[i][0], obj[i][1], obj[i][0] / obj[i][1])

  pivot = obj[pivotIndex][2]

  middle = 0

  for index in range(size):
    if(obj[index][2] > pivot):
      obj[index], obj[middle] = obj[middle], obj[index]
      middle += 1

  obj[middle], obj[pivotIndex] = obj[pivotIndex], obj[middle]

  soma = 0

  for i in range(0, middle+1):
    soma += obj[i][1]

  return (soma, middle)
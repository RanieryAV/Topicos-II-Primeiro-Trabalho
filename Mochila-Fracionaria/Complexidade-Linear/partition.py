def partition(obj, start, end, pivotIndex):
  for i in range(start, end):
    obj[i] = (obj[i][0], obj[i][1], obj[i][0] / obj[i][1])

  pivot = obj[pivotIndex][2]

  middle = start

  for index in range(start, end):
    if(obj[index][2] > pivot):
      obj[index], obj[middle] = obj[middle], obj[index]
      middle += 1

  obj[middle], obj[pivotIndex] = obj[pivotIndex], obj[middle]

  soma = 0

  for i in range(start, middle+1):
    soma += obj[i][1]

  return (soma, middle)
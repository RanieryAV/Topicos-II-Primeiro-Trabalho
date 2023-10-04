def partition(obj, start, end):
  pivotIndex = end
  pivot = obj[pivotIndex][0] / obj[pivotIndex][1]

  middle = start

  for index in range(start, end+1):
    currentReason = obj[index][0] / obj[index][1]
    
    if(currentReason > pivot):
      obj[index], obj[middle] = obj[middle], obj[index]
      middle += 1

  obj[middle], obj[pivotIndex] = obj[pivotIndex], obj[middle]

  soma = 0

  for i in range(start, middle+1):
    soma += obj[i][1]

  return (soma, middle)
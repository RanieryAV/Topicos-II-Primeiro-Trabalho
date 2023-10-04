def partition(obj, start, pivot):
  middle = start

  for index in range(start, len(obj)):
    currentReason = obj[index][0] / obj[index][1]
    
    if(currentReason > pivot):
      obj[index], obj[middle] = obj[middle], obj[index]
      middle += 1


  if(middle == start):
    return (obj[middle][1], middle)
  
  soma = 0

  for i in range(start, middle):
    soma += obj[i][1]

  return (soma, middle-1)
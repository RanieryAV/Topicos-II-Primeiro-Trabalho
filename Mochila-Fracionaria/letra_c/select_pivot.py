def select_pivot(obj, start, end):
  if(start > end):
    return obj[start][0]/obj[start][1]
  
  totalSum = 0
  size = (end - start) + 1

  for index in range(start, end+1):
    totalSum += obj[index][0]/obj[index][1]

  return totalSum/size
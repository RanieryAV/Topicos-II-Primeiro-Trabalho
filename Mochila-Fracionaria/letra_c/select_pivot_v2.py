def select_pivot_v2(obj, start, end):
  # Caso em que só existe um elemento no array maior que pivô
  if(start > end):
    return obj[start][0]/obj[start][1]
  
  # Armazena a soma total da razões
  totalSum = 0
  # Armazena o tamnho do arranjo
  size = (end - start) + 1

  for index in range(start, end+1):
    totalSum += obj[index][0]/obj[index][1]

  # retorna a media
  return totalSum/size
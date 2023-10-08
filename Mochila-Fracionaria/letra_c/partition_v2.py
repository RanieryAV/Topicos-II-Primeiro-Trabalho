def partition_v2(obj, start, pivot):
  # Guarda o ultimo item maior que o pivot
  middle = start

  # Percorre sobre todos os items
  for index in range(start, len(obj)):
    currentReason = obj[index][0] / obj[index][1]
    
    # Se a razão for maior que o pivot troca ela de posição com middle e incrementa
    if(currentReason > pivot):
      obj[index], obj[middle] = obj[middle], obj[index]
      middle += 1

  # Caso o maior elemento ja seja o middle
  if(middle == start):
    return (obj[middle][1], middle)
  
  soma = 0

  # Soma todos os pesos até o pivô
  for i in range(start, middle):
    soma += obj[i][1]

  return (soma, middle-1)
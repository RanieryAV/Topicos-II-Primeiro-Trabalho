def partition_v1(obj, start, end):
  # Pegamos o index do pivô
  pivotIndex = end

  # pegamos a valor do pivô
  pivot = obj[pivotIndex][0] / obj[pivotIndex][1]

  # Esta variavel marca onde o pivô deve ficar
  middle = start

  # Percorrendo todos os items do array
  for index in range(start, end+1):
    # Salvamos a razão valor/peso do item
    currentReason = obj[index][0] / obj[index][1]
    
    # Verificamos de ele é maior que o pivô
    if(currentReason > pivot):
      # Colocamos este item na posição middle (que na primeira iteração esta no inicio do array)
      obj[index], obj[middle] = obj[middle], obj[index]

      # Incrementamos middle
      middle += 1

  # Por fim colocamos o pivô que estava no fim do array no lugar correto
  obj[middle], obj[pivotIndex] = obj[pivotIndex], obj[middle]

  # Aqui realizamos a soma do pesos até o pivô
  soma = 0

  for i in range(start, middle+1):
    soma += obj[i][1]

  return (soma, middle)
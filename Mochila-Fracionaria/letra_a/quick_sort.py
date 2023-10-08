import random

def partition(arr, low, high):
  # Escolha um pivô aleatório
  pivot_index = random.randint(low, high)
  arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
  pivot = arr[high]

  i = low - 1

  for j in range(low, high):
    # Comparando as razões entre as tuplas
    if arr[j][0] / arr[j][1] >= pivot[0] / pivot[1]:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quickSort(arr, low, high):
  if low < high:
    pivotIndex = partition(arr, low, high)
    quickSort(arr, low, pivotIndex - 1)
    quickSort(arr, pivotIndex + 1, high)


from merge_sort import mergeSort
from quick_sort import quickSort

def fractionalKnapsack(W, arr):
  # mergeSort(arr, 0, len(arr)-1)
  quickSort(arr, 0, len(arr)-1)

  # arr.sort(key=lambda x: (x[0]/x[1]), reverse=True)
  finalvalue = 0.0

  test=W

  for item in arr:
    if item[1] <= test:
      test -= item[1]
      finalvalue += item[0]
    else:
      finalvalue += item[0] * test / item[1]
      break

  return finalvalue

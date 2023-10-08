from merge_sort import mergeSort

def fractionalKnapsack(W, arr):
  mergeSort(arr)
  # arr.sort(key=lambda x: (x[0]/x[1]), reverse=True)
  
  finalvalue = 0.0

  width=W

  for item in arr:
    if item[1] <= width:
      width -= item[1]
      finalvalue += item[0]
    else:
      finalvalue += item[0] * width / item[1]
      break

  return finalvalue

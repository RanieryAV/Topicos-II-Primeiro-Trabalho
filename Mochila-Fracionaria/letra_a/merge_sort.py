def mergeSort(arr):
  if len(arr) > 1:

    mid = len(arr)//2

    L = arr[:mid]

    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i][0] / L[i][1]  >= R[j][0]/R[j][1]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    # Checking if any element was left
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

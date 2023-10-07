def fractionalKnapsack(W, arr):
  arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
  finalvalue = 0.0

  for item in arr:
    if item.weight <= W:
      W -= item.weight
      finalvalue += item.profit
    else:
      finalvalue += item.profit * W / item.weight
      break

  return finalvalue

def fractional_knapsack(weights, values, maximumCapacity):
  size = len(weights)
  f = [0.0 for i in range(size)]
  capacity = maximumCapacity
  
  reason = []

  for index in range(size):
    reason.append(round(values[index]/weights[index], 2))

  for index in range(1, size):
    if(capacity >= weights[index]):
      f[index] = 1
      capacity -= weights[index]
    else:
      f[index] = round(capacity/weights[index], 2)

  return f


def main():
  weights = [10, 20, 20, 30, 40]
  values = [100, 300, 400, 600, 840]

  result = fractional_knapsack(weights, values, 50)
  
  print(result)

main()
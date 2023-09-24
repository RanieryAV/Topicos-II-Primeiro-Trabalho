from mochila_fracionaria_linear import fractional_knapsack_linear

def main():
  obj=[(150, 30), (100, 50), (90, 10), (140, 70), (120, 40)]
  # [5,2,9,2,3]
  # [2,2,3,5,9]

  totalSumWeights = 0

  for index in range(len(obj)):
    totalSumWeights += obj[index][1] 

  result = fractional_knapsack_linear(obj, totalSumWeights, 150)

  print(result)

main()
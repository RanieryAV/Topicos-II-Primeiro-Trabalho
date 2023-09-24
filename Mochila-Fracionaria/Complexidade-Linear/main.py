from mochila_fracionaria_linear import fractional_knapsack_linear

def main():
  #Example inputs
  inputs = [
    { 'obj': [(5, 1), (10, 3), (15, 5), (7, 4), (8, 1), (9, 3), (4, 2)], 'maximumCapacity': 15 }, #expect 51
    { 'obj': [(840, 40), (600, 30), (400, 20), (100, 10), (300, 20)], 'maximumCapacity': 50 }, #expect 1040
  ]


  for input in inputs:
    totalSumWeights = 0
    obj = input['obj']
    maximumCapacity = input['maximumCapacity']
    
    for index in range(len(obj)):
      totalSumWeights += obj[index][1] 

    result = fractional_knapsack_linear(obj, totalSumWeights, maximumCapacity)

    print(result)

main()
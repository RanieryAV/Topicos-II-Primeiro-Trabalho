from mochila_fracionaria_linear import fractional_knapsack_linear
from time import time_ns

import sys
import os
path = os.path.abspath("../utils")
sys.path.append(path)

from ler_entrada import read_files
from gerar_graficos import individual_chart

def main():
  instances = read_files()
  times = list()

  for input in instances.copy():
    totalSumWeights = 0
    obj = input['obj']
    maximumCapacity = input['maximumCapacity']
    
    for index in range(len(obj)):
      totalSumWeights += obj[index][1] 

    start_time = time_ns()
    result = fractional_knapsack_linear(obj, totalSumWeights, maximumCapacity)

    print("result V1", result)
    end_time = time_ns()

    elapsed_time = end_time - start_time  #Calcula o tempo consumido em nanossegundos
    times.append((len(obj), elapsed_time))

  individual_chart(times)

main()
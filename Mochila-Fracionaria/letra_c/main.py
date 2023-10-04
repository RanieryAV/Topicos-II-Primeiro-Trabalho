from mochila_fracionaria_pivo_calculado import fractional_knapsack_pivot_calculation
import sys
import os
path = os.path.abspath("../utils")
sys.path.append(path)

from ler_entrada import read_files
from gerar_graficos import individual_chart
from time import time_ns


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
    resultV2 = fractional_knapsack_pivot_calculation(obj, totalSumWeights, maximumCapacity)
    print("resultV2", resultV2)
    end_time = time_ns()

    times.append((len(obj), end_time-start_time))

  individual_chart(times)
main()
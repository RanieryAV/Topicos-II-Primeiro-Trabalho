from mochila_fracionaria_linear import fractional_knapsack_linear
import time
import tracemalloc

import sys
import os
path = os.path.abspath("../utils")
sys.path.append(path)

from ler_entrada import read_files
from gerar_graficos import individual_chart

def main():
  instances = read_files()
  results = list()

  for input in instances.copy():

    start_execution = time.time()
    times_by_execution = list()
    memories_by_execution = list()

    while(time.time() - start_execution < 5):
      totalSumWeights = 0
      obj = input['obj']
      maximumCapacity = input['maximumCapacity']
      
      for index in range(len(obj)):
        totalSumWeights += obj[index][1] 

      tracemalloc.start()

      start_time = time.time_ns()
      result = fractional_knapsack_linear(obj, totalSumWeights, maximumCapacity)
      print("result v1", result)
      end_time = time.time_ns()

      first_size, _ = tracemalloc.get_traced_memory()
      
      tracemalloc.reset_peak()

      # mem_used_mb = first_peak / (1024 * 1024)  # first_peak é o uso de memória em bytes

      elapsed_time = end_time - start_time  #Calcula o tempo consumido em nanossegundos
      times_by_execution.append(elapsed_time)
      memories_by_execution.append(first_size)
      
    results.append(
      (
        len(obj),
        sum(times_by_execution)/len(times_by_execution),
        sum(memories_by_execution)/len(memories_by_execution)
      )
    )


  individual_chart(results)

main()
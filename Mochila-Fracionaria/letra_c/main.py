from mochila_fracionaria_pivo_calculado import fractional_knapsack_pivot_calculation
import sys
import os
path = os.path.abspath("../utils")
sys.path.append(path)

from ler_entrada import read_files
from gerar_graficos import individual_chart
import time
import tracemalloc


def main():
  instances = read_files()
  results = list()

 
  for input in instances.copy():
    start_execution = time.time()
    times_by_execution = list()
    memories_by_execution = list()

    while(time.time() - start_execution < 1):
      totalSumWeights = 0
      obj = input['obj']
      maximumCapacity = input['maximumCapacity']
      
      for index in range(len(obj)):
        totalSumWeights += obj[index][1] 
      
      tracemalloc.start()

      start_time = time.time_ns()
      result = fractional_knapsack_pivot_calculation(obj, totalSumWeights, maximumCapacity)
      print("result", result)
      end_time = time.time_ns()

      first_size, first_peak = tracemalloc.get_traced_memory()
      
      tracemalloc.reset_peak()

      mem_used_mb = first_peak / (1024 * 1024) 
      
      elapsed_time = end_time - start_time  #Calcula o tempo consumido em nanossegundos
      times_by_execution.append(elapsed_time)
      memories_by_execution.append(mem_used_mb)

    results.append(
      (
        len(obj),
        sum(times_by_execution)/len(times_by_execution),
        sum(memories_by_execution)/len(memories_by_execution)
      )
    )
  
  individual_chart(results)

main()
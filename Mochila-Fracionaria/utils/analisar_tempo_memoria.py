import time
import tracemalloc
import sys
import os

path = os.path.abspath("../letra_a")
sys.path.append(path)

path = os.path.abspath("../letra_b")
sys.path.append(path)

path = os.path.abspath("../letra_c")
sys.path.append(path)

from ler_entrada import read_files
from mochila_fracionaria_nLogn import fractionalKnapsack
from mochila_fracionaria_linear import fractional_knapsack_linear
from mochila_fracionaria_pivo_calculado import fractional_knapsack_pivot_calculation

def analyzes_time_and_memory(algorithm):
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
      if(algorithm == "fractionalKnapsack"):
        result = fractionalKnapsack(maximumCapacity, obj)
      elif(algorithm == "fractional_knapsack_linear"):
        result = fractional_knapsack_linear(obj, totalSumWeights, maximumCapacity)
      else:
        result = fractional_knapsack_pivot_calculation(obj, totalSumWeights, maximumCapacity)
      end_time = time.time_ns()

      first_size, first_peak = tracemalloc.get_traced_memory()
      
      tracemalloc.reset_peak()

      elapsed_time = end_time - start_time  #Calcula o tempo consumido em nanossegundos
      times_by_execution.append(elapsed_time)
      memories_by_execution.append(first_peak)
    print("result", (len(obj), result))
    
    results.append(
      (
        len(obj),
        sum(times_by_execution)/len(times_by_execution),
        sum(memories_by_execution)/len(memories_by_execution)
      )
    )

  return results


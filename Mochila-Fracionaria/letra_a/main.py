import os
import sys
import time
import tracemalloc

from mochila_fracionaria_nLogn import fractionalKnapsack

path = "Mochila-Fracionaria/utils"
sys.path.append(path)

from ler_entradaFracionaria import read_files
from gerar_graficos import individual_chart

def main():
  instances = read_files()
  results = list()

  for input in instances.copy():

    start_execution = time.time()
    times_by_execution = list()
    memories_by_execution = list()

    while(time.time() - start_execution < 5):
      obj = input['obj']
      maximumCapacity = input['maximumCapacity']

      tracemalloc.start()

      start_time = time.time_ns()
      fractionalKnapsack(maximumCapacity, obj)
    #   print(input['obj'])
      end_time = time.time_ns()

      first_size, first_peak = tracemalloc.get_traced_memory()
      
      tracemalloc.reset_peak()

      mem_used_mb = first_peak / (1024 * 1024)  # first_peak é o uso de memória em bytes

      print("mem_used_mb", mem_used_mb)
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
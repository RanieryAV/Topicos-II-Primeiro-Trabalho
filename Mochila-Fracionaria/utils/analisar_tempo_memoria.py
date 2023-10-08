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

# Essa função recebe o nome do algoritmo
def analyzes_time_and_memory(algorithm):
  # Lendo as instancias
  instances = read_files()

  #Armazena os resultados obtidos
  results = list()

  # Amazena resultados da tabela
  table = list()

  for input in instances.copy():

    # Armazena o inicio da execução
    start_execution = time.time()
    times_by_execution = list()
    memories_by_execution = list()
    number_of_executions = 0

    # Algoritmo vai se executado durante 5 segundos 
    while(time.time() - start_execution < 5):
      totalSumWeights = 0
      obj = input['obj']
      maximumCapacity = input['maximumCapacity']
      
      for index in range(len(obj)):
        totalSumWeights += obj[index][1] 

      tracemalloc.start()
      
      start_time = time.time_ns()
      if(algorithm == "fractionalKnapsack"):
        fractionalKnapsack(maximumCapacity, obj)
      elif(algorithm == "fractional_knapsack_linear"):
        fractional_knapsack_linear(obj, totalSumWeights, maximumCapacity)
      else:
        fractional_knapsack_pivot_calculation(obj, totalSumWeights, maximumCapacity)
      end_time = time.time_ns()

      first_size, fisr_pick = tracemalloc.get_traced_memory()
      
      tracemalloc.reset_peak()

      elapsed_time = end_time - start_time  #Calcula o tempo consumido em nanossegundos
      times_by_execution.append(elapsed_time)
      memories_by_execution.append(first_size)

      number_of_executions += 1
    
    input_size = len(obj)
    average_execution_time = sum(times_by_execution)/len(times_by_execution)
    average_memory_usage = sum(memories_by_execution)/len(memories_by_execution)


    table.append((input_size, average_execution_time, min(times_by_execution), max(times_by_execution), number_of_executions, average_memory_usage))
    results.append((input_size, average_execution_time, average_memory_usage))

  return (results, table)


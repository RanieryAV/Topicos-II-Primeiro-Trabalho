import sys
import os

path = os.path.abspath("../utils")
sys.path.append(path)

from analisar_tempo_memoria import analyzes_time_and_memory
from gerar_graficos import comparative_chart

def main():
  fractionalKnapsack = analyzes_time_and_memory("fractionalKnapsack")
  print(fractionalKnapsack)
  print("\n")
  
  fractional_knapsack_linear = analyzes_time_and_memory("fractional_knapsack_linear")
  print(fractional_knapsack_linear)
  print("\n")

  fractional_knapsack_pivot_calculation = analyzes_time_and_memory("fractional_knapsack_pivot_calculation")
  print(fractional_knapsack_pivot_calculation)
  print("\n")

  comparative_chart([fractionalKnapsack, fractional_knapsack_linear, fractional_knapsack_pivot_calculation])

main()
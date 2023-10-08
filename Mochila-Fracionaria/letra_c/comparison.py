import sys
import os

path = os.path.abspath("../utils")
sys.path.append(path)

from analisar_tempo_memoria import analyzes_time_and_memory
from gerar_graficos import comparative_chart

def main():
  fractionalKnapsack, _ = analyzes_time_and_memory("fractionalKnapsack")
  
  fractional_knapsack_linear, _ = analyzes_time_and_memory("fractional_knapsack_linear")

  fractional_knapsack_pivot_calculation, _ = analyzes_time_and_memory("fractional_knapsack_pivot_calculation")

  comparative_chart([fractionalKnapsack, fractional_knapsack_linear, fractional_knapsack_pivot_calculation])

main()
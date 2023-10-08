import sys
import os
path = os.path.abspath("../utils")
sys.path.append(path)

from gerar_graficos import individual_chart
from analisar_tempo_memoria import analyzes_time_and_memory

def main():
  results = analyzes_time_and_memory("fractional_knapsack_pivot_calculation")
  individual_chart(results)

main()
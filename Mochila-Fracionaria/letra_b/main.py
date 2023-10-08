import sys
import os
path = os.path.abspath("../utils")
sys.path.append(path)


from gerar_graficos import individual_chart
from analisar_tempo_memoria import analyzes_time_and_memory

def main():
  results, table = analyzes_time_and_memory("fractional_knapsack_linear")
  
  print("fractional_knapsack_linear table", table)
  print("\n")
  
  individual_chart(results)

main()
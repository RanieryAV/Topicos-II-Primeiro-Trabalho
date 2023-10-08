import sys

path = "../utils"
sys.path.append(path)

from gerar_graficos import individual_chart
from analisar_tempo_memoria import analyzes_time_and_memory

def main():
  results, table = analyzes_time_and_memory("fractionalKnapsack")
  
  print("fractionalKnapsack table", table)
  print("\n")

  individual_chart(results)

main()
import sys

path = "../utils"
sys.path.append(path)

from gerar_graficos import individual_chart
from analisar_tempo_memoria import analyzes_time_and_memory

def main():
  results = analyzes_time_and_memory("fractionalKnapsack")
  individual_chart(results)

main()
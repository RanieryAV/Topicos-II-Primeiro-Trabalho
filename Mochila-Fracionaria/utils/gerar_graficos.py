import matplotlib.pyplot as plt

def individual_chart(obj):
  print("obj", obj)
  tamanho_da_entrada, tempo = zip(*obj)

  # Crie o gráfico de dispersão (scatter plot)
  plt.figure(figsize=(10, 6))  # Define o tamanho da figura
  plt.scatter(tamanho_da_entrada, tempo, marker='o', color='b', label='Tempo de Execução')

  # Adicione uma linha conectando os pontos
  # plt.plot(tamanho_da_entrada, tempo, linestyle='-', color='r', label='Linha de Regressão')

  # Adicione rótulos aos eixos e um título
  plt.xlabel('Tamanho da Entrada')
  plt.ylabel('Tempo (ns)')
  plt.title('Tempo de Execução em Função do Tamanho da Entrada')

  # Adicione uma legenda
  plt.legend()

  # Exiba o gráfico
  plt.grid(True)
  plt.show()
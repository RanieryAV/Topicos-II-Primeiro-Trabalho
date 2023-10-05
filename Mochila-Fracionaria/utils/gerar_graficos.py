import matplotlib.pyplot as plt

def memory_graph(input_size, memory):
  # Crie o gráfico de dispersão (scatter plot) para o uso de memória
  plt.figure(figsize=(10, 6))
  plt.scatter(input_size, memory, marker='x', color='r', label='Uso de Memória')

  # Adicione rótulos aos eixos e um título
  plt.xlabel('Tamanho da Entrada')
  plt.ylabel('Uso de Memória (MB)')
  plt.title('Uso de Memória em Função do Tamanho da Entrada')

  # Adicione uma legenda
  plt.legend()

  # Exiba o gráfico
  plt.grid(True)
  plt.show()

def time_graph(input_size, time):
  plt.figure(figsize=(10, 6))  # Define o tamanho da figura
  plt.scatter(input_size, time, marker='o', color='b', label='Tempo de Execução')

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

def individual_chart(obj):
  input_size, time, memory = zip(*obj)

  time_graph(input_size, time)
  memory_graph(input_size, memory)
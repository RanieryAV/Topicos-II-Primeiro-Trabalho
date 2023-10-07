import matplotlib.pyplot as plt
import plotly.express as px

def memory_graph(input_size, memory):
  x = input_size
  y = memory

  fig = px.scatter(x=x, y=y, title=f"Uso de Memória em Função do Tamanho da Entrada", labels={'x': 'Tamanho da Entrada', 'y': 'Uso de Memória (MB)'})

  # Exibir o gráfico
  fig.show()

def time_graph(input_size, time):
  x = input_size
  y = time

  fig = px.scatter(x=x, y=y, title=f"Tempo de execução em função do tamanho da entrada", labels={'x': 'Tamanho da Entrada', 'y': 'Tempo (ns)'})

  # Exibir o gráfico
  fig.show()

def individual_chart(obj):
  input_size, time, memory = zip(*obj)

  time_graph(input_size, time)
  memory_graph(input_size, memory)
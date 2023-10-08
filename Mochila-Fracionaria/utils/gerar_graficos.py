import plotly.express as px
import pandas as pd

def memory_graph(input_size, memory):
  x = input_size
  y = memory

  fig = px.scatter(x=x, y=y, title=f"Uso de memória em função do tamanho da entrada",
    labels={'x': 'Tamanho da Entrada', 'y': 'Uso de Memória (Bytes)'})

  # Definir o tamanho da fonte do título
  fig.update_layout(title_font=dict(size=24))
  
  # Definir o tamanho da fonte dos rótulos dos eixos x e y
  fig.update_xaxes(tickfont=dict(size=18))
  fig.update_yaxes(tickfont=dict(size=18))

  # Definir o tamanho da fonte dos rótulos dos eixos x e y
  fig.update_xaxes(title_font=dict(size=25))
  fig.update_yaxes(title_font=dict(size=25))

  # Definir a cor do marcador
  fig.update_traces(marker=dict(color='red'))

  # Definir o tamanho dos pontos
  fig.update_traces(marker=dict(size=10)) 

  # Exibir o gráfico
  fig.show()

def time_graph(input_size, time):
  x = input_size
  y = time

  fig = px.scatter(x=x, y=y, title=f"Tempo de execução em função do tamanho da entrada",
    labels={'x': 'Tamanho da Entrada', 'y': 'Tempo (ns)'})
  
  # Definir o tamanho da fonte do título
  fig.update_layout(title_font=dict(size=24))

  # Definir o tamanho da fonte dos rótulos dos eixos x e y
  fig.update_xaxes(tickfont=dict(size=18))
  fig.update_yaxes(tickfont=dict(size=18))

  # Definir o tamanho da fonte dos rótulos dos eixos x e y
  fig.update_xaxes(title_font=dict(size=25))
  fig.update_yaxes(title_font=dict(size=25))


  # Definir a cor do marcador
  fig.update_traces(marker=dict(color='blue'))

  # Definir o tamanho dos pontos
  fig.update_traces(marker=dict(size=10)) 


  # Exibir o gráfico
  fig.show()

def individual_chart(obj):
  input_size, time, memory = zip(*obj)

  time_graph(input_size, time)
  memory_graph(input_size, memory)


def comparative_chart(arr):
  fisrt, second, third = arr

  input_size_first, time_first, memory_first = zip(*fisrt)
  input_size_second, time_second, memory_second = zip(*second)
  input_size_third, time_third, memory_third = zip(*third)

  df = pd.DataFrame({'Tamanho da Entrada': input_size_first + input_size_second + input_size_third,
    'Tempo (ns)': time_first + time_second + time_third,
    'Execução': ['O(n * log n)'] * len(input_size_first) + ['O(n) mediana das medianas'] * len(input_size_second) + ['O(n) média das razões'] * len(input_size_third)})

  # Criar um gráfico de dispersão comparativo com Plotly Express
  fig = px.scatter(df, x='Tamanho da Entrada', y='Tempo (ns)', color='Execução', title='Comparação de tempos de execução')

  # Definir o tamanho da fonte do título
  fig.update_layout(title_font=dict(size=24))

  # Definir o tamanho da fonte dos rótulos dos eixos x e y
  fig.update_xaxes(tickfont=dict(size=18))
  fig.update_yaxes(tickfont=dict(size=18))

  # Definir o tamanho da fonte dos rótulos dos eixos x e y
  fig.update_xaxes(title_font=dict(size=25))
  fig.update_yaxes(title_font=dict(size=25))


  # Definir o tamanho dos pontos
  fig.update_traces(marker=dict(size=10)) 

  fig.show()

caminho = "Mochila-Fracionaria/Instancias/"
import os

def carregaArquivo(arquivo):
  valores = []

  instancia = open(arquivo, 'r')
  instancia = instancia.readlines()
  list(instancia)

  result = [item.split(',') for item in instancia]
  result = [value for value in result if value != " \n"]
  result_flat = []

  for l in result:
    for item in l:
      item  = ''.join(item.splitlines())
      item = item.replace(" ", "")
      result_flat.append(int(item))

  valores.append(result_flat)

  return valores

def listFiles(caminho):
  nomes = []
  for diretorio, subpastas, arquivos in os.walk(caminho):
    for arquivo in arquivos:
      nomes.append(os.path.join(diretorio, arquivo))
  return nomes


def read_files():
  arquivos = listFiles(caminho)

  result = list()
  
  for arq in arquivos:
    vet = carregaArquivo(arq)

    W = vet[0][0]
    arr = vet[0][1:]


    obj = list()

    for i in range(0, int(len(arr)/2)):
      obj.append((arr[i*2], arr[(i*2)+1]))
    
    result.append({ 'obj': obj, 'maximumCapacity': W })
  
  return result
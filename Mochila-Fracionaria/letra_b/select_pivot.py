def ratioCmp(item):
  return item[0] / item[1]
    
def select_pivot(obj, ini, fim):
  # Armazenamos o número de candidatos para ser o pivô
  ncand = (fim - ini ) + 1
  # Preenchemos uma lista com os indices dos candidados
  cand = list(range(ini, fim+1))

  while ncand > 1:
    storeind = 0

    # Aqui dividimos a lista de candidatos em grupos de 5
    for i in range(0, ncand, 5):
      posini, posfim = i, min(i + 4, ncand)

      # Ordenamos este grupo de 5 elementos baseando na razão valor/peso
      cand[posini:posfim] = sorted(cand[posini:posfim], key=lambda x: ratioCmp(obj[x]))

      # Pegamos a mediana deste grupo
      cand[storeind] = cand[(posini + posfim) // 2]

      storeind += 1
    
    # Aqui atualizamos o número de candidatos depois que pegamos a mediana de cada grupo
    ncand = storeind

  return cand[0]
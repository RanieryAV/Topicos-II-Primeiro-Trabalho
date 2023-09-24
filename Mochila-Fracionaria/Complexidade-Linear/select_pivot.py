def ratioCmp(item):
  return item[0] / item[1]
    
def select_pivot(obj, ini, fim):
  ncand = fim - ini
  cand = list(range(ini, fim))

  while ncand > 1:
    storeind = 0

    for i in range(0, ncand, 5):
      posini, posfim = i, min(i + 5, ncand)

      cand[posini:posfim] = sorted(cand[posini:posfim], key=lambda x: ratioCmp(obj[x]))
      cand[storeind] = cand[(posini + posfim) // 2]

      storeind += 1
      
    ncand = storeind

  return cand[0]
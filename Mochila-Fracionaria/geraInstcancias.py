'''
    Gerardor de instâncias para Mochila Fracionária
'''

import random
tamanho = 700000
test=10

for i in range(0,1):
    file = open('{}.txt'.format(i+test),'w')
    W = random.randint(1,100)
    file.writelines(str(W) + " \n")
    for j in range(tamanho):
        lucro = random.randint(1, 100)
        peso = random.randint(1, 100)
        item = [str(lucro), ', ', str(peso)]
        file.writelines(item)
    print("Instância: {}".format(i))
    tamanho *= 10
    file.close()
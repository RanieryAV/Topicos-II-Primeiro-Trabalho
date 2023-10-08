'''
    Gerardor de instâncias para Mochila Fracionária
'''

import random

tamanho = 1200000
test=1

for i in range(0,1):
    file = open('./Instancias/{}.txt'.format(i+test),'w')
    W = random.randint(500,1000)
    file.writelines(str(W) + " \n")
    for j in range(tamanho):
        lucro = random.randint(1, 1000)
        peso = random.randint(1, 1000)
        item = [str(lucro), ', ', str(peso)]
        file.writelines(item)
    print("Instância: {}".format(i))
    tamanho *= 10
    file.close()
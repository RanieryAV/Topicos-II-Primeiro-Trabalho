'''
    Gerardor de instâncias para Mochila Fracionária
'''

import random

tamanho = 100

for i in range(1,10):
    file = open('{}.txt'.format(i),'w')
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
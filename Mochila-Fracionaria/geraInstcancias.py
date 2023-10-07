'''
    Gerardor de instâncias para Mochila Fracionária
'''

import random

tamanho = 100

for i in range(1,5):
    file = open('Mochila-Fracionaria/Instancias/{}.txt'.format(i),'w')
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
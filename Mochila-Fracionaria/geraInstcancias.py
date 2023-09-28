'''
    Gerardor de instâncias para Mochila Fracionária
'''

import random


for i in range(1,10):
    file = open('{}.txt'.format(i),'w')
    for j in range(i*10):
        lucro = random.randint(1, 100)
        peso = random.randint(1, 100)
        item = [str(lucro), ', ', str(peso), "\n"]
        file.writelines(item)
    print("Instância: {}".format(i))	
    file.close()
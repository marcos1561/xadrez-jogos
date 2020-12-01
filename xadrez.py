import numpy as np
from functions import *

# Número de elementos
num_elementos = 6
elementos = np.arange(num_elementos)


"""Gera todas as duplas possíveis com os n elementos

    Consiste em pegar o elemnto i e formar duplas com os elemntos moiores que i 
"""
duplas = np.array([])

for i in range(elementos.size):
    for j in range(i+1, elementos.size):
        duplas = np.append(duplas, f"{i} X {j}")


''' Separa o conjunto das duplas em rodadas. 
    
    Cada rodada possui todos os elemntos uma única vez.

    O processo consiste em tentar colocar dupla a dupla nas rodadas, até preencher todos as rodadas. 
'''
# Cria uma lista  com o número de rodadas que irão existir
rodadas = []
for i in range(num_elementos-1):
    rodadas.append([])


# Loop pelas duplas
np.random.shuffle(duplas)
for dupla in duplas:
    # Separa os elementos da dupla
    el_1 = dupla[:1]
    el_2 = dupla[-1:]

    # Loop pelos rodadas
    for rod_id in range(len(rodadas)):
        # Variável que armazena se algum elemento da dupla está no subconjunto em questão
        dupla_in = False
        
        # Verifica se algum elemnto da dupla já está no subconjunto em quenstão
        # Caso estiver, quebra o loop
        for rod_dupla in rodadas[rod_id]:      
            if el_1 in rod_dupla or el_2 in rod_dupla:
                dupla_in = True
                break
        
        # Se a dupla não estiver na rodada em questão, adiciona ela ao mesmo
        if not dupla_in:
            rodadas[rod_id].append(dupla)
            break
    
    exibir_rodadas(rodadas, int(num_elementos/2), num_elementos)
    print(f"{dupla}\n", "=-="*30)
    
print(rodadas)

        
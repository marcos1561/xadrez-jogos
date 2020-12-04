import numpy as np
from functions import *

# Número de elementos
num_el = 6
elementos = np.arange(num_el)


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
for i in range(num_el-1):
    rodadas.append([])

np.random.shuffle(duplas)
duplas_copia = list(duplas)
for rodada in rodadas:
    duplas_selec = []
    el_selec = []

    duplas_ignore = []
    for i in range(int(num_el/2)):
        jogo_i_ignore = []
        for j in range(i):
            jogo_i_ignore.append([])
        
        duplas_ignore.append(jogo_i_ignore) 

    i = 0 
    while i < len(duplas_copia):
        dupla = duplas_copia[i]
        
        current_dupla_ignore = duplas_to_ignore(duplas_ignore, len(duplas_selec))
        if dupla not in current_dupla_ignore:
            el_1 = dupla[:1]
            el_2 = dupla[-1:]
            
            el_selec = []
            for item in duplas_selec:
                [el_selec.append(el) for el in [item[:1], item[-1:]]]

            if el_1 not in el_selec and el_2 not in el_selec:
                duplas_selec.append(dupla)
                
                rodada.append(dupla)
                
                exibir_rodadas(rodadas, int(num_el/2), num_el)
                print(f"{dupla}\n", "=-="*30)
            
            if len(rodada) == int(num_el/2):
                break

        i += 1
        if i == len(duplas_copia):
            
            i = 0
            
            

            duplas_selec.pop(-1)
            rodada.pop(-1)
            

    [duplas_copia.remove(dupla) for dupla in duplas_selec]

verificar(rodadas, num_el)
print(rodadas)     
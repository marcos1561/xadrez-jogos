import numpy as np
import time
from functions import *

start_time = time.time()

# Número de elementos
num_el = 22
elementos = np.arange(num_el)


"""Gera todas as duplas possíveis com os n elementos

    Consiste em pegar o elemnto i e formar duplas com os elemntos moiores que i 
"""
duplas = np.array([])

for i in range(elementos.size):
    for j in range(i+1, elementos.size):
        duplas = np.append(duplas, f"{i} X {j}")

print(len(duplas))


''' Separa o conjunto das duplas em rodadas. 
    
    Cada rodada possui todos os elemntos uma única vez.

    O processo consiste em tentar colocar dupla a dupla nas rodadas, até preencher todos as rodadas. 
'''
# Cria uma lista  com o número de rodadas que irão existir
rodadas = []
for i in range(num_el-1):
    rodadas.append([])

print(len(rodadas))

# np.random.shuffle(duplas)
duplas_copia = list(duplas)

# print(duplas)
# duplas_copia = ['0 X 1', '1 X 5', '0 X 4','3 X 4', '4 X 5', '0 X 2', '0 X 5', '2 X 4', '1 X 3','1 X 4', '0 X 3', '2 X 3', '2 X 5', '1 X 2', '3 X 5']

for rodada in rodadas:
    duplas_selec = []
    el_selec = []

    # duplas_ignore = []
    # for i in range(int(num_el/2)):
    #     jogo_i_ignore = []
    #     for j in range(i):
    #         jogo_i_ignore.append([])
        
    #     duplas_ignore.append(jogo_i_ignore) 

    contador = 0

    duplas_ignore = []
    for i in range(int(num_el/2)):
        shape = [1 for _ in range(i)] + [0]
        new_dlp_ig = np.empty(shape=shape).tolist()
        duplas_ignore.append(new_dlp_ig)
    

    i = 0 
    while i < len(duplas_copia):
        contador += 1

        dupla = duplas_copia[i]
        
        dupla_ignore_arr_id = duplas_to_ignore(duplas_ignore, len(duplas_selec))
        current_dupla_ignore = get_list_item(duplas_ignore, dupla_ignore_arr_id)
        
        if dupla not in current_dupla_ignore:
            x_id = dupla.find("X")
            el_1 = dupla[:x_id-1]
            el_2 = dupla[x_id+2:]
            
            el_selec = []
            for item in duplas_selec:
                x_id = item.find("X")
                [el_selec.append(el) for el in [item[:x_id-1], item[x_id+2:]]]

            if el_1 not in el_selec and el_2 not in el_selec:
                duplas_selec.append(dupla)
                
                rodada.append(dupla)
                
            # if contador > 5000:
            #     # if len(rodadas[13]) == 6:
            #     #     noice = 2

            #     contador = 0
            #     exibir_rodadas(rodadas, int(num_el/2), num_el)
            #     print(f"{dupla}\n", "=-="*30)
            #     # print(duplas_copia)
            
            if len(rodada) == int(num_el/2):
                break

        i += 1
        if i == len(duplas_copia):
            i = 0

            dpl_up_id = duplas_to_ignore(duplas_ignore, len(duplas_selec)-1)
            dpl_up = get_list_item(duplas_ignore, dpl_up_id)
            dpl_up.append(duplas_selec[-1])

            duplas_update_shape(duplas_ignore, dpl_up_id)

            duplas_selec.pop(-1)
            rodada.pop(-1)

    [duplas_copia.remove(dupla) for dupla in duplas_selec]


end_time = time.time()
exec_time = end_time - start_time

print(duplas_copia)     
exibir_rodadas(rodadas, int(num_el/2),  num_el)
verificar(rodadas, num_el)
print(f"{round(exec_time, 2)} segundos")
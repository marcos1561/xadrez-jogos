import numpy as np
import time
from functions import *

start_time = time.time()

# Número de elementos
num_el = 18
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

    O processo consiste em ir adionando jogo por jogo até preencher a rodada, quando um rodada está completa, aplica este mesmo
    processo para a próxima rodada até preencher todas as rodadas.
    Caso chegue num beco sem saída (impossível preencher o resto da rodada com as duplas restantes) desfaz a última dupla colocana rodada e
    continua com o memso processo

    OBS: O processo de desfazer a última ação vai até o inicio da rodada, portanto se for ímpossivel formar uma rodada, um erro irá ocorrer,
    no entendo é conjecturado que a possibilidade disso acontecer, cai dramasticamente com o número de elementos crescendo. 
'''
# Cria uma lista com o número de rodadas que irão existir
rodadas = []
for i in range(num_el-1):
    rodadas.append([])


# np.random.shuffle(duplas)
duplas_copia = list(duplas)

#Exibir rodada sendo preenchida no console?
exibir_rod_console = False
# Controlam a frequência da exibição da rodada no console
contador = 0

for rodada in rodadas:
    # Contém as duplas selecionadas desrodada = []
    # Contém os elemtos selecionados dessa rodada
    el_selec = []

    """
        Essa variável contém todas as listas com duplas para serem ignoradas (Uma dupla deve ser ignorada caso seja impossível completar
        a rodada logo após ela ter sido adicionada na rodada).x

        OBS: ver documentação da função "duplas_to_ignore_id" para mais informações
    """
    duplas_ignore = []

    # Gerado todos os elementos de "duplas_ignore" com suas respectivas dimensões.
    # Conforme o algoritmo for executado, duplas serão adicionadas nessa variável.
    # Quando a rodada for completa, essa variável será limpada.
    # num_el/2 é o número de jogos que cada rodada vai possuir.
    for i in range(int(num_el/2)):
        shape = [1 for _ in range(i)] + [0]
        new_dlp_ig = np.empty(shape=shape).tolist()
        duplas_ignore.append(new_dlp_ig)
    

    # Loop que preenche a rodada
    # Pega dupla por dupla e tenta colocar na rodada em questão
    i = 0 
    while i < len(duplas_copia):
        contador += 1

        dupla = duplas_copia[i]
        
        # Baseada na posição em que estamos tentanto colocar a dupla na rodada (len(rodada)), pega a lista de duplas para ignorar,
        # ou seja, as duplas que tentaram ser colocada nessa rodada, mas não deram certo
        dupla_ignore_arr_id = duplas_to_ignore_id(duplas_ignore, len(rodada))
        current_dupla_ignore = get_list_item(duplas_ignore, dupla_ignore_arr_id)
        
        if dupla not in current_dupla_ignore:
            # Pega os elemntos da dupla selecionada
            x_id = dupla.find("X")
            el_1 = dupla[:x_id-1]
            el_2 = dupla[x_id+2:]
            
            # Baseado nas duplas que já estão na rodada, extrai todos os elemntos que já estão nessa rodada
            el_selec = []
            for item in rodada:
                x_id = item.find("X")
                [el_selec.append(el) for el in [item[:x_id-1], item[x_id+2:]]]

            # Se ambos elementos da dupla seleciona não estiverem nos elementos da rodada adiciona a dupla na rodadaa
            if el_1 not in el_selec and el_2 not in el_selec:
                rodada.append(dupla)
                
            # Exibe as rodadas como estão no momento no console
            if contador > 5000 and exibir_rod_console:
                contador = 0
                exibir_rodadas(rodadas, int(num_el/2), num_el)
                print(f"Dupla atual: {dupla}\n", "=-="*30)
            
            # Se a rodada estiver completa quebra o Loop e vai para a próxima rodada
            if len(rodada) == int(num_el/2):
                break

        i += 1

        # Esse loop nunca deve chegar até o fim, caso isso aconteça é porque é impossível completara a rodad com as duplas restantes.
        # Portanto é retirado a última dupla da rodada e recomeçado o loop.
        if i == len(duplas_copia):
            i = 0

            # índice da lista que contém as duplas para ignorar em que será adiciona a última dupla da rodada em questão
            dpl_up_id = duplas_to_ignore_id(duplas_ignore, len(rodada)-1)
            # Lista que contém as duplas para ignorar em que será adiciona a última dupla da rodada em questão
            dpl_up = get_list_item(duplas_ignore, dpl_up_id)
            # Adicionado a última dupla na rodada na lista de duplas para ignorar
            dpl_up.append(rodada[-1])

            # Atualiza os shapes da listas que estão em "duplas_ignore" pois um item for adiciona em alguma de suas listas
            duplas_update_shape(duplas_ignore, dpl_up_id)

            # Retira a última dupla da rodada
            rodada.pop(-1)

    # Remove as duplas que foram colocadas na rodada na lista que contém todos os jogos possíveis
    [duplas_copia.remove(dupla) for dupla in rodada]


end_time = time.time()
exec_time = end_time - start_time

# Exibe as rodadas
exibir_rodadas(rodadas, int(num_el/2),  num_el)
#Verifica se existe algum erro nas rodasdas calculdas
verificar(rodadas, num_el)
# Tempo de execução
print(f"{round(exec_time, 2)} segundos")
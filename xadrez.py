import numpy as np
import time
from functions import *

start_time = time.time()

# Número de elementos. OBS: Essa variável deve ser um número par.
num_el = 26
elementos = np.arange(num_el)

#Exibir rodada sendo preenchida no console?
exibir_rod_console = True
# Controlam a frequência da exibição da rodada no console
count_max = 50000


"""Gera todas as duplas possíveis com os n elementos

    Consiste em pegar o elemnto i e formar duplas com os elemntos moiores que i 
"""
duplas = np.array([])

for i in range(elementos.size):
    for j in range(i+1, elementos.size):
        duplas = np.append(duplas, f"{i} X {j}")


''' Separa o conjunto das duplas em rodadas. 
    
    Cada rodada possui todos os elemntos uma única vez.

    O processo consiste em ir adionando jogo por jogo até preencher a rodada, quando uma rodada está completa, é aplica esse mesmo
    processo para a próxima rodada, até preencher todas as rodadas.
    Caso chegue em um beco sem saída (impossível preencher o resto da rodada com as duplas restantes) desfaz a última dupla colocada na rodada 
    e continua com o mesmo processo.

    OBS: O processo de desfazer a última ação, vai até o inicio da rodada, portanto se for ímpossivel formar uma rodada, um erro irá ocorrer,
    no entendo, é conjecturado que a possibilidade disso acontecer cai dramasticamente com o número de elementos crescendo. 
'''
# Cria uma lista com o número de rodadas que irão existir
rodadas = []
for i in range(num_el-1):
    rodadas.append([])

# np.random.shuffle(duplas)
duplas_copia = list(duplas)

for rodada in rodadas:
    # Contém os elementos selecionados da rodada em questão
    el_selec = []
    # Sempre que é adicionado ou removido algum jogo da rodada, essa variável fica = True
    len_rodada_change = True

    """
        Essa variável contém todas as listas com duplas para serem ignoradas (Uma dupla deve ser ignorada caso 
        seja impossível completar a rodada logo após ela ter sido adicionada na rodada).

        OBS: ver documentação da função "duplas_to_ignore_id" para mais informações
    """
    duplas_ignore = []
    # Gera todos os elementos de "duplas_ignore" com saus respectivas dimensões.
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
    contador = 0 # Contador que ativa a exibição das rodadas
    while i < len(duplas_copia):
        contador += 1
        dupla = duplas_copia[i]
        
        # Caso o compriemnto da rodada mude, é necessário recalcular qual deve ser a lista com duplas para ignorar
        if len_rodada_change:
            # Baseada na posição em que estamos tentanto colocar a dupla na rodada (len(rodada)), pega a lista de duplas para ignorar,
            # ou seja, as duplas que tentaram ser colocada nessa rodada, mas não deram certo
            dupla_ignore_arr_id = duplas_to_ignore_id(duplas_ignore, len(rodada))
            current_dupla_ignore = get_list_item(duplas_ignore, dupla_ignore_arr_id)
            len_rodada_change = False
        
        if dupla not in current_dupla_ignore:
            # Pega os elementos da dupla selecionada
            x_id = dupla.find("X")
            el_1 = dupla[:x_id-1]
            el_2 = dupla[x_id+2:]
            
            # Se ambos elementos da dupla seleciona não estiverem nos elementos da rodada, adiciona a dupla na rodada
            if el_1 not in el_selec and el_2 not in el_selec:
                # Coloca os elementos dessa dupla em "el_selec"
                [el_selec.append(el) for el in [el_1, el_2]]
                rodada.append(dupla)
                len_rodada_change = True

                # Se a rodada estiver completa, quebra o Loop e vai para a próxima rodada
                if len(rodada) == int(num_el/2):
                    break

            # Exibe as rodadas como estão no momento, no console
            if contador > count_max and exibir_rod_console:
                contador = 0
                exibir_rodadas(rodadas, int(num_el/2), num_el)
                print(f"Dupla atual: {dupla}\n", "=-="*30)
            
        i += 1

        # Esse loop nunca deve chegar até o fim, caso isso aconteça é porque é impossível completara a rodada com as duplas restantes.
        # Portanto é retirado a última dupla da rodada e recomeçado o loop.
        if i == len(duplas_copia):
            # Calcula em qual ponto do loop se deve voltar para continuar preenchendo a rodada.
            # Esse ponto deve ser o índice da dupla que está sendo removida mais 1.
            # Como esse loop nunca deve acabar sem preencher a rodada, caso a dupla a ser removida seja a última na lista,
            # o ponto no loop continua sendo o último ponto.
            next_i = duplas_copia.index(rodada[-1]) + 1
            if next_i == len(duplas_copia):
                next_i = len(duplas_copia)-1

            i = next_i

            # índice da lista que contém as duplas para ignorar em que será adiciona a última dupla da rodada em questão
            dpl_up_id = duplas_to_ignore_id(duplas_ignore, len(rodada)-1)
            # Lista que contém as duplas para ignorar em que será adiciona a última dupla da rodada em questão
            dpl_up = get_list_item(duplas_ignore, dpl_up_id)
            # Adicionado a última dupla na rodada na lista de duplas para ignorar
            dpl_up.append(rodada[-1])

            # Atualiza os shapes da listas que estão em "duplas_ignore" pois um item for adiciona em alguma de suas listas
            duplas_update_shape(duplas_ignore, dpl_up_id)

            # Retira a última dupla da rodada e os dois últimos elementos de "el_selec"
            del(el_selec[-2:]) 
            rodada.pop(-1)
            len_rodada_change = True

    # Remove as duplas que foram colocadas na rodada, na lista que contém todos os jogos possíveis.
    [duplas_copia.remove(dupla) for dupla in rodada]

end_time = time.time()
exec_time = end_time - start_time

# Exibe as rodadas
exibir_rodadas(rodadas, int(num_el/2),  num_el)
#Verifica se existe algum erro nas rodasdas calculdas
verificar(rodadas, num_el)
# Tempo de execução
print(f"Elementos: {num_el}|", end=" ")
if exec_time > 60:
    print(f"{round(exec_time/60, 2)} minutos")
else:
    print(f"{round(exec_time, 2)} segundos")

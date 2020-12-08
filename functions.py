import numpy as np
import time

def gerar_rodadas(num_el, show_rod, count_show_max, count_time_max, max_time, duplas_init):
    """
        Gera as rodadas dodo um número de elementos

        Parâmetos:
        ----------
        num_el: int
            número de elementos
        
        show_rod: bool
            Controle se deve ser mostrado as rodadas durante a execução

        count_show_max: int 
            Controla a frêquancia de mostrar as rodadas durante a execução
        
        count_time_max: int
            Controla a frêquancia de verificar o tempo execução

        max_time: float
            Tempo máximo de execução
        
        duplas_init: list
            Lista com todas os jogos possíveis com um número de elemntos = num_el
            Se não for desejado já iniciar como os jogos prontos deve ser passado
            uma lista vazia.

        Retorna
        -------
        int, items

        O primeiro elemento do retorno pode ser o seguinte:
            1 - Se atingir uma rodada impossívez de fazer
            2 - Se atingir o tempo máximo de execução
            3 - Se completar a execução

        -Para os valores 1 e 2, o retorno é:
            (1 ou 2), time_elapsed: float, duplas: list

        Onde time_elapsed é o tempo de execução e duplas é lista com
        todos os jogos possíveis

        -Para o valor 3, o reterno é:
            3, rodadas: list

        Onde rodadas é a lista com todas as rodadas
    """

    start_time = time.time()
    duplas = np.array([]) # Variável que irá conter todos os jogos possíveis

    # If para caso já seja dado todos os jogos possíveis
    if len(duplas_init) > 0:
        duplas = duplas_init
    else:
        elementos = np.arange(num_el) # Número de elementos. OBS: Essa variável deve ser um número par.


        """Gera todas as duplas possíveis com os n elementos

            Consiste em pegar o elemnto i e formar duplas com os elementos moiores que i 
        """
        for i in range(elementos.size):
            for j in range(i+1, elementos.size):
                duplas = np.append(duplas, f"{i} X {j}")


    ''' Separa o conjunto das duplas em rodadas. 
        
        Cada rodada possui todos os elementos uma única vez.

        O processo consiste em ir adionando jogo por jogo até preencher a rodada, quando uma rodada está completa, é aplica esse mesmo
        processo para a próxima rodada, até preencher todas as rodadas.
        Caso chegue em um beco sem saída (impossível preencher o resto da rodada com as duplas restantes) desfaz a última dupla colocada na rodada 
        e continua com o mesmo processo.

        OBS: O processo de desfazer a última ação, vai até o inicio da rodada, portanto se for ímpossivel formar uma rodada, um erro irá ocorrer.
             Também é disparrado um erro se o tempo de execução ultrapassar um valor limite.
    '''
    # Cria uma lista com o número de rodadas que irão existir
    rodadas = []
    for _ in range(num_el-1):
        rodadas.append([])

    # Aleatoriza o arranjo de duplas e gera uma copia
    np.random.shuffle(duplas)
    duplas_copia = list(duplas)

    count_show = 0 # Contador que ativa a exibição das rodadas
    count_time = 0 # Contador que ativa a checagem do tempo
    
    for rodada in rodadas:
        el_selec = [] # Contém os elementos selecionados da rodada em questão

        # Loop que preenche a rodada
        # Pega dupla por dupla e tenta colocar na rodada em questão
        i = 0 
        while i < len(duplas_copia):
            dupla = duplas_copia[i]
            
            # Pega os elementos da dupla selecionada
            x_id = dupla.find("X")
            el_1 = dupla[:x_id-1]
            el_2 = dupla[x_id+2:]
            
            # Se ambos elementos da dupla seleciona não estiverem nos elementos da rodada, adiciona a dupla na rodada
            if el_1 not in el_selec and el_2 not in el_selec:
                # Coloca os elementos dessa dupla em "el_selec"
                [el_selec.append(el) for el in [el_1, el_2]]
                rodada.append(dupla)

                # Se a rodada estiver completa, quebra o Loop e vai para a próxima rodada
                if len(rodada) == int(num_el/2):
                    break

            # Exibe as rodadas como estão no momento, no console
            if show_rod:
                count_show += 1
                if count_show > count_show_max:
                    count_show = 0
                    exibir_rodadas(rodadas, int(num_el/2), num_el)
                    print(f"Dupla atual: {dupla}\n", "=-="*30)
                
            i += 1

            # Esse loop nunca deve chegar até o fim, caso isso aconteça é porque é impossível completara a rodada com as duplas restantes.
            # Portanto é retirado a última dupla da rodada e o loop volta açgumas duplas, para continuar preenchendo a rodada.
            if i == len(duplas_copia):
                # Calcula em qual ponto do loop se deve voltar para continuar preenchendo a rodada.
                # Esse ponto deve ser o índice da dupla que está sendo removida mais 1.
                # Como esse loop nunca deve acabar sem preencher a rodada, caso a dupla a ser removida seja a última na lista,
                # o ponto para retornar o loop é o índice da penúltima duplas na rodada mais 1 (OBS: Nessa caso, a última e a
                # penúltima duplas na rodada devem ser removidas. Uma é removida nesse if e a outra logo após)
                next_i = duplas_copia.index(rodada[-1]) + 1
                if next_i == len(duplas_copia):
                    del(el_selec[-2:])
                    rodada.pop(-1)

                    # Caso a rodada fique vazia, é impossível formar uma rodada com as duplas restantes.
                    # Portanto é retorndado as duplas (que será utilizando logo a seguir para reexecutar essa função),
                    # o tempo decorrido e um código que informa qual foi o erro (nesse caso 1).
                    if len(rodada) == 0:
                        time_elapsed = round(time.time()-start_time,2)
                        print(f"Rodada impossível | {time_elapsed} s")
                        
                        return 1, time_elapsed, duplas

                    next_i = duplas_copia.index(rodada[-1]) + 1

                i = next_i

                # Retira a última dupla da rodada e os dois últimos elementos de "el_selec"
                del(el_selec[-2:]) 
                rodada.pop(-1)

            count_time += 1
            if count_time > count_time_max:
                count_time = 0
                time_now = time.time()
                time_elapsed = time_now - start_time

                # Se o tempo de execução ultrapassa o valor limite, o código termina, para, então, recomeçar com um
                # novo arranjo aleatório para as duplas
                if time_elapsed > max_time:
                    print(f"Tempo máximo alcançado | {round(time_elapsed,2)} s")
                    return 2, round(time_elapsed, 2), duplas

        # Remove as duplas que foram colocadas na rodada, na lista que contém todos os jogos possíveis.
        [duplas_copia.remove(dupla) for dupla in rodada]

    return 3, rodadas


def exibir_rodadas(rodadas, max_duplas, long_el):
    """
    Imprime no console a lista que possui as rodadas.

    Parâmetros
    ----------
    rodadas: list 2-D
        lista contendo as rodadas
    
    max_duplas: int
        Indica o número máximos de duplas que uma rodada possui
    
    long_el: str
        Elemento nas rodadas com o maior número de caracteres

    Retorna
    -------
    None

    """
    long_el_size = len(str(long_el))
    for i in range(max_duplas):
        linha = "|"
        for rod in rodadas:
            if i < len(rod):
                dupla = rod[i]
                x_id = dupla.find("X")
                
                linha += f"{dupla[:x_id-1]}".rjust(long_el_size) + " X " + f"{dupla[x_id+2:]}".ljust(long_el_size) + "|"
            else:
                linha += "|".rjust(long_el_size*2 + 4)

        print(linha)


def verificar(rodadas, n):
    error = False
    duplas = []

    for rodada in rodadas:
        if len(rodada) != int(n/2):
            error = True
            print(f"Erro! Número de jogos na rodada.\n"
                  f"Esperado {int(n/2)} jogos ao invés de {len(rodada)}.\n"
                  f"Rodada: {rodada}\n")    

        elementos = []
        for dupla in rodada:
            x_id = dupla.find("X")
            el_i = [dupla[:x_id-1], dupla[x_id+2:]]
            for el in el_i:
                if el not in elementos:
                    elementos.append(el)
                else:
                    error = True
                    print(f"Erro! Elemento repetido\n"
                          f"Elemento: {el}\n"
                          f"Rodada: {rodada}\n")
            
            if dupla not in duplas:
                duplas.append(dupla)
            else:
                error = True
                print(f"Erro! Dupla repetida\n"
                      f"Dupla: {dupla}\n")

    if not error:
        print("Todas as rodadas estão corretas! :)")
        return False
    else:
        return True


def tempo_execucao(start_time, end_time, num_el, show):
    """
        Calcula o tempo de execução do código

        Parâmetros
        ----------
        start_time: float
            Tempo inicial
        
        end_time: flaot
            Tempo final
        
        num_el: int
            Número de elementos da atual execução

        show: bool
            Mostra o tempo no console

        Retorna
        -------
        exec_time: flaot
            O tempo de execução
    """

    exec_time = round((end_time - start_time), 2)
    
    if show:
        print(f"Elementos: {num_el}|", end=" ")
        if exec_time > 60:
            print(f"{round(exec_time/60, 2)} minutos")
        else:
            print(f"{round(exec_time, 2)} segundos")

    return exec_time

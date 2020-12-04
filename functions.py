import numpy as np

def exibir_rodadas(rodadas, max_duplas, long_el):
    """
    Imprime no console o conjunto que possui as rodadas.

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


def get_list_item(arr, arr_id):
    """
    Retorna o elemento da lista "arr" cujo índice é arr_id[0], arr_id[1], arr_id[2], ... arr_id[n], onde n = len(arr_id)-1

    Parâmetros
    ----------
    arr: list 
        lista de qualquer tamanho
    
    arr_id: list
        Lista contente os índices do elemento para retorna. Se tamanho deve ser menor ou igual a dimensão de "arr".

    Retorna
    -------
    element_return: list ou o tipo de elemento que estiver em "arr"
        Elemento da lista "arr" cujo índice é arr_id[0], arr_id[1], arr_id[2], ... arr_id[n], onde n = len(arr_id)-1
    """

    for index in arr_id:
        next_arr = arr[index]
        arr = next_arr
    
    element_return = arr
    return element_return


def duplas_to_ignore(duplas_ignore, jogo_num):
    arr_id = [-1]

    for i in range(jogo_num):
        arr_id[0] = i
        next_id = len(get_list_item(duplas_ignore, arr_id))
        arr_id.append(next_id)

    arr_id[0] += 1
    return (arr_id)


def duplas_update_shape(duplas_ignore, arr_id): 
    jogo_num = arr_id[0]
    max_jogos = len(duplas_ignore)

    dim = 0
    for i in range(jogo_num+1, max_jogos):
        shape = [1 for _ in range(dim)] + [0]
        dim += 1 
        
        arr_id[0] = i
        duplas_now = get_list_item(duplas_ignore, arr_id)
        duplas_now.append(np.empty(shape=shape).tolist())


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

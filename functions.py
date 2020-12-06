import numpy as np

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


def duplas_to_ignore_id(duplas_ignore, jogo_num):
    """
    Retorna os índices de lista que contém as duplas que devem ser ignoradas no processo de tentar colar uma dupla na rodada.

    Cada elemento da rodada possui listas de duplas para serem ignoradas (duplas, em que nessa posição, não permitem completar a rodada)
    O primeiro elemento da rodada tem um lista 1-D contendo as duplas para ignorar, o segundo elemento uma lista 2-D, pois cada elemento dessa 
    lista é uma lista que está associada aos elementos da lista do primeiro elemento da rodada, e assim sucessivamente.

    Sabendo qual o índice da posição na rodada em que estamos tentando colocar o jogo, podemos calcular o comprimento das listas de duplas 
    para ignorar dos índices acima, para assim, obter os índices da lista de duplas para ignorar do atual elemento da rodada.

    Parâmetros
    ----------
    duplas_ignore: list
        Lista contendo todas as listas com duplas para ignorar da atual rodada.

    jogo_num: int
        índice da posição na rodada em que o jogo está tentando ser colocado. Portanto, é o len() dos jogos que já foram colocados na rodada.  

    Retorna
    -------
        arr_id: list 1-D
            Lista contendo os índices da lista das duplas para serem ignoradas que está em "duplas_ignore".

    """

    arr_id = [-1]

    for i in range(jogo_num):
        arr_id[0] = i
        next_id = len(get_list_item(duplas_ignore, arr_id))
        arr_id.append(next_id)

    arr_id[0] += 1
    return (arr_id)


def duplas_update_shape(duplas_ignore, arr_id): 
    """
        Atualiza os shapes das listas que estão dentro de "duplas_ignore"

        Sempre que no elemento de índice i de "duplas_ignore" é adicionado um item na lista com índica x nesse elemento, todos os elementos 
        com índice > i devem ter seus shapes atualizados.
        A única atualização necessária é adiconar um item na lista de índice x nos elementos de "duplas_ignore" com índice > i

    
        Parâmtros:
        ----------
        duplas_ignore: list
            Lista contendo todas as listas com duplas para ignorar da atual rodada.

        arr_id: list 1-D
            Lista contendo os índices da lista de duplas para ignorar em que foi adicionado um elemento.

    """ 

    jogo_num = arr_id[0]
    max_jogos = len(duplas_ignore)

    dim = 0
    for i in range(jogo_num+1, max_jogos):
        # A dimensão do item que é adiconado no primeiro elemento de "duplas_ignore" com índice maior que arr_id[0]
        # é 1, do segundo elemento é 2, e assim por diante.
        shape = [1 for _ in range(dim)] + [0]
        dim += 1 
        
        # Pega a lista que é necessário adicionar um item e adicona o item
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

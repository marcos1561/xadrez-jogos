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


def duplas_to_ignore(duplas_ignore, jogo_num):
    list_index = []
    
    def return_list(lista, id):
        return lista[id]

    now_lista = duplas_ignore

    for i in range(jogo_num):
        now_lista = now_lista[i]
        list_index.append(len(now_lista))
    



def verificar(rodadas, n):
    duplas = []

    for rodada in rodadas:
        if len(rodada) != int(n/2):
            print(f"Erro! Número de jogos na rodada.\n"
                  f"Esperado {int(n/2)} jogos ao invés de {len(rodada)}.\n"
                  f"Rodada: {rodada}\n")    

        elementos = []
        for dupla in rodada:
            el_i = [dupla[:1], dupla[-1:]]
            for el in el_i:
                if el not in elementos:
                    elementos.append(el)
                else:
                    print(f"Erro! Elemento repetido\n"
                          f"Elemento: {el}\n"
                          f"Rodada: {rodada}\n")
            
            if dupla not in duplas:
                duplas.append(dupla)
            else:
                print(f"Erro! Dupla repetida\n"
                      f"Dupla: {dupla}\n")


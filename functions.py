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


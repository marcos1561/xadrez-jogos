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

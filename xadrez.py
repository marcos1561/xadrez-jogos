import time
import json
from functions import gerar_rodadas, exibir_rodadas, verificar, tempo_execucao

"""
    Este arquivo serve apenas para testes, "gerar_rodadas.py" é quem possui a usabilidade
"""

# Número de elementos. OBS: Essa variável deve ser um número par.
num_el_start = 0
num_el_end = 30
repeat_exec = 20 # Quantas vezes executar a geração de rodadas com n números de elementos

show_rod = False       # Exibir rodada sendo preenchida no console?
count_show_max = 50000 # Controlam a frequência da exibição da rodada no console
count_time_max = 50000 # Controlam a frequência da verificação do tempo

# Função que calcula o tempo máximo de execução em função do número elementos
def max_time_func(el):
    return 1.51**(el-26.9)

# Gera as rodadas com os parâmetros especificados acima
rod_error = [] # Erros nas rodadas são armazenaddos aqui
time_list = [] # Contém os tempos de execução
for num_el in range(num_el_start, num_el_end+1, 2):
    time_list_el = [] # Tempos de execução da rodada com um número n de elementos.
    for i in range(repeat_exec):
        print("#=-="*30)
        
        start_time = time.time()
        
        # Executa o código para gerar as rodadas até conseguir.
        # Toda vez que ocorre algum erro, as duplas utilizadas na execução anterior são repassadas para a
        # próxima execução, através da variável "duplas_init", para seu arranjo ser alterado.
        duplas_init = []
        while True:
            rodadas = gerar_rodadas(num_el, show_rod, count_show_max, count_time_max, max_time_func(num_el), duplas_init)
            if rodadas[0] == 3: # Caso não de erro, quebra esse loop e segue para o próximo número de elementos
                rodadas = rodadas[-1]
                break
            else: # Se der erro, recomeça a execução com um novo arranjo para duplas.
                duplas_init = rodadas[2]
                time_list_el.append(rodadas[:2]) # Coloca o tempo de execução informando qual o erro ocorrido
        
        end_time = time.time()

        # Exibe as rodadas
        # exibir_rodadas(rodadas, int(num_el/2), num_el)
        
        # Verifica se existe algum erro nas rodadas calculadas
        if verificar(rodadas, num_el):
            rod_error.append(num_el)

        # Tempo de execução
        exec_time = tempo_execucao(start_time, end_time, num_el, show=True)
        time_list_el.append((3, exec_time))

    time_list.append((num_el, time_list_el))
print("#=-="*40)

# Salva todos os tempos no arquivo "tempos.json"
# with open("tempos.json", "w") as f:
#     json.dump(time_list, f)

# Caso for detectado algum erro é avisado aqui
if len(rod_error) > 0:
    for num_el_err in rod_error:
        print(f"Erro na rodada com num_el={num_el_err}")
else:
    print(f"Nenhum erro encontrado! :)")

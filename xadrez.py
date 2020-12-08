import time
import json
from functions import gerar_rodadas, exibir_rodadas, verificar, tempo_execucao

"""
    Este arquivo serve apenas para testes, "gerar_rodadas.py" é quem possui a usabilidade
"""

# Número de elementos. OBS: Essa variável pode ser um número ímpar.
num_el_start = 30
num_el_end = 40
repeat_exec = 1 # Quantas vezes executar a geração de rodadas com n números de elementos

show_rod = False          # Exibir rodada sendo preenchida no console?
freq_show_max = 50000     # Controlam a frequência da exibição da rodada no console
freq_time_max = 50000     # Controlam a frequência da verificação do tempo
num_time_streak = 6       # Número máximo para atingir o tempo máximo de execução
max_time_multiplier = 1.7 # Quanto o tempo máximo é multiplicado quando "num_time_streak" é atingindo

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
        count_max_time = 0    # Número de vezes que o tempo máximo de execução foi atingido
        count_time_streak = 0 # Número de vezes que "num_time_streak" foi atingido

        while True:
            # Toda vez que é atingindo o tempo máximo de execução num_time_streak vezes seguidas, 
            # aumenta o tempo máximo de execução em (max_time_multiplier - 1)*100 % 
            if count_max_time >= num_time_streak:
                count_max_time = 0
                count_time_streak += 1
                print(f"MAX_TIME: {max_time}")
            
            max_time = max_time_func(num_el) * max_time_multiplier**(count_time_streak)
            
            rodadas = gerar_rodadas(num_el, show_rod, freq_show_max, freq_time_max, max_time, duplas_init)
            if rodadas[0] == 3: # Caso não de erro, quebra esse loop e segue para o próximo número de elementos
                rodadas = rodadas[-1]
                break
            else: # Se der erro, recomeça a execução com um novo arranjo para duplas.
                # Conta quantas vezes é atingindo o tempo máximo de execução
                if rodadas[0] == 2: 
                    count_max_time += 1
                    
                duplas_init = rodadas[2]
                time_list_el.append(rodadas[:2]) # Coloca o tempo de execução informando qual o erro ocorrido
        
        end_time = time.time()

        # Exibe as rodadas
        exibir_rodadas(rodadas, int(num_el/2), num_el)
        
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

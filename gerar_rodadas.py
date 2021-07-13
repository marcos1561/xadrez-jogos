import sys
import functions as func

"""
    Primeiro é gerado as rodadas com números sendo place holders para os jogadores, depois eles são substituidos.
    
    Os place holders vão de 0 até o número de jogadores menos um, assim é possível associar cada placeholder com o índice do
    jogador em "elementos"

    Antes de substituir os place holders pelos jogadore e realizado um shuffle em "elementos".
""" 

# Extrai os jogadores da arquivo com os mesmos e calcula qual jogador possui o maior nome (Utilizado para melhor exibir as rodadas)
elementos = [] # Lista contendo os jogadores
long_el = ""   # Nome com maior número de caracteres
with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        person = line.strip()
        if len(person) > 0:
            elementos.append(person)

            if len(person) > len(long_el):
                long_el = person

num_el = len(elementos) # número de jogadores

show_rod = False          # Exibir rodada sendo preenchida no console?
freq_show_max = 50000     # Controlam a frequência da exibição da rodada no console
freq_time_max = 50000     # Controlam a frequência da verificação do tempo
num_time_streak = 6       # Número máximo para atingir o tempo máximo de execução
max_time_multiplier = 1.7 # Quanto o tempo máximo é multiplicado quando "num_time_streak" é atingindo

# Função que calcula o tempo máximo de execução em função do número elementos
# Talvez no seu computar esses coeficientes não funcionem bem
def max_time_func(el):
    return 1.51**(el-26.9)

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
    
    max_time = max_time_func(num_el) * max_time_multiplier**(count_time_streak)
    result = func.gerar_rodadas(num_el, show_rod, freq_show_max, freq_time_max, max_time, duplas_init)

    if result[0] == 3: # Caso não de erro, quebra o loop
        rodadas = result[-1]
        break
    else: # Se der erro, recomeça a execução com um novo arranjo para duplas.
        # Conta quantas vezes é atingindo o tempo máximo de execução
        if result[0] == 2: 
            count_max_time += 1

        duplas_init = result[-1]

func.verificar(rodadas, num_el) # Verifica se ocorreu algum erro

# Realizado o shuffle nos jogadores (numpy já foi importado em "functions.py")
elementos = func.np.array(elementos)
func.np.random.shuffle(elementos)

# Substitui os place holders pelos jogadores
for rodada in rodadas:
    for i in range(len(rodada)):
        dupla = rodada[i]

        x_id = dupla.find("X")
        el_1 = int(dupla[:x_id-1])
        el_2 = int(dupla[x_id+2:])

        person_1 = elementos[el_1]
        person_2 = elementos[el_2]

        rodada[i] =  f"{person_1} X {person_2}"

# Escreva as rodadas no arquivo "rodadas.txt"
rodadas_lines = func.exibir_rodadas(rodadas, int(num_el/2), long_el, show=False)
with open("rodadas.txt", encoding="UTF-8", mode="w") as file:
    for line in rodadas_lines:
        file.write(line) 
        file.write("\n")
    
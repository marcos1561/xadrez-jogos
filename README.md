# xadrez-jogos
Pequeno projeto para gerar partidas de xadrez, separadas em rodadas, em um conjunto de n jogadores.

O objetivo do projeto e gerar todos os jogos possíveis dentre os n jogadores e separar esses jogos em rodadas, de tal forma que todos os jogadores jogam uma única vez por rodada.

OBS: 
* Esse projeto não é exclusivo para xadrez, se aplica para qualquer jogo que seja 1 x 1.  
* O arquivo que possui usabilidade é "gerar_rodadas.py", o arquivo "xadrez.py" serve para testes.  

-> **Nos tutorias a seguir será pressuposto que o python está no PATH e que você está na pasta do repositório.**

# Instalando dependências
```powershell
pip install -r requirements.txt
```

# Como usar
O input aceitado é um arquivo .txt contendo os jogadores separados por linha. Ex:

Nome_1  
Nome_2  
Nome_3  
Nome_4  

OBS: 
* É esperado que a codificação desse arquivo seja utf-8.
* Agora a quantidade de jogadores também pode ser ímpar, mas nesse caso o tempo de execução é bem maior.

Então, apenas é necessário executar o seguinte comando no terminal.  

  ```powershell
  python .\gerar_rodadas.py .\jogadores.txt
  ```
 
Após a execução do script, será gerado o arquivo "rodadas.txt" (a codificação utilizada é utf-8) contendo as rodadas.  
Um possível resultado para o arquivo exemplo é:

|Nome_3 X Nome_2|Nome_3 X Nome_4|Nome_1 X Nome_3|  
|Nome_1 X Nome_4|Nome_1 X Nome_2|Nome_4 X Nome_2|

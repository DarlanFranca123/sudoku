'''
Equipe:
Darlan Vitor Albuquerque França: 580497
Diego Lugano Oliveira Lima Pereira: 580472
Luis Otavio Almeida Martins: 587770
'''

from .testar_tabuleiro import testar_tabuleiro 

# Dicionário de conversão de letras para índices de linha
LETRA_PARA_NUMERO = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8
}

NUMERO_PARA_LETRA = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I'
}

def ler_linha(linha_str):
    try:
        coordenada_str, valor_str = linha_str.split(':')
        char_coluna, char_linha = coordenada_str.split(',')
    except ValueError:
        raise ValueError("Formato de entrada inválido.")
    
    indice_linha = int(char_linha.strip()) - 1 
    letra_coluna = char_coluna.strip().upper()

    if letra_coluna not in LETRA_PARA_NUMERO:
        raise ValueError(f"Letra de coluna '{letra_coluna}' inválida. Use de A a I.")
    indice_coluna = LETRA_PARA_NUMERO[letra_coluna]
    valor = int(valor_str.strip())  
    # Tratamento de erros e entradas
    if not (0 <= indice_linha < 9 and 0 <= indice_coluna < 9):
        raise ValueError(f"Posição '{letra_coluna},{indice_linha+1}' está fora dos limites.")
    
    if not (1 <= valor <= 9):
        raise ValueError(f"Valor '{valor}' inválido. Deve ser entre 1 e 9.")

    return (indice_coluna, indice_linha, valor)

def ler_linha_batch(linha_str):

    coordenada_str, valor_str = linha_str.split(':')
    char_coluna, char_linha = coordenada_str.split(',')
  
    
    indice_linha = int(char_linha.strip()) - 1 
    letra_coluna = char_coluna.strip().upper()
    valor = int(valor_str.strip())  


    return (letra_coluna, indice_linha, valor)


def ler_pergunta_interativo(linha_entrada):
    if linha_entrada[0] != '?':
        raise ValueError("A pergunta deve começar com '?'")
    coordenada_str = linha_entrada[1:].replace(" ", "") # Exclui o ? e os espaços em branco
    try:
        coluna_str, linha_str , _ = ler_linha(coordenada_str + ":1") # Usamos aqui a lógica de ler_linha para validar a entrada, para nao ter que reescrever
    except ValueError as error:
        raise ValueError(f"Erro ao ler a pergunta: {error}") # Jogamos o erro de ler_linha para o usuário
    return (coluna_str, linha_str) # Retorna a coluna e a linha 

def ler_remocao_interativo(linha_entrada):
    if linha_entrada[0] != '!':
        raise ValueError("A remoção deve começar com '!'")
    coordenada_str = linha_entrada[1:].replace(" ", "")  # Exclui o ! e os espaços em branco
    try:
        coluna_str, linha_str, _ = ler_linha(coordenada_str + ":1")  # Usamos aqui a lógica de ler_linha para validar a entrada
    except ValueError as error:
        raise ValueError(f"Erro ao ler a remoção: {error}")  # Jogamos o erro de ler_linha para o usuário
    return (coluna_str, linha_str)  # Retorna a coluna e a linha

def criar_tabuleiro_inicial(caminho):
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    contador = 0
    try:
        with open(caminho, 'r') as arquivo:
            for linha_arquivo in arquivo:
                linha_limpa = linha_arquivo.strip()
                if linha_limpa:  # Pula linhas completamente vazias
                    contador += 1
                    try:
                        col_idx, linha_idx, valor = ler_linha(linha_limpa)
                        tabuleiro[linha_idx][col_idx] = valor
                    except ValueError as erro:
                        # Captura o erro de ler_linha e adiciona o número da linha para contexto
                        raise ValueError(f"Erro no arquivo na {linha_limpa}: {erro}")

    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: O arquivo de configuração não foi encontrado.")
    
    if not (1 <= contador <= 81):
        raise ValueError(f"O numero de entradas é inválido")

    # Após preencher, valida as regras do Sudoku para a configuração inicial
    if not testar_tabuleiro(tabuleiro):
        raise ValueError("Configuração do tabuleiro inválida em relação às regras do Sudoku.")
        
    return tabuleiro

def criar_tabuleiro_inicial_batch(caminho):
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    contador = 0
    try:
        with open(caminho, 'r') as arquivo:
            for linha_arquivo in arquivo:
                linha_limpa = linha_arquivo.strip()
                if linha_limpa:  # Pula linhas completamente vazias
                    contador += 1
                    try:
                        col_idx, linha_idx, valor = ler_linha(linha_limpa)
                        if tabuleiro[linha_idx][col_idx] == 0:
                            tabuleiro[linha_idx][col_idx] = valor
                        else:
                            raise ValueError("Repetido")
                    except ValueError as erro:
                        # Captura o erro de ler_linha e adiciona o número da linha para contexto
                        raise ValueError(f"Erro no arquivo na {linha_limpa}: {erro}")

    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: O arquivo de configuração não foi encontrado.")
    

    # Após preencher, valida as regras do Sudoku para a configuração inicial
    if not testar_tabuleiro(tabuleiro):
        raise ValueError("Configuração do tabuleiro inválida em relação às regras do Sudoku.")
        
    return tabuleiro

RED = "\033[91m"
RESET = "\033[0m"

def imprimir_tabuleiro(tabuleiro, pistas):
    linhas = []

    # Topo: letra alinhada com o centro de cada célula (o segundo caractere dos === ou ---)
    topo = "   "  # Começa com 2 espaços para alinhar com ++
    for i in range(9):
        topo += " " + NUMERO_PARA_LETRA[i] + "  "  # 4 posições por coluna: espaço + letra + 2 espaços
        if i in [2, 5]:
            topo += " "
    topo = topo.rstrip()
    linhas.append(topo)

    for i in range(9):
        if i % 3 == 0 and i != 0:
            linhas.append(" ++===+===+===++===+===+===++===+===+===++")
        else:
            linhas.append(" ++---+---+---++---+---+---++---+---+---++")

        linha = f"{i+1}||"

        for j in range(9):
            val = tabuleiro[i][j]
            if val != 0:
                if (i, j) in pistas:
                    celula = f" {RED}{val}{RESET} "
                else:
                    celula = f" {val} "
            else:
                celula = "   "
            linha += celula

            if j == 8:
                linha += f"||{i+1}"
            elif (j + 1) % 3 == 0:
                linha += "||"
            else:
                linha += "|"

        linhas.append(linha)

    linhas.append(" ++---+---+---++---+---+---++---+---+---++")
    linhas.append(topo)

    return print("\n".join(linhas))


def tabuleiro_cheio(tabuleiro):
    # Verifica se o tabuleiro está cheio (sem zeros)
    for linha in tabuleiro: 
        if 0 in linha: 
            return False
    return True

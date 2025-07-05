from testar_tabuleiro import testar_tabuleiro 

# Dicionário de conversão de letras para índices de linha
LETRA_PARA_LINHA = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8
}

def ler_linha(linha_str):

    coordenada, valor_str = linha_str.split(':')
        
    letra_linha, str_coluna = coordenada.split(',')
    
    if letra_linha.upper() not in LETRA_PARA_LINHA:
        raise ValueError(f"Coluna '{letra_linha}' inválida.")
        
    valor = int(valor_str.strip())
    col_idx = int(str_coluna.strip()) - 1
    linha_idx = LETRA_PARA_LINHA[letra_linha.upper()]

    # Verificação de limites
    if not (0 <= linha_idx < 9 and 0 <= col_idx < 9):
        raise ValueError(f"Posição '{letra_linha},{str_coluna}' está fora dos limites do tabuleiro.")
    
    if not (1 <= valor <= 9):
        raise ValueError(f"Valor '{valor}' inválido.")

    return (col_idx, linha_idx, valor)

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
                        tabuleiro[col_idx][linha_idx] = valor
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

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for numero in linha: 
            print(numero, end=" ")
        print()

def validar_entradas_jogadas(caminho):
    # Lógica a ser implementada
    return 0
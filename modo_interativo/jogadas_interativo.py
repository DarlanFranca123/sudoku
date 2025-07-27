'''
Equipe:
Darlan Vitor Albuquerque França: 580497
Diego Lugano Oliveira Lima Pereira: 580472
Luis Otavio Almeida Martins: 587770
'''
from funcoes_gerais.validar_entradas import NUMERO_PARA_LETRA

def possibilidades_interativo(tabuleiro, linha, coluna, pistas):    
    # Retorna uma lista de números possíveis para a posição (linha, coluna)

    if (linha, coluna) in pistas:
        # A lógica para converter para letra/número precisaria ser ajustada se usada aqui
        raise ValueError(f"A posição ({NUMERO_PARA_LETRA[coluna]}, {linha + 1}) é uma pista e não pode ser alterada.")

    numeros_possiveis = list(range(1, 10))  # Números de 1 a 9

    # 1. Verifica a Linha
    for j in range(9):
        numero = tabuleiro[linha][j]
        if numero in numeros_possiveis:
            numeros_possiveis.remove(numero)

    # 2. Verifica a coluna
    for i in range(9):
        numero = tabuleiro[i][coluna]
        if numero in numeros_possiveis:
            numeros_possiveis.remove(numero)

    # 3. Verifica o Quadrante 3x3
    quadrante_linha_comeco = (linha // 3) * 3
    quadrante_coluna_comeco = (coluna // 3) * 3

    for i in range(quadrante_linha_comeco, quadrante_linha_comeco + 3):
        for j in range(quadrante_coluna_comeco, quadrante_coluna_comeco + 3):
            numero = tabuleiro[i][j]
            if numero in numeros_possiveis:
                numeros_possiveis.remove(numero)
    
    return numeros_possiveis
def remocao_interativo(tabuleiro, linha, coluna, pistas):

    if (linha,coluna) in pistas:
        raise ValueError(f"A posição é uma pista e não pode ser removida.")
    else: 
        if tabuleiro[linha][coluna] == 0:
            raise ValueError(f"A posição {NUMERO_PARA_LETRA[coluna]},{linha + 1} já está vazia.")
        else: 
            tabuleiro[linha][coluna] = 0
            print(f"Valor removido da posição ({NUMERO_PARA_LETRA[coluna]}, {linha + 1}).")
    return tabuleiro
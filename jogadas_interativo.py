
def possibilidades_interativo(tabuleiro, coluna, linha):    
    # Retorna uma lista de números possíveis para a posição (coluna, linha)
    numeros_possiveis = list(range(1, 10))  # Números de 1 a 9
    # Verifica a coluna
    for numero in tabuleiro[coluna]:
        if numero != 0 and numero in numeros_possiveis:
            numeros_possiveis.remove(numero)
    # Verifica a linha
    for i in range(9):
        if tabuleiro[i][linha] != 0 and tabuleiro[i][linha] in numeros_possiveis:
            numeros_possiveis.remove(tabuleiro[i][linha])
    # Verifica o quadrante 3x3
    quadrante_coluna_comeco = (coluna // 3) * 3
    quadrante_linha_comeco = (linha // 3) * 3

    for i in range(quadrante_coluna_comeco, quadrante_coluna_comeco + 3):
        for j in range(quadrante_linha_comeco, quadrante_linha_comeco + 3):
            if tabuleiro[i][j] != 0 and tabuleiro[i][j] in numeros_possiveis:
                numeros_possiveis.remove(tabuleiro[i][j])
    return numeros_possiveis
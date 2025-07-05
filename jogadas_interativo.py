from validar_entradas import NUMERO_PARA_LETRA

def possibilidades_interativo(tabuleiro, coluna, linha, pistas):    
    # Retorna uma lista de números possíveis para a posição (coluna, linha)
    if (coluna, linha) in pistas:
        raise ValueError(f"A posição ({NUMERO_PARA_LETRA[coluna]}, {linha + 1}) é uma pista e não pode ser alterada.")
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
    
    if(tabuleiro[linha][coluna] != 0):
        print(f"Observação: A posição ({NUMERO_PARA_LETRA[coluna]}, {linha + 1}) já está preenchida com o valor {tabuleiro[linha][coluna]}.")
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
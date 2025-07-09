
def encontrar_primeira_vazia(tab):
    for i in range(9):
        for j in range(9):
            if tab[i][j]==0:
                return (i,j)
    return None

def validar_possivel_numero(tab, numero, posicao):
    # Vou checar se consigo colocar o numero no tabuleiro na posicao fornecida
    linha, coluna = posicao
    # Checando a linha
    for j in range(9):
        if tab[linha][j] == numero and coluna != j:
            return False
    # Checando a coluna
    for i in range(9):
        if tab[i][coluna] == numero and coluna != i:
            return False
    # Checando o quadrante
    piso_linha = linha // 3
    piso_coluna = coluna // 3
    # Armazenam o primeiro quadrado do quadrante da posição que estamos lidando
    for i in range(piso_linha*3, piso_linha*3 + 3):
        for j in range(piso_coluna*3, piso_coluna*3 + 3):
            if tab[i][j] == numero and (i,j) != posicao:
                return False
    return True    

def backtracking(tab):

    prox_vazia = encontrar_primeira_vazia(tab)

    if not prox_vazia: # Isso quer dizer que o tabuleiro está completo 
        return True
    else: 
        linha, coluna = prox_vazia
    
    for num in range(1,10):
        if validar_possivel_numero(tab,num, (linha,coluna)): # Testo se é possível colocar o número na posição
            tab[linha][coluna] = num # Coloco o número
            if backtracking(tab): # Vejo se é possível terminar com esse número e, caso seja, retorno True
                return True 
            tab[linha][coluna] = 0 # Caso contrário, reinicio o valor da posição para 0 e testo o próximo valor
    return False

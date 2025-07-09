import copy
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

def solucoes(tab):
    tab_sol = [None]
    contador = [0]
    backtracking(tab,contador, tab_sol)
    return contador[0], tab_sol[0]

def backtracking(tab, contador, tab_sol):

    if contador[0] >= 2:
        return True

    prox_vazia = encontrar_primeira_vazia(tab)

    if not prox_vazia: # Isso quer dizer que o tabuleiro está completo 
        contador[0] += 1
        if contador[0] == 1: # Se só foi encontrada uma solução, vamos atrás de outra e salvar a atual
            tab_sol[0] = copy.deepcopy(tab)
        return contador[0] >= 2 # Se tem ao menos duas, então retornarnamos True, ou seja, que já terminamos de procurar.
    else: 
        linha, coluna = prox_vazia
    
    for num in range(1,10):
        if validar_possivel_numero(tab,num, (linha,coluna)): # Testo se é possível colocar o número na posição
            tab[linha][coluna] = num # Coloco o número
            if backtracking(tab, contador, tab_sol): # Se tem mais de duas soluções quando eu coloco esse num na posição, então vamos retornando True nos outros vértices
                return True 
            tab[linha][coluna] = 0 # Caso contrário, testemos outros números para essa posição.
    return False # Caso não foram encontradas ao menos duas soluções


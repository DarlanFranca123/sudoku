'''
Equipe:
Darlan Vitor Albuquerque França
Diego Lugano Oliveira Lima Pereira
Luis Otavio Almeida Martins

'''
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
        if tab[i][coluna] == numero and linha != i:
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
    # Dado um tabuleiro, retornará o quantas solucoes tem(no máximo 2), qual a primeira e a segunda, podendo, ambas,
    # serem vazias
    tab_sol_1 = [None] 
    tab_sol_2 = [None]
    contador = [0]
    backtracking(tab,contador, tab_sol_1, tab_sol_2)
    return contador[0], tab_sol_1[0], tab_sol_2[0]

def backtracking(tab, contador, tab_sol_1, tab_sol_2):

    # Se já encontramos 2 soluções, paramos a busca.
    if contador[0] >= 2:
        return True

    prox_vazia = encontrar_primeira_vazia(tab)

    # Se não há mais casas vazias, encontramos uma solução completa.
    if not prox_vazia: 
        contador[0] += 1 # Incrementa o contador de soluções.
        
        if contador[0] == 1: # Salva a primeira solução e vai procurar a outra, retornando False.
            tab_sol_1[0] = copy.deepcopy(tab)
            
        elif contador[0] == 2: # Salva a segunda solução e para o código.
            tab_sol_2[0] = copy.deepcopy(tab)
            
        # Retorna True se já achamos 2, para parar a busca completamente.
        return contador[0] >= 2
    else: 
        linha, coluna = prox_vazia

    for num in range(1, 10):
        if validar_possivel_numero(tab, num, (linha, coluna)):
            tab[linha][coluna] = num # Faz a jogada.
            if backtracking(tab, contador, tab_sol_1, tab_sol_2):
                return True # Se foram encontradas duas soluções, manda o código parar e retorna paras os vértices acima
            
            # Se a chamada recursiva retornou False, desfazemos a jogada para tentar o próximo número.
            tab[linha][coluna] = 0 
    return False


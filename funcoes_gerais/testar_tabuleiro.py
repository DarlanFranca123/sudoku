'''
Equipe:
Darlan Vitor Albuquerque França: 580497
Diego Lugano Oliveira Lima Pereira: 580472
Luis Otavio Almeida Martins: 587770
'''

def nao_duplicados(lista):
    #Dada uma lista de números, verifica se há números duplicados, ignorando zeros.
    numeros = []
    for numero in lista:
        if numero != 0:
            if numero in numeros:
                return False
            numeros.append(numero)
    return True

def testar_tabuleiro(tabuleiro):
    # Verifica linhas
    for linha in tabuleiro:
        if not nao_duplicados(linha):
            return False

    # Verifica colunas
    for col in range(9):
        colunas = [tabuleiro[linha][col] for linha in range(9)]
        if not nao_duplicados(colunas):
            return False

    # Verifica quadrantes 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrante = []
            for linha in range(i, i + 3):
                for coluna in range(j, j + 3):
                    quadrante.append(tabuleiro[linha][coluna])
            if not nao_duplicados(quadrante):
                return False

    return True


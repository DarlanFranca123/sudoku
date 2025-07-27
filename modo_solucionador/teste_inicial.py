'''
Equipe:
Darlan Vitor Albuquerque França
Diego Lugano Oliveira Lima Pereira
Luis Otavio Almeida Martins

'''
from modo_interativo.jogadas_interativo import possibilidades_interativo
# Aqui, olhando apenas para a linha, coluna e quadrante e reutilizando a logica do modo interativo para
# calcular as possibilidades de entrada disso
def preencher_apenas_uma(tab,pistas):
    for _ in range(81):
        for i in range(9):
            for j in range(9):
                if (i,j) not in pistas and (tab[i][j] == 0): 
                    possibilidades = possibilidades_interativo(tab,i,j,pistas)
                    if len(possibilidades) == 1:
                        tab[i][j] = possibilidades[0]



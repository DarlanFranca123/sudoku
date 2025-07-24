'''
Equipe:
Darlan Vitor Albuquerque França
Diego Lugano Oliveira Lima Pereira
Luis Otavio Almeida Martins
'''
import os
import copy
import sys
from funcoes_gerais.validar_entradas import criar_tabuleiro_inicial_batch, ler_linha, tabuleiro_cheio,ler_linha_batch
from funcoes_gerais.testar_tabuleiro import testar_tabuleiro

def modo_batch(arquivo_pistas, arquivo_jogadas):
    try:
        # Cria o tabuleiro inicial e salva posições das pistas
        tabuleiro = criar_tabuleiro_inicial_batch(arquivo_pistas)
        pistas = [
            (i, j)
            for i in range(9)
            for j in range(9)
            if tabuleiro[i][j] != 0
        ]
    except Exception as e:
        print("Configuração de dicas inválida!")
        return

    try:
        with open(arquivo_jogadas, 'r') as f:
            linhas_jogadas = f.readlines()
    except:
        print("Erro ao abrir o arquivo de jogadas.")
        return

    for linha in linhas_jogadas:
        linha = linha.strip()
        if linha:
            try:
                tabuleiro_temp = copy.deepcopy(tabuleiro) # Cria uma cópia do tabuleiro para validação temporária
                col_idx, linha_idx, valor = ler_linha(linha)

                # Verifica se a jogada está em uma célula com pista
                if (linha_idx, col_idx) in pistas:
                    raise ValueError()

                # Verifica se já há um valor e sobrescreve
                elif tabuleiro[linha_idx][col_idx] != 0:
                    raise ValueError()
                
                # Caso contrário, tenta colocar o valor nessa posicão
                else:   
                    tabuleiro_temp[linha_idx][col_idx] = valor # Registra a jogada no tabuleiro temporário
                
                if not testar_tabuleiro(tabuleiro_temp): # Verifica se a jogada é válida

                    tabuleiro_temp = copy.deepcopy(tabuleiro) # Restaura o tabuleiro original se a jogada for inválida
                    raise ValueError()
        
                else: 
                    tabuleiro = tabuleiro_temp # Atualiza o tabuleiro original com o temporário se a jogada for válida

            except ValueError as erro:
                col_letra, linha_idx, valor = ler_linha_batch(linha)
                print(f"A jogada ({col_letra},{linha_idx+1}) = {valor} é inválida!")

    if tabuleiro_cheio(tabuleiro):
        print("A grade foi preenchida com sucesso!")
    else:
        print("A grade não foi preenchida!")


    


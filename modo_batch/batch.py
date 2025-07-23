import os
import copy
import sys
from funcoes_gerais.validar_entradas import criar_tabuleiro_inicial, ler_linha, imprimir_tabuleiro, tabuleiro_cheio, LETRA_PARA_NUMERO
from funcoes_gerais.testar_tabuleiro import testar_tabuleiro

NUMERO_PARA_LETRA = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I'}

def modo_batch(arquivo_pistas, arquivo_jogadas):
    try:
        # Cria o tabuleiro inicial e salva posições das pistas
        tabuleiro = criar_tabuleiro_inicial(arquivo_pistas)
        pistas = [
            (i, j)
            for i in range(9)
            for j in range(9)
            if tabuleiro[i][j] != 0
        ]
        imprimir_tabuleiro(tabuleiro,pistas)
    except Exception as e:
        print("Configuração de pistas inválida!")
        return
    op = input("Deseja prosseguir com o preenchimento usando o segundo arquivo inserido? (S/N?)")
    op = op.strip().upper()

    if op == "S":
        try:
            with open(arquivo_jogadas, 'r') as f:
                linhas_jogadas = f.readlines()
        except:
            print("Erro ao abrir o arquivo de jogadas.")
            return

        for linha in linhas_jogadas:
            linha = linha.strip()
            if not linha:
                continue
            try:
                tabuleiro_temp = copy.deepcopy(tabuleiro) # Cria uma cópia do tabuleiro para validação temporária
                col_idx, linha_idx, valor = ler_linha(linha)

                # Verifica se a jogada está em uma célula com pista
                if (linha_idx, col_idx) in pistas:
                    raise ValueError(f"Essa jogada é inválida pois é uma pista. ")

                # Verifica se já há um valor e sobrescreve
                elif tabuleiro[linha_idx][col_idx] != 0:
                    raise ValueError(f"A jogada é inválida pois essa posição já está preenchida. ")
                
                # Caso contrário, tenta colocar o valoe nessa posicão
                else:   
                    tabuleiro_temp[linha_idx][col_idx] = valor # Registra a jogada no tabuleiro temporário
                
                if not testar_tabuleiro(tabuleiro_temp): # Verifica se a jogada é válida

                    tabuleiro_temp = copy.deepcopy(tabuleiro) # Restaura o tabuleiro original se a jogada for inválida
                    raise ValueError(f"A jogada é inválida pois viola as regras do Sudoku.")
        
                else: 
                    tabuleiro = tabuleiro_temp # Atualiza o tabuleiro original com o temporário se a jogada for válida

            except ValueError as erro:
                print(f"A jogada {linha} é inválida. {erro}")

        if tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro,pistas)
            print("A grade foi preenchida com sucesso!")
        else:
            imprimir_tabuleiro(tabuleiro,pistas)
            print("A grade não foi preenchida!")
    else:
        print("Encerrando...")

    


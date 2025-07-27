'''
Equipe:
Darlan Vitor Albuquerque França: 580497
Diego Lugano Oliveira Lima Pereira: 580472
Luis Otavio Almeida Martins: 587770
'''
import os
import copy
from funcoes_gerais.validar_entradas import criar_tabuleiro_inicial, imprimir_tabuleiro, tabuleiro_cheio
from funcoes_gerais.validar_entradas import ler_linha, ler_pergunta_interativo, ler_remocao_interativo, NUMERO_PARA_LETRA
from funcoes_gerais.testar_tabuleiro import testar_tabuleiro
from .jogadas_interativo import *



def modo_interativo(nome_arquivo):
    # Cria o tabuleiro e salva as pistas iniciais para que elas não sejam sobrepostas ou removidas pelo usuário
    try:
        tabuleiro = criar_tabuleiro_inicial(nome_arquivo)
        pistas = []
        for i, linha in enumerate(tabuleiro):
            for j,valor in enumerate(linha):
                if valor != 0:
                    pistas.append((i, j))
        imprimir_tabuleiro(tabuleiro,pistas)
    except ValueError as e:
        print( f"Erro ao criar o tabuleiro: {e} \nTente novamente!" )
        return
    
    
    while not tabuleiro_cheio(tabuleiro):  # Continua até que o tabuleiro esteja cheio

        linha_str = input("Você está no modo interativo. Entre uma jogada ou operação: \n").strip()

        #Usuário coloca a entrada, podendo ser uma jogada, uma pergunta ou uma remoção

        if not (linha_str[0] == "?" or linha_str[0] == "!"):
            try:    
                tabuleiro_temp = copy.deepcopy(tabuleiro) # Cria uma cópia do tabuleiro para validação temporária
                col_idx, linha_idx, valor = ler_linha(linha_str)

                if (linha_idx, col_idx) in pistas:  # Verifica se a posição é uma pista
                    raise ValueError(f"A posição ({NUMERO_PARA_LETRA[col_idx]}, {linha_idx + 1}) é uma pista e não pode ser alterada.")

                elif tabuleiro[linha_idx][col_idx] != 0:  # Verifica se a posição já está preenchida
                    operacao = input(f"Essa posição já está preenchida com o valor {tabuleiro[linha_idx][col_idx]}.Você deseja sobrescrever? (S/N)") 
                    operacao = operacao.strip().upper() 

                    if operacao == 'S':
                        tabuleiro_temp[linha_idx][col_idx] = valor # Sobrescreve o valor no tabuleiro temporário
                        print(f"O valor {valor} será sobrescrito na posição ({NUMERO_PARA_LETRA[col_idx]}, {linha_idx + 1})")
                    else:
                        print("O valor não foi alterado.")

                else:
                    tabuleiro_temp[linha_idx][col_idx] = valor # Registra a jogada no tabuleiro temporário
                    print(f"Jogada registrada: ({linha_idx + 1}, {col_idx + 1}) = {valor}")

                if not testar_tabuleiro(tabuleiro_temp): # Verifica se a jogada é válida

                    tabuleiro_temp = copy.deepcopy(tabuleiro) # Restaura o tabuleiro original se a jogada for inválida
                    raise ValueError("Jogada inválida pois viola as regras do Sudoku.")
    
                else: 
                    tabuleiro = tabuleiro_temp # Atualiza o tabuleiro original com o temporário se a jogada for válida
                    print(f"Jogada {linha_idx + 1}, {col_idx + 1} = {valor} válida e registrada.")
                os.system('clear')  # Limpa a tela do terminal
                imprimir_tabuleiro(tabuleiro,pistas) # Imprime o tabuleiro atualizado

            except ValueError as error: 
                print(f"{error} \nTente novamente!")

        elif linha_str[0] == '?':
            # Exibe as possibilidades para a posição requisitada
            try:
                col_idx, linha_idx = ler_pergunta_interativo(linha_str)
                possibilidades = possibilidades_interativo(tabuleiro, linha_idx, col_idx, pistas)
                if not possibilidades: #Tratamos diferentemente o caso de não haver possibilidades
                    print(f"Não há possibilidades válidas para a posição ({NUMERO_PARA_LETRA[col_idx]}, {linha_idx + 1}). Tem algo errado!")
                else:
                    possibilidades = sorted(possibilidades) #Apenas sorta a lista de possibilidades
                    print(f"As possibilidades válidas para a posição ({NUMERO_PARA_LETRA[col_idx]}, {linha_idx + 1}) são: {possibilidades}")
            except ValueError as e:
                print(f"Erro: {e} \nTente novamente!")

        elif linha_str[0] == '!':
            # Exclui o valor da posição requisitada, caso ela não seja uma pista
            try: 
                col_idx, linha_idx = ler_remocao_interativo(linha_str)
                tabuleiro = remocao_interativo(tabuleiro, linha_idx, col_idx, pistas)
                os.system('clear')  # Limpa a tela do terminal
                imprimir_tabuleiro(tabuleiro,pistas)  # Imprime o tabuleiro atualizado
            except ValueError as error:
                print(f"Erro: {error} \nTente novamente!")
    print("Parabéns! O tabuleiro está cheio. Você completou o Sudoku!")
        


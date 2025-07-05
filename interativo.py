import os
import copy
from validar_entradas import criar_tabuleiro_inicial , ler_linha , imprimir_tabuleiro
from testar_tabuleiro import testar_tabuleiro


def modo_interativo(nome_arquivo):
    try:
        tabuleiro = criar_tabuleiro_inicial(nome_arquivo)
        pistas = []
        for i, linha in enumerate(tabuleiro):
            for j,valor in enumerate(linha):
                if valor != 0:
                    pistas.append((i, j))
    except ValueError as e:
        return f"Erro ao criar o tabuleiro: {e} \nTente novamente!"
    os.system('clear')  # Limpa a tela do terminal
    for linha in tabuleiro:
        for numero in linha:
            print(numero, end=' ')
        print()
    
    while True:
        linha_str = input("Você está no modo interativo. Entre uma jogada ou operação: \n").strip()
        if not (linha_str[0] == "?" or linha_str[0] == "!"):
            try:    
                tabuleiro_temp = copy.deepcopy(tabuleiro) # Cria uma cópia do tabuleiro para validação temporária
                col_idx, linha_idx, valor = ler_linha(linha_str)

                if (col_idx, linha_idx) in pistas:  # Verifica se a posição é uma pista
                    raise ValueError(f"A posição ({col_idx + 1}, {linha_idx + 1}) é uma pista e não pode ser alterada.")

                elif tabuleiro[col_idx][linha_idx] != 0:  # Verifica se a posição já está preenchida
                    operacao = input(f"Essa posição já está preenchida com o valor {tabuleiro[col_idx][linha_idx]}.Você deseja sobrescrever? (S/N)") 
                    operacao = operacao.strip().upper() 

                    if operacao == 'S':
                        tabuleiro_temp[col_idx][linha_idx] = valor # Sobrescreve o valor no tabuleiro temporário
                        print(f"O valor {valor} será sobrescrito na posição ({linha_idx + 1}, {col_idx + 1})")

                else:
                    tabuleiro_temp[col_idx][linha_idx] = valor # Registra a jogada no tabuleiro temporário
                    print(f"Jogada registrada: ({linha_idx + 1}, {col_idx + 1}) = {valor}")

                if not testar_tabuleiro(tabuleiro_temp): # Verifica se a jogada é válida

                    tabuleiro_temp = copy.deepcopy(tabuleiro) # Restaura o tabuleiro original se a jogada for inválida
                    raise ValueError("Jogada inválida pois viola as regras do Sudoku.")
    
                else: 
                    tabuleiro = tabuleiro_temp # Atualiza o tabuleiro original com o temporário se a jogada for válida
                    print(f"Jogada {linha_idx + 1}, {col_idx + 1} = {valor} válida e registrada.")
                os.system('clear')  # Limpa a tela do terminal
                imprimir_tabuleiro(tabuleiro) # Imprime o tabuleiro atualizado

            except ValueError as error:
                print(f"{error} \nTente novamente!")


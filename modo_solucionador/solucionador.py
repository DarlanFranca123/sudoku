import os
from funcoes_gerais.validar_entradas import criar_tabuleiro_inicial, imprimir_tabuleiro
from .backtracking import backtracking
def modo_solucionador(nome_arquivo):
    try:
        tabuleiro = criar_tabuleiro_inicial(nome_arquivo)
        pistas = []
        for i, linha in enumerate(tabuleiro):
            for j,valor in enumerate(linha):
                if valor != 0:
                    pistas.append((i, j))
    except ValueError as e:
        return f"Erro ao criar o tabuleiro: {e} \nTente novamente!"
    os.system('clear') 
    imprimir_tabuleiro(tabuleiro)
    # Mesma lógica de leitura do modo interativo, copiado e colado de lá
    print("Essa é a configuração inicial de pistas, deseja continuar?")
    # Mostro a configuração inicial de pistas e pergunto ao usuário se ele deseja ver a solução.
    entrada = True
    while entrada:
        op = input("S/N?:")
        op = op.strip().upper()
        if op == "S":
            entrada = False
            if backtracking(tabuleiro): # Procuro uma solução e imprimo, caso exista
                imprimir_tabuleiro(tabuleiro)
                print("Esse é a solução do tabuleiro completa!")
            else:   
                print("Não foi possível encontrar uma solução.")
        elif op == "N":
            print("Terminando modo solucionador")
            entrada = False
        else:
            print("Por favor, digite S ou N:")
    

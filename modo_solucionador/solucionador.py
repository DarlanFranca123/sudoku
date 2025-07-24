'''
Equipe:
Darlan Vitor Albuquerque França
Diego Lugano Oliveira Lima Pereira
Luis Otavio Almeida Martins
'''
import os
from funcoes_gerais.validar_entradas import criar_tabuleiro_inicial, imprimir_tabuleiro, tabuleiro_cheio
from .backtracking import  solucoes
from .teste_inicial import  preencher_apenas_uma
def modo_solucionador(nome_arquivo):
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
    except:
        print(f"Erro Estranho!")
        return 
    # Mesma lógica de leitura do modo interativo, copiado e colado de lá
    print("Essa é a configuração inicial de pistas, deseja continuar?")
    # Mostro a configuração inicial de pistas e pergunto ao usuário se ele deseja ver a solução.
    entrada = True
    while entrada:
        op = input("S/N?:")
        op = op.strip().upper()
        if op == "S":
            entrada = False
            preencher_apenas_uma(tabuleiro,pistas) # Preenche apenas as casas óbvias
            imprimir_tabuleiro(tabuleiro,pistas)
            if tabuleiro_cheio(tabuleiro):
                print("Essa é a solução do Sudoku!")
            else: # Caso nao esteja cheio, daremos ao usuário a opção de utilizar o modo tentativa e erro 
                entrada_2 = True
                while entrada_2:
                    print("O Sudoku não pôde ser completo diretamente com as entradas iniciais, deseja prosseguir a" \
                    " solução com o modo tentativa?")
                    var = input("S/N?:") 
                    var = var.strip().upper()
                    if var == "S":
                        entrada_2 = False
                        contador , solucao_1, solucao_2 = solucoes(tabuleiro)
                        if contador == 0: # Se não tem solução
                            print("Este Sudoku não tem solucao")
                        elif contador == 1: #Se tem apenas uma, imprime essa solucao unica
                            imprimir_tabuleiro(solucao_1,pistas)
                            print(f"Essa é a solução única deste Sudoku!")
                        else: # Tem ao menos duas soluções e printo as duas
                            print("Existe mais de uma solução para essas pistas. É impossível resolver apenas com essas pistas.")
                            print("Essa são duas das possíveis soluçoes para esse Sudoku:")
                            print("Primeira Solução:")
                            imprimir_tabuleiro(solucao_1,pistas)
                            print("Segunda Solução:")
                            imprimir_tabuleiro(solucao_2,pistas)
                    elif var == "N":
                        entrada_2 = False
                        print("Certo, parando programa!")
                    else: # Apenas tratando as entradas do usuário
                        print("Por favor, digite S ou N")
        elif op == "N":
            print("Terminando modo solucionador!")
            entrada = False
        else: # Tratamento de entradas
            print("Por favor, digite S ou N:")
    

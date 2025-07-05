import os
from validar_entradas import criar_tabuleiro_inicial
def modo_interativo(nome_arquivo):
    try:
        tabuleiro = criar_tabuleiro_inicial(nome_arquivo)
    except ValueError as e:
        return f"Erro ao criar o tabuleiro: {e} \nTente novamente!"
    os.system('clear')  # Limpa a tela do terminal
    for linha in tabuleiro:
        for numero in linha:
            print(numero, end=' ')
        print()
    return "Tabuleiro carregado com sucesso."
'''
Equipe:
Darlan Vitor Albuquerque França
Diego Lugano Oliveira Lima Pereira
Luis Otavio Almeida Martins
'''
import sys
from modo_interativo.interativo import modo_interativo
from modo_batch.batch import modo_batch
from modo_solucionador.solucionador import modo_solucionador

def main():
    if len(sys.argv) == 2:
        nome_arquivo = sys.argv[1]
        modo_valido = False
        while modo_valido == False:
            print("Você deseja executar o modo interativo ou solucionador?")
            modo = input("(1) Interativo\n(2) Solucionador\n")
            if modo == "1":
                modo_interativo(nome_arquivo)
                modo_valido = True
            elif modo == "2":
                modo_solucionador(nome_arquivo)
                modo_valido = True
            else:
                print("Opção inválida. Tente novamente.")
    elif len(sys.argv) == 3:
        nome_arquivo_pistas= sys.argv[1]
        nome_arquivo_jogadas = sys.argv[2]
        modo_batch(nome_arquivo_pistas, nome_arquivo_jogadas)
    else: 
        print("Entrada inválida.")

if __name__ == "__main__":
    main()


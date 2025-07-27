## Projeto Sudoku

O projeto consiste em três modos de jogo de **Sudoku**.

## Equipe

* Darlan Vitor Albuquerque França
* Diego Lugano Oliveira Lima Pereira
* Luis Otavio Almeida Martins

## Estrutura do Projeto

O projeto está dividido em três modos principais:

* `modo_interativo`: permite que o usuário resolva o sudoku manualmente.
* `modo_solucionador`: resolve automaticamente o sudoku fornecido.
* `modo_batch`: executa automaticamente várias jogadas a partir de arquivos de pistas e jogadas.

## Execução

O programa principal está no arquivo `sudoku.py`. Você pode executá-lo com os seguintes comandos:

### Modo Interativo ou Solucionador

```bash
python3 sudoku.py arquivo.txt
```

Após rodar, o programa perguntará se você deseja executar:

* `(1) Interativo`
* `(2) Solucionador`

#### Modo Interativo

Permite que o usuário jogue manualmente, interagindo com o tabuleiro:

Inserção de jogadas no formato Coluna, Linha: Valor. Ex: `A,4 : 7`

Remoção de valores no formato !Coluna, Linha. Ex: `!A,4`

Consulta de possibilidades no formato ?Coluna, Linha. Ex: `?A,4`

Ocorre a validação de jogadas, impede a remoção em pistas e se a jogada viola as regras do Sudoku. O tabuleiro é exibido a cada jogada e termina apenas quando todas as casas forem preenchidas corretamente.

#### Modo Solucionador

Resolve o Sudoku em duas etapas:

Preenchimento direto: tenta resolver preenchendo apenas as posições que possuem apenas uma possibilidade levando em consideração a linha, a coluna e o quadrante.

Caso o preenchimento direto não resolva, pergunta ao usuário se ele deseja ir ao modo tentativa e erro usando backtracking.

Se houver mais de uma solução possível, o programa informa que existe mais de uma solução possível e, além disso, imprime duas soluções válidas encontradas.

Caso tenha apenas uma solução possível, a imprime diretamente e, caso não exista solução válida, imprime que não existe nenhuma solução para aquela configuração inicial de pistas.

### Modo Batch

```bash
python3 sudoku.py pistas.txt jogadas.txt
```

Executa as pistas e as jogadas, imprimindo no terminal se o tabuleiro foi completo ou não, e se alguma jogada ou as pistas foram inválidas.


# Pacman

- Implementação dos seguintes algoritmos de busca no jogo do PAC-MAN:
    - A*
    - Têmpera Simulada
    - Subida de Encosta
    - Busca de Custo Uniforme

- Criação de novos labirintos para teste(pequenos, médios e grandes).

- Apresentar relatório sobre os resultados.

Entrada: Estado inicial e estado meta;

Deve retornar: 

a) o número de estados (movimentos) testados

b) o caminho e número de estados para a solução;


Compilação:

A*:

Labirinto Pequeno: python pacman.py -l tinyMaze -p SearchAgent -a fn=astar

Labirinto Médio: python pacman.py -l mediumMaze -p SearchAgent -a fn=astar

Labirinto Grande: python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar


Busca de Custo Uniforme: 

Labirinto Pequeno: python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs

Labirinto Médio: python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

Labirinto Grande: python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs


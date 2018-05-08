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


Compilação nos labirintos criados:

- A*:

        Labirinto Pequeno: 
        
            python pacman.py -l small -p SearchAgent -a fn=astar

        Labirinto Médio:
        
            python pacman.py -l medium -p SearchAgent -a fn=astar

        Labirinto Grande: 
        
            python pacman.py -l big  -z .5 -p SearchAgent -a fn=astar

     - Usando função heurística:

            Distância Manhattan:  python pacman.py -l small -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

            Distância Euclidiana: python pacman.py -l small -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic


- Busca de Custo Uniforme: 

        Labirinto Pequeno: 
        
            python pacman.py -l small -p SearchAgent -a fn=ucs

        Labirinto Médio:
        
            python pacman.py -l medium -p SearchAgent -a fn=ucs

        Labirinto Grande: 
        
            python pacman.py -l big -z .5 -p SearchAgent -a fn=ucs

- Têmpera Simulada:
    
         python pacman.py -l small -p SearchAgent -a fn=sa
    
         python pacman.py -l medium -p SearchAgent -a fn=sa
    
         python pacman.py -l big -z .5 -p SearchAgent -a fn=sa

- Subida de Encosta:
    
         python pacman.py -l small -p SearchAgent -a fn=hc
    
         python pacman.py -l medium -p SearchAgent -a fn=hc
    
         python pacman.py -l big -z .5 -p SearchAgent -a fn=hc
    

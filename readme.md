# Implementação do algoritmo MRFO (Manta Ray Foraging Optimization)

## Este repositório contem uma implementação do algoritmo MRFO.


### O algoritmo MRFO

é baseado no comportamento de forrageamento da raia-manta, que se alimenta de plâncton e pequenos peixes. A raia-manta é um animal que se move lentamente, mas que possui uma grande capacidade de manobra. A raia-manta utiliza o seu corpo para criar um vórtice que atrai o plâncton para perto de sua boca, permitindo que ela se alimente.O algoritmo MRFO utiliza o comportamento de forrageamento da raia-manta para otimizar problemas de otimização.

### As tecnicas utilizada por este algoritmo são:

Forrageamento de Ciclone / Cyclone

Forrageamento em Cadeia / Chain

Forrageamento de Cambalhota (Somersault foraging)


### Caracteristicas da implementação
As bibliotecas numpy e matplotlib são necessárias para a implementação do algoritmo e para a visualização dos resultados.

É definido a função de fitness que a raia-manta irá otimizar. Neste caso o alvo é a bitstring target com valor: [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]

Inicialização: O espaço de busca é definido por um conjunto de limites inferior e superior.

Avaliação de aptidão: Uma função de aptidão é usada para avaliar a qualidade de cada solução. Em que a melhor solução encontrada é armazenada em best_fitness.

A função MRFO recebe como entrada o número de iterações, o número de raias-mantas, a dimensão do espaço de busca, e os limites inferior e superior para a busca.

Esta função é executada 10x para cada método de forrageamento, ao final calculada a média de aptidão da melhor raia-manta para cada iteração.

Por fim é gerado um plot contendo a média da aptidão da melhor raia-manta vs o número de iterações para cada método de forrageamento, permitindo uma comparação visual.

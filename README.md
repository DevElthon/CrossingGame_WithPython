# CrossingGame_WithPython
Jogos de atravessar são famosos desde a internet de escada. Nesse projeto, criei um Crossing Game utilizando a linguagem de programação Python.

Além da linguagem Python, utilizei uma biblioteca chamada "turtle" para criação dos objetos e do jogador. Essa biblioteca é muito útil para criação de jogos, principalmente aqueles com mecânicas simples.

Para criação do jogo primeiro devemos ter alguns passos em mente.

1: O jogador deve poder se movimentar para cima e para baixo.

2: Devemos ter um placar para contabilizar os níveis.

3: Precisamos gerar carros (objetos inimigos) de forma aleatória tanto no eixo x quanto no eixo y, porém com uma velocidade padronizada de acordo com o nível.

4: Ao colidir com um objeto inimigo, o jogo acaba, ou seja, gameover.

5: Quando o jogador chegar do outro lado do mapa, o jogador deverá passar para o próximo nível e reiniciar do ponto inicial.

Tendo esses passos em mente, podemos dividir o jogo entre jogador, gerenciador de carros e placar.

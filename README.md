<h1 align="center">
📄<br>Jogo das Somas
</h1>
 <h3 align="center">
Projeto de um jogo de tabuleiro simples, entitulado "Jogo das Somas" inspirado no famoso jogo japonês Sudoku, requisitado aos alunos do MI-Algoritmos e programação I da Universidade Estadual de Feira de Santana.
</h3>

<h3 align="center">
 - Especificação do problema -
</h3>

<p align="justify">
    Lara e seu irmão Liam são muito amigos e amam jogos eletrônicos, principalmente os de raciocínio. Eles moram em um país de inverno rigoroso, o que os obriga a ficar muito tempo brincando dentro de casa. Eles têm dois jogos favoritos: Sudoku e o Jogo das Somas Esquecidas, este segundo tendo sido desenvolvido por um grupo de estudantes do MI de Algoritmos da UEFS no primeiro semestre de 2022.
    Mas como os irmãozinhos já jogaram muitas vezes esses jogos - tendo sua criatividade aflorada como o quê -, eles inventaram um novo, inspirado nos outros dois. Só tem um problema, nem Liam, nem Lara sabem programar, e eles querem muito transformar a ideia deles em realidade!
    Ficaram sabendo que um novo grupo de estudantes está cursando a mesma disciplina MI Algoritmos na UEFS, e, como o primeiro grupo fez ótimo trabalho, é certo que desta vez não será diferente. Os irmãozinhos só não têm certeza de qual é o melhor nome para o jogo: Soma-Sudoku ou Jogo das Somas 2.0
</p>

<h3 align="center">
 - Requisitos do sistema -
</h3>

<p align="justify">

- O jogo é de tabuleiro e deve ser disputado entre dois jogadores: Jogador 1 e Jogador 2, utilizando um único tabuleiro, com ambos jogando ao mesmo tempo

- O jogo pode ser jogado em dois níveis. No nível 1 o tabuleiro tem as dimensões 4x4, dividido em 4 seções, e no nível 2 o tabuleiro apresenta as dimensões 9x9, dividido em 9 seções.

- Cada uma das seções do tabuleiro é preenchida aleatoriamente com números de 1 a 4 para o nível 1, e números de 1 a 9 para o nível 2, de forma que os números não se repitam em uma mesma seção.

- O tabuleiro deve permanecer oculto aos jogadores. Respectivamente, "a um lado" de cada linha e "abaixo" de cada coluna são armazenados os valores de suas somas, além da soma da diagonal principal do tabuleiro (bônus), que também deve ser calculada. Os valores das somas das linhas e da colunas devem permanecer visíveis aos jogadores. A soma-bônus deve ficar escondida

- A cada rodada, cada jogador escolhe uma seção do tabuleiro e um número a ter a posição revelada, e assim ocorre:

    - Se o número revelado completar uma linha ou coluna do tabuleiro, o jogador acumula a soma daquela linha ou coluna à pontuação;
    
    - Se o número revelado completar uma linha e uma coluna ao mesmo tempo, ambas as somas são acrescidas à pontuação do jogador;
    
    - Se o número revelado completar a diagonal principal do tabuleiro, o jogador acumula o dobro do valor da soma da diagonal.

- Vence o jogador que tiver acumulado a maior pontuação após o tabuleiro ser todo revelado.

</p>

<h3 align="center">
 - Produto -
</h3>

<p align = "justify">
    A implementação do software é feita utilizando linguagem Python e o relatório padronizadoi nos moldes da SBC (Sociedade Brasileira de Computação).
</p>

## Ferramentas utilizadas
- Python

## Git Clone
- git clone https://github.com/felipe-py/Jogos-das-Somas

## Autor
- [Felipe Silva](https://github.com/felipe-py)
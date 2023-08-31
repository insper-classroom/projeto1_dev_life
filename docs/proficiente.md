# Nível Proficiente

Agora que o jogador já consegue se mover pelo mapa, é hora de adicionar algum desafio. Para o nível proficiente, você deve adicionar paredes nos mapas e monstros que se movem aleatoriamente. Ao final desta etapa, o jogo deverá estar mais ou menos assim:

![Jogo Proficiente](img/proficiente.gif)

## Etapa 1: Adicionando paredes

Modifique a função `inicializa_estado` no arquivo `inicializacao.py` para que ele também crie paredes. As paredes também devem ser objetos, assim como os corações e espinhos. No nível proficiente você pode criar as paredes como achar mais fácil. Elas não precisam ser aleatórias então pode ser mais fácil criar uma lista com posições fixas para as paredes. Ao final desta etapa as paredes devem ser desenhadas na tela, ainda sem nenhuma colisão com elas.

## Etapa 2: Adicionando colisão com as paredes

Modifique a função `atualiza_estado` no arquivo `tela_jogo.py` para que o jogador não possa avançar para uma posição onde há uma parede. Caso o jogador tente se mover em direção a uma parede, o jogo deve mostrar uma mensagem dizendo que o jogador não pode se mover naquela direção.

## Etapa 3: Adicionando monstros

Modifique a função `inicializa_estado` para criar monstros. Além do tipo, posição e cor, o dicionário também deve ter as chaves `'vidas'` e `'probabilidade_de_ataque'`. Uma sugestão de valores: `5` vidas e probabilidade de ataque `0.3` (usaremos esses valores na próxima etapa). Ao final desta etapa os monstros devem ser desenhados na tela.

## Etapa 4: Adicionando batalha

Quando o jogador se mover para uma posição onde há um monstro, o seu movimento deve ser impedido. Então um número aleatório entre 0 e 1 deve ser sorteado (sugestão: pesquise sobra a função `random.random()`). Se o número for menor do que a probabilidade de ataque do monstro, o monstro ataca e o jogador perde uma vida. Caso contrário, o jogador ataca e o monstro perde uma vida. Se as vidas do jogador chegarem a zero o jogo acaba. Se as vidas do monstro chegarem a zero, o monstro é removido da lista de objetos e o jogador avança para a posição do monstro.

O jogo deve sempre mostrar uma mensagem indicando o que aconteceu (quem atacou quem e se o monstro morreu).

## Etapa 5: Adicionando movimento aos monstros

Toda vez que o jogador apertar uma tecla para se mover, todos os monstros também devem tentar se mover de forma aleatória. Para isso, para cada monstro, sorteie uma direção aleatória (esquerda, direita, cima, baixo) e veja se o monstro pode se mover para aquela posição, ou seja, se não há nenhum outro objeto no lugar e se a posição ainda está dentro do mapa. Se ele puder se mover para aquela posição, atualize a posição no dicionário.

Ao final desta etapa, o jogo deverá estar similar ao mostrado no gif no começo da página.

Ah sim! Lembre-se sempre de fazer os commits!

**Importante:** consulte e atualize o [checklist de funcionalidades](funcionalidades-implementadas.md) para garantir que cumpriu todas as etapas.

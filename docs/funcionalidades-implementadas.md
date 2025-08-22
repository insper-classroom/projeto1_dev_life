# Funcionalidades Implementadas

As seguintes funcionalidades do projeto foram implementadas:

Coloque aqui o link para o vídeo, de no máximo 2 minutos, do jogo: [LINK VÍDEO](https://linkparaovideo.com)

### [Nível Básico](basico.md)

No nível básico você deve entender o código fornecido e implementar as seguintes funcionalidades (marque com `x` as que já tiver concluido - nós utilizaremos este checklist para corrigir seu projeto):

- [x] Configurar o Git e o GitHub (já deixamos esta primeira tarefa marcada como feita);
- [ ] Implementar a função `gera_posicao_desocupada`;
    - [ ] Devolver uma posição aleatória dentro do mapa;
    - [ ] Adicionar a posição à lista de posições ocupadas.
- [ ] Implementar a função `desenha_tela`:
    - [ ] Mostrar mapa;
    - [ ] Mostrar jogador;
    - [ ] Mostrar objetos;
    - [ ] Mostrar quantidade de vidas (se o jogador tiver menos vidas do que o máximo, o restante deve ser mostrado como corações brancos - exemplo: 🧡🧡🧡🤍🤍);
    - [ ] Mostrar mensagem.
- [ ] Implementar a função `atualiza_estado`:
    - [ ] Mover o jogador;
    - [ ] Impedir o jogador de sair do mapa;
    - [ ] Ao colidir com um coração:
        - [ ] Remover o coração da lista de objetos;
        - [ ] Aumentar uma vida caso ainda não esteja no máximo;
        - [ ] Não aumentar caso contrário;
        - [ ] Adicionar uma mensagem indicando o que aconteceu.
    - [ ] Ao colidir com um espinho:
        - [ ] Diminuir uma vida;
        - [ ] Terminar o jogo caso tenha atingido zero vidas (mudar `estado['tela_atual']`).

### [Nível Proficiente](proficiente.md)

- [ ] Adiciona paredes na inicialização (ainda sem colisão);
- [ ] Adiciona colisão com as paredes:
    - [ ] Impede o movimento do jogador:
    - [ ] Mostra mensagem na tela.
- [ ] Adiciona monstros:
    - [ ] Sorteia posições aleatórias para os monstros;
    - [ ] Adiciona `'vida'` e `'probabilidade_de_ataque'` aos monstros;
    - [ ] Mostra monstros na tela.
- [ ] Implementa sistema de batalha:
    - [ ] Verifica se a nova posição do jogador está ocupada por um monstro e impede o movimento;
    - [ ] Sorteia um número aleatório;
    - [ ] Verifica quem ataca quem e diminui as vidas do alvo;
    - [ ] Se o jogador morrer, acaba o jogo;
    - [ ] Se o monstro morrer, o monstro é removido da lista e o jogador avança para a posição do monstro;
    - [ ] Mostra mensagem na tela.
- [ ] Implementa movimentação aleatória dos monstros:
    - [ ] Sorteia um movimento para cada monstro e tenta andar naquela direção;
    - [ ] Atualiza a posição se for uma posição válida (dentro do mapa e desocupada).

### [Nível Avançado](avancado.md)

- [ ] Funcionalidade 1: Personagem centralizado na tela e mapa maior do que a janela;
- [ ] Funcionalidade 2: Diferentes tipos de inimigos;
- [ ] Funcionalidade 3: Chefão;
- [ ] Funcionalidade 4: Sala secreta;
- [ ] Funcionalidade 5: Sistema de experiência e níveis;
- [ ] Funcionalidade 6: Itens e inventário;
- [ ] Funcionalidade 7: Equipamento e limite de mochila;
- [ ] Funcionalidade 8: Mapa em arquivo;
- [ ] Funcionalidade 9: Monstro cobrinha;
- [ ] Funcionalidade 10: Telas adicionais;
- [ ] Funcionalidade 11: [Sua sugestão validada por um professor - INDIQUE AQUI O NOME DO PROFESSOR QUE VALIDOU SUA IDEIA].

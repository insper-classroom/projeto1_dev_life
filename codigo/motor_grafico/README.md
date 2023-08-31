# Mini Documentação das Funções do Motor Gráfico

Este documento apresenta as funções disponíveis para desenhar strings no terminal. Você não precisa (nem é esperado) entender como cada uma dessas funções foi implementada. As informações deste documento deveriam ser suficientes para você decidir quais funções usar para cada situação, quais deveriam ser os argumentos de cada uma e qual é o efeito desejado.

As funções utilizam internamente o módulo curses do Python. Se você estiver no Mac ou Linux, a sua instalação do Python já deve conter esse módulo. Se estiver no Windows, será necessário instalar o módulo `windows-curses` (como discutido no README do projeto).

Alternativamente, existe outra implementação usando outra biblioteca que utilizaremos em breve, o PyGame. Para utilizá-la você deve primeiro instalar o PyGame com o comando `pip install pygame` e então modificar a linha 9 do arquivo `codigo/motor_grafico/__init__.py` (`MOTOR = 'curses') para (`MOTOR = 'pygame'`).

As funções a seguir são utilizadas para dois fins: desenhar strings na tela e receber a tecla apertada pelo usuário. Para desenhar strings na tela existem 3 etapas importantes:

1. Apagar a tela anterior;
2. Desenhar na tela atual;
3. Mostrar a tela atual.

Enquanto você não realizar a etapa 3 (mostrar a tela atual), a última tela continuará visível para o usuário. Ou seja, você pode continuar desenhando na tela o quanto quiser antes de efetivamente mostrá-la para o usuário.

Agora sim, vamos às explicações de cada função disponibilizada.

## `chama_funcao_jogo(funcao)`

Esta função já é chamada no arquivo `jogo.py`. Você não precisa mais chamá-la em nenhum outro lugar.

Essencialmente, ela é responsável por realizar algumas inicializações e então chamar a sua função que executa o jogo.

A sua função `jogo` é a porta de entrada do seu programa. A partir dessa função, todas as funcionalidades são implementadas. É como se o código do programa só chamasse essa função.

A função `jogo` deve receber 3 argumentos, nesta ordem:

- `janela`: é uma estrutura de dados que armazena informações sobre a janela. Você não precisa entender o que ela guarda, mas deve passá-la para as funções que recebem uma janela como argumento. Por exemplo, quando for desenhar uma string, você deve passar a janela como argumento.
- `largura_janela`: é a largura da janela **em caracteres**. Ou seja, se `largura_janela` for 20, significa que cabem 20 caracteres na horizontal.
- `altura_janela`: é a altura da janela **em caracteres**. Ou seja, se `altura_janela` for 20, significa que cabem 20 caracteres na vertical.

## `pega_tecla_apertada(janela)`

Esta função recebe uma janela como argumento (a mesma que você recebe na função `jogo` acima). Ela se comporta como o `input()`: o código ficará parado até que o usuário aperte alguma tecla. Com a diferença que assim que o usuário apertar qualquer tecla, ela devolve a tecla apertada (no `input()` o usuário precisa apertar `ENTER` para concluir).

A função devolve a tecla apertada. Os valores possíveis para as teclas são as strings:

- `'ENTER'`: a tecla ENTER foi apertada
- `'ESCAPE'`: a tecla ESC foi apertada
- `'ESPACO'`: a tecla ESPAÇO foi apertada
- `'ESQUERDA'`: a seta para a esquerda foi apertada
- `'DIREITA'`: a seta para a direita foi apertada
- `'CIMA'`: a seta para a cima foi apertada
- `'BAIXO'`: a seta para a baixo foi apertada
- 'a': a tecla A foi apertada
- ...
- 'z': a tecla Z foi apertada

Caso alguma outra tecla seja apertada, será devolvido um número inteiro. Você pode consultar a [documentação do módulo curses](https://docs.python.org/3/library/curses.html#constants) para mais informações sobre esses outros casos.

## `preenche_fundo(janela, cor_rgb)`

Esta função recebe a janela, como discutido acima, e uma cor, representada por uma lista de 3 elementos. Cada elemento dessa lista representa a intensidade de vermelho, verde e azul, respectivamente, em uma escala de 0 a 255.

A função preenche toda a tela com a cor solicitada, apagando qualquer conteúdo que estivesse desenhado anteriormente.

**Importante:** ao chamar esta função, a tela ainda não mostrará o resultado. Para mostrar o resultado para o usuário é necessário chamar a função `mostra_janela(janela)` abaixo.

## `desenha_string(janela, x, y, string, cor_fundo, cor_texto)`

Esta função é provavelmente a função que você vai mais utilizar. Ela recebe uma janela, uma posição (x, y) (em caracteres, logo precisam ser números inteiros), uma string, e duas cores, uma para o fundo e outra para o texto. A função desenha a string a partir da posição (x, y) com as cores especificadas.

Imagine que a janela possui 5 caracteres de altura por 10 de largura. Se você desenhar a string `"Olá"` na posição `x = 3` e `y = 1`, o resultado será mais ou menos assim (preenchemos com `'.'` as outras posições para facilitar a visualização):

```
..........
...Olá....
..........
..........
..........
```

Note que a posição do canto superior esquerdo é (0, 0).

## `mostra_janela(janela)`

Esta função deve ser chamada uma vez a cada frame. Ela mostra tudo o que foi desenhado desde o último frame apresentado. Já chamamos esta função no final da função `desenha_tela`, então você não deve chamá-la novamente em outro lugar.
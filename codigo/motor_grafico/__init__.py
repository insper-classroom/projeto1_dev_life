'''
Neste arquivo são disponibilizadas as funções criadas pelos professores para o jogo. 
Você não precisa entender como elas funcionam, mas pode dar uma olhada se quiser. O que você 
precisa saber é o que elas fazem: elas são usadas para desenhar as telas e atualizar o estado do jogo.
'''

from .constantes_do_motor import *
# Opções disponíveis: 'curses' e 'pygame'
MOTOR = 'curses'


if MOTOR == 'curses':
    from . import motor_curses as motor
elif MOTOR == 'pygame':
    from . import motor_pygame as motor
else:
    raise ImportError('Motor gráfico não encontrado')


def chama_funcao_jogo(funcao):
    """
    Executa a função passada como parâmetro. Esta função é usada para chamar a função jogo().

    Essa função é necessária para fazer algumas inicializações. Você não precisa entender
    o que está acontecendo aqui.
    """
    motor.chama_funcao_jogo(funcao)


def pega_tecla_apertada(janela):
    """
    Retorna a tecla que foi apertada pelo jogador. Esta função é semelhante a uma função
    input(): ela espera que o jogador aperte uma tecla e retorna qual tecla foi apertada.

    Enquanto o jogador não apertar uma tecla, a função fica travada.
    """
    return motor.pega_tecla_apertada(janela)


def preenche_fundo(janela, cor_rgb):
    """
    Preenche o fundo da janela com a cor passada como parâmetro.
    A cor deve ser uma lista com três valores entre 0 e 255, que representam a quantidade
    de vermelho, verde e azul, respectivamente.

    Exemplo: [255, 0, 0] é vermelho, [0, 255, 0] é verde, [0, 0, 255] é azul, [255, 255, 255]

    A tela inteira será preenchida com a cor passada como parâmetro, ou seja, quaisquer elementos
    que já estiverem na tela serão apagados.
    """
    motor.preenche_fundo(janela, cor_rgb)


def desenha_string(janela, x, y, string, cor_fundo, cor_texto):
    """
    Desenha uma string na janela, na posição (x, y), com o fundo da cor cor_fundo e o texto
    da cor cor_texto.

    A cor do fundo e do texto devem ser uma lista com três valores entre 0 e 255, que representam
    a quantidade de vermelho, verde e azul, respectivamente.

    Exemplo: [255, 0, 0] é vermelho, [0, 255, 0] é verde, [0, 0, 255] é azul, [255, 255, 255]

    A string será desenhada na posição (x, y) da janela. A posição (0, 0) é o canto superior
    esquerdo da janela. A posição (x, y) é a posição do caractere mais à esquerda da string.

    Se já houver algum caractere na posição (x, y), ele será apagado e substituído pela string
    passada como parâmetro.
    """
    motor.desenha_string(janela, x, y, string, cor_fundo, cor_texto)


def mostra_janela(janela):
    """
    Mostra a janela na tela. Esta função deve ser chamada ao final de cada iteração do loop.

    A janela só é mostrada na tela quando a função mostra_janela é chamada. Se você não chamar
    a função mostra_janela, a janela não será mostrada na tela.
    """
    motor.mostra_janela(janela)

'''
Neste arquivo são disponibilizadas as funções criadas pelos professores para o jogo. 
Essas funções utilizam o módulo curses para desenhar strings na tela e ler as teclas apertadas pelo jogador.
Você não precisa entender como elas funcionam, mas pode dar uma olhada se quiser.
'''
import curses

from . import constantes_do_motor as consts


def chama_funcao_jogo(jogo):
    def jogo_wrapper(tela):
        # Verifica tamanho disponível no terminal (em caracteres)
        altura_tela, largura_tela = tela.getmaxyx()
        
        # Cria janela na posição (0, 0)
        janela = curses.newwin(altura_tela, largura_tela, 0, 0)
        
        # Aceita teclas especiais
        janela.keypad(True)
        # Esconde o cursor
        curses.curs_set(0)

        # Chama função jogo
        jogo(janela, altura_tela, largura_tela)
    curses.wrapper(jogo_wrapper)


def pega_tecla_apertada(janela):
    # Pega a tecla apertada
    tecla = janela.getch()

    # Mapeia teclas do curses para valores das constantes
    # do motor gráfico. Isso é necessário porque o curses
    # usa números para representar as teclas especiais
    # (setas, enter, escape, etc.) e o motor gráfico
    # usa strings.
    mapeamento_teclas = {
        curses.KEY_UP: consts.SETA_CIMA,
        curses.KEY_DOWN: consts.SETA_BAIXO,
        curses.KEY_LEFT: consts.SETA_ESQUERDA,
        curses.KEY_RIGHT: consts.SETA_DIREITA,
        curses.KEY_ENTER: consts.ENTER,
        ord(' '): consts.ESPACO,
        27: consts.ESCAPE,
    }
    if tecla in mapeamento_teclas:
        return mapeamento_teclas[tecla]
    # Mapeia letras de números para strings
    if ord('a') <= tecla <= ord('z') or ord('A') <= tecla <= ord('Z'):
        return chr(tecla)
    # Neste caso, a tecla não está entre as que sabemos mapear
    # então retornamos o valor da tecla diretamente
    return tecla


def preenche_fundo(janela, cor_rgb):
    """
    Limpa a janela e preenche o fundo com a cor especificada.
    Todas as posições serão preenchidas com a string ' '.

    A cor é uma lista com 3 elementos, cada um representando a intensidade de vermelho, verde e azul no
    intervalo de 0 a 255.
    """
    janela.clear()
    id_par = __pega_par_de_cores(cor_rgb, cor_rgb)
    janela.bkgd(' ', curses.color_pair(id_par))


def desenha_string(janela, x, y, string, cor_fundo, cor_texto):
    """
    Desenha uma string na janela, na posição (x, y), com as cores
    especificadas.

    A posição (0, 0) é a esquerda superior da janela.
    cor_fundo e cor_texto são listas com 3 elementos, cada um
    representando a intensidade de vermelho, verde e azul no 
    intervalo de 0 a 255.
    """
    id_par = __pega_par_de_cores(cor_fundo, cor_texto)
    janela.addstr(y, x, string, curses.color_pair(id_par))


def mostra_janela(janela):
    janela.refresh()


# As funções abaixo são usadas internamente pelo motor gráfico
# e não precisam ser chamadas pelo jogo.
# Dicionário que mapeia cores do jogo para cores do curses
__CORES_E_IDS = {}
__PARES_E_IDS = {}


def __pega_cor(rgb):
    """
    No curses, cores são identificadas por números, que devem
    ser inicializados antes de serem usadas. Para isso, criamos
    um dicionário que mapeia cores do jogo para cores do curses.
    """

    # O módulo curses usa cores de 0 a 1000, então precisamos
    # converter as cores do jogo (que são de 0 a 255) para
    # as cores do curses.
    vermelho, verde, azul = rgb
    vermelho = int(vermelho * 1000 / 255)
    verde = int(verde * 1000 / 255)
    azul = int(azul * 1000 / 255)

    cor = (vermelho, verde, azul)
    if cor in __CORES_E_IDS:
        id_cor = __CORES_E_IDS[cor]
    else:
        id_cor = len(__CORES_E_IDS) + 1
        __CORES_E_IDS[cor] = id_cor
        curses.init_color(id_cor, vermelho, verde, azul)
    return id_cor


def __pega_par_de_cores(cor_de_fundo, cor_de_frente):
    """
    No curses, para usar cores, devemos criar um par de cores
    (uma cor de fundo e uma cor de frente) e usar esse par
    para desenhar na tela. Para isso, criamos um dicionário
    que mapeia pares de cores do jogo para pares de cores do curses.
    """

    par = (__pega_cor(cor_de_fundo), __pega_cor(cor_de_frente))
    if par in __PARES_E_IDS:
        id_par = __PARES_E_IDS[par]
    else:
        id_par = len(__PARES_E_IDS) + 1
        __PARES_E_IDS[par] = id_par
        curses.init_pair(id_par, par[1], par[0])
    return id_par

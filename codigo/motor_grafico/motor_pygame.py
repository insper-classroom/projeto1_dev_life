'''
Neste arquivo são disponibilizadas as funções criadas pelos professores para o jogo. 
Essas funções utilizam o módulo pygame para desenhar strings na tela e ler as teclas apertadas pelo jogador.
Você não precisa entender como elas funcionam, mas pode dar uma olhada se quiser.
'''
import pygame

from . import constantes_do_motor as consts


__ASSETS = {}
def chama_funcao_jogo(jogo):
    pygame.init()
    pygame.display.set_caption('Jogo')

    largura_char, altura_char = __carrega_fonte()
    largura_tela = largura_char * consts.LARGURA_TELA_CHARS
    altura_tela = altura_char * consts.ALTURA_TELA_CHARS

    # Cria janela
    janela = pygame.display.set_mode((largura_tela, altura_tela))
    jogo(janela, consts.ALTURA_TELA_CHARS, consts.LARGURA_TELA_CHARS)


__TECLAS_APERTADAS = {}
__DELAY = 200  # Em milissegundos
def pega_tecla_apertada(janela):
    # Pega a tecla apertada
    while True:
        for evento in pygame.event.get():
            if evento == pygame.QUIT:
                return consts.ESCAPE
            elif evento.type == pygame.KEYDOWN:
                __TECLAS_APERTADAS[evento.key] = -1
            elif evento.type == pygame.KEYUP:
                __TECLAS_APERTADAS.pop(evento.key)
        if __TECLAS_APERTADAS:
            proxima_tecla = sorted(__TECLAS_APERTADAS.keys(), key=lambda t: __TECLAS_APERTADAS[t])[0]
            t0 = __TECLAS_APERTADAS[proxima_tecla]
            t1 = pygame.time.get_ticks()
            if t1 - t0 > __DELAY:
                __TECLAS_APERTADAS[proxima_tecla] = t1

                # Mapeia teclas do pygame para valores das constantes
                # do motor gráfico.
                mapeamento_teclas = {
                    pygame.K_UP: consts.SETA_CIMA,
                    pygame.K_DOWN: consts.SETA_BAIXO,
                    pygame.K_LEFT: consts.SETA_ESQUERDA,
                    pygame.K_RIGHT: consts.SETA_DIREITA,
                    pygame.K_RETURN: consts.ENTER,
                    pygame.K_SPACE: consts.ESPACO,
                    pygame.K_ESCAPE: consts.ESCAPE,
                    pygame.K_a: 'a',
                    pygame.K_b: 'b',
                    pygame.K_c: 'c',
                    pygame.K_d: 'd',
                    pygame.K_e: 'e',
                    pygame.K_f: 'f',
                    pygame.K_g: 'g',
                    pygame.K_h: 'h',
                    pygame.K_i: 'i',
                    pygame.K_j: 'j',
                    pygame.K_k: 'k',
                    pygame.K_l: 'l',
                    pygame.K_m: 'm',
                    pygame.K_n: 'n',
                    pygame.K_o: 'o',
                    pygame.K_p: 'p',
                    pygame.K_q: 'q',
                    pygame.K_r: 'r',
                    pygame.K_s: 's',
                    pygame.K_t: 't',
                    pygame.K_u: 'u',
                    pygame.K_v: 'v',
                    pygame.K_w: 'w',
                    pygame.K_x: 'x',
                    pygame.K_y: 'y',
                    pygame.K_z: 'z',
                }
                return mapeamento_teclas.get(proxima_tecla, proxima_tecla)


def preenche_fundo(janela, cor_rgb):
    """
    Limpa a janela e preenche o fundo com a cor especificada.
    Todas as posições serão preenchidas com a string ' '.

    A cor é uma lista com 3 elementos, cada um representando a intensidade de vermelho, verde e azul no
    intervalo de 0 a 255.
    """
    janela.fill(cor_rgb)


def desenha_string(janela, x, y, string, cor_fundo, cor_texto):
    """
    Desenha uma string na janela, na posição (x, y), com as cores
    especificadas.

    A posição (0, 0) é a esquerda superior da janela.
    cor_fundo e cor_texto são listas com 3 elementos, cada um
    representando a intensidade de vermelho, verde e azul no 
    intervalo de 0 a 255.
    """
    tamanho_char = __ASSETS['fonte'].size(' ')
    imagem_texto = __ASSETS['fonte'].render(string, True, cor_texto, cor_fundo)
    janela.blit(imagem_texto, (x * tamanho_char[0], y * tamanho_char[1]))


def mostra_janela(janela):
    pygame.display.flip()


# As funções abaixo são usadas internamente pelo motor gráfico
# e não precisam ser chamadas pelo seu código.

def __carrega_fonte():
    tamanho = 8
    
    encontrou_tamanho_certo = False
    while not encontrou_tamanho_certo:
        fonte = pygame.font.SysFont('monospace', tamanho)
        if fonte.size(' ')[0] > consts.LARGURA_CARACTERE:
            tamanho -= 1
            encontrou_tamanho_certo = True
        else:
            tamanho += 1
    __ASSETS['fonte'] = pygame.font.SysFont('monospace', tamanho)
    return __ASSETS['fonte'].size(' ')
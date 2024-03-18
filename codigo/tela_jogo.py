from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto


def desenha_tela(janela, estado, altura_tela, largura_tela):
    # Utilize o dicionário estado para saber onde o jogador e os outros objetos estão.
    # Por exemplo, para saber a posição do jogador, use estado['pos_jogador']
    # O mapa esta armazenado em estado['mapa'].
    motor.preenche_fundo(janela, PRETO)
    
    # desenha o mapa 
    for y, linha in enumerate(estado['mapa']):
        for x, caractere in enumerate(linha):
            motor.desenha_string(janela, x, y, caractere, PRETO, BRANCO)
    
    # desenha jogador
    posicao_jogador = estado['pos_jogador']
    motor.desenha_string(janela, posicao_jogador[0], posicao_jogador[1], '@', PRETO, BRANCO)
    
    # desenha demais objetos
    for objeto in estado['objetos']:
        posicao_objeto = objeto['posicao']
        caractere_objeto = objeto['tipo']
        cor_objeto = objeto['cor']
        motor.desenha_string(janela, posicao_objeto[0], posicao_objeto[1], caractere_objeto, cor_objeto, BRANCO)

    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado['mensagem'] = ''

    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    # APAGUE ESTA LINHA E ESCREVA SEU CÓDIGO AQUI

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
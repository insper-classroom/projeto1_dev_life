from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor

from motor_grafico import desenha_string  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
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

    # desenha a mensagem na tela
    mensagem = estado['mensagem']
    motor.desenha_string(janela, 10, altura_tela-1, mensagem, PRETO, BRANCO)

     # Desenha a quantidade de vidas
    quantidade_vidas = estado['vidas']
    max_vidas = estado['max_vidas']
    coracao_cheio = '❤'
    coracao_vazio = '🤍'
    vidas_desenhadas = coracao_cheio * quantidade_vidas + coracao_vazio * (max_vidas - quantidade_vidas)
    motor.desenha_string(janela, 0, altura_tela - 1, vidas_desenhadas, PRETO, BRANCO)

    motor.mostra_janela(janela)



def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado['mensagem'] = ''

    posicao_atual = estado['pos_jogador']
    
    # pega o mapa e a lista de objetos no estado atual
    mapa = estado['mapa']
    objetos = estado['objetos']
    estado['mensagem'] = 'Vidas disponíveis:' + str(estado['vidas'])
    
    # atualiza a posição do jogador
    if tecla == 'CIMA':
        nova_posicao = [posicao_atual[0], posicao_atual[1] - 1]
    elif tecla == 'BAIXO':
        nova_posicao = [posicao_atual[0], posicao_atual[1] + 1]
    elif tecla == 'ESQUERDA':
        nova_posicao = [posicao_atual[0] - 1, posicao_atual[1]]
    elif tecla == 'DIREITA':
        nova_posicao = [posicao_atual[0] + 1, posicao_atual[1]]
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
    else:
        # se a tecla que o usuário pressionar for invalida, faz nada
        return estado
    
    # verifica os limites do mapa 
    if nova_posicao[1] < 0 or nova_posicao[1] >= len(mapa) or \
            nova_posicao[0] < 0 or nova_posicao[0] >= len(mapa[0]):
        return estado
    
    # verifica se tem um coração na posição
    for objeto in objetos:
        if objeto['posicao'] == nova_posicao and objeto['tipo'] == CORACAO:
            # remove o coração da posição
            objetos.remove(objeto)
            # aumenta a vida do usuário, se já não estiver com a vida máxima
            if estado['vidas'] < estado['max_vidas']:
                estado['vidas'] += 1
                # mensagem que aparece quando pega um coração 
                estado['mensagem'] = 'Você pegou um coração e ganhou uma vida!'
            elif estado['vidas']==estado['max_vidas']:
                estado['mensagem'] = 'Você já tem o máximo de vidas!'
                return estado
                
            return estado
    
    # ve se tem um espinho na posição
    for objeto in objetos:
        if objeto['posicao'] == nova_posicao and objeto['tipo'] == ESPINHO:
            # diminui a vida do usuario em 1 
            estado['vidas'] -= 1
            # mensagem que aparece quado encosta em um espinho
            estado['mensagem'] = 'Você encostou em um espinho e perdeu uma vida!'
            # se a quantidade de vidas chegar a 0, da game over
            if estado['vidas'] == 0:
                estado['tela_atual'] = NULL
            return estado
    
    # se n tiver nenhum objeto na tela, o jogador vai pra esse lugar
    estado['pos_jogador'] = nova_posicao
    return estado
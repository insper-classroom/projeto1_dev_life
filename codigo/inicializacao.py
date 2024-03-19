from random import randint

from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código


def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    # Implemente esta função para o nível básico
    # A função deve retornar uma posição aleatória dentro da janela que não esteja na lista de posições ocupadas.
    # Uma posição é uma lista com exatas dois elementos: a posição x e a posição y.
    # Além disso, a posição gerada deve ser adicionada à lista de posições ocupadas.
    while True:
        x = randint(0, largura_mapa)
        y = randint(0, altura_mapa)
        posicao = [x, y]
        if posicao not in posicoes_ocupadas:
            posicoes_ocupadas.append(posicao)
            return posicao


def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):
    """
    Esta função já está pronta, você não precisa modificá-la.

    Gera uma lista de objetos do tipo especificado, com a quantidade especificada.
    Cada objeto é um dicionário com as chaves 'tipo', 'posicao' e 'cor'.

    Parâmetros:
    quantidade: quantidade de objetos a serem gerados
    tipo: tipo do objeto a ser gerado. É uma string como '❤'
    cor: cor do objeto a ser gerado. É uma lista com três elementos, como [255, 0, 0]
    largura_mapa: largura do mapa do jogo em caracteres
    altura_mapa: altura do mapa do jogo em caracteres
    posicoes_ocupadas: lista de posições ocupadas no mapa. Cada posição é uma lista com exatamente dois elementos: a posição x e a posição y.
    """
    objetos = []

    for i in range(quantidade):
        posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
        objetos.append({
            'tipo': tipo,
            'posicao': posicao,
            'cor': cor,
        })

    return objetos


def inicializa_estado():
    # Cria lista de listas, cada uma com 50 espaços em branco
    # Você pode mudar esta lista, inclusive seu tamanho, à vontade
    mapa = [
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
    ]
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    # bota o usuario no meio do mapa
    pos_jogador = [largura_mapa // 2, altura_mapa // 2]

    # cria os outros objetos pelo mapa
    posicoes_ocupadas = [pos_jogador]
    objetos = []
    
    # cria os coracoes
    objetos += gera_objetos(8, CORACAO, VERMELHO, largura_mapa-1, altura_mapa-1, posicoes_ocupadas)
    
    # cria os espinhos
    objetos += gera_objetos(6, ESPINHO, VERDE_CLARO, largura_mapa-1, altura_mapa-1, posicoes_ocupadas)
    
    # cria os monstros
    objetos += gera_objetos(12, MONSTRO, BRANCO, largura_mapa-1, altura_mapa-1, posicoes_ocupadas)

    #inicializa propriedades mosntro
    for objeto in objetos:
        if objeto['tipo'] == MONSTRO:
            objeto['vidas'] = 5
            objeto['probabilidade_de_ataque'] = 0.3

    
    # cria um loop pra adicionar as paredes nas extremidades do mapa
    for x in range(largura_mapa):
        for y in range(altura_mapa):
            if x == 0 or x == largura_mapa - 1 or y == 0 or y == altura_mapa - 1:
                objetos.append({
                    'tipo': PAREDE,
                    'posicao': [x, y],
                    'cor': [150, 75, 0],
                })

    
    # cria as paredes com as suas respectivas coordenadas
    paredes = [
        [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],  
        [10, 10], [11, 10], [12, 10], [13, 10], [14, 10],  
        
    ]
    
    for parede in paredes:
        objetos.append({
            'tipo': PAREDE,
            'posicao': parede,
            'cor': [150, 75, 0],
        })

    return {
        'tela_atual': TELA_JOGO,
        'pos_jogador': pos_jogador,
        'vidas': 5,
        'max_vidas': 5,
        'objetos': objetos,
        'mapa': mapa,
        'mensagem': '',
    }


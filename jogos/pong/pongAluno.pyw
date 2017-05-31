#!/usr/bin/python
# -*- coding: utf8 -*-

# Importanto o pygame.
import pygame
from pygame.locals import *

# Importando a função randint de dentro de random.
from random import randint

# Importando o arquivo dashLine que está na nossa pasta principal.
from dashLine import *

# Definir cores padrões
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Função principal do jogo.
def main():
    # Iniviar o pygame
    pygame.init()

    # Definir um tamanho de tela em umavariável
    tamanhoTela = (640, 480)

    # Definir a minha tela com o tamanho escolhido
    tela = pygame.display.set_mode(tamanhoTela)

    # O objeto Clock() serve para gerenciar o relógio do computador
    # para que possamos definir os Frames Por Segundo do nosso jogo.
    # Vamos guardá-lo em uma variavel para facilitar o acesso.
    clock = pygame.time.Clock()

    # Precisamos tratar o jogo dentro de um loop que é executaro até
    # que mandemos ele parar. Para isso utilizaremos uma variável que
    # trata o status do jogo se está rodando ou não. Definimos ela
    # inicialmente como True para que o jogo possa rodar on início.
    rodando = True

    # Para que o jogo rode ele precisa de um loop que estará sendo
    # executado enquanto a variável rodando estiver como True e
    # com isso podemos fazer todo o necessário para o jogo rodar.
    while rodando:
        # Para cada iteração no loop precisamos dizer ao nosso relogio
        # que chamamos anteriormente de clock há quantos FPS queremos
        # que o nosso jogo rode. Para isso utilizamos a função tick
        # que está dentro do objeto Clock()
        clock.tick(60)

        # Agora para que o jogo possa tratar as teclas apertadas pelo
        # usuário precisamos que o nosso jogo tenha um tratador de
        # eventos e para isso utilizamos os eventos de dentro do pygame.
        for evento in pygame.event.get():

            # Aqui um exemplo básico: se a função executada for clicar no botão
            # de fechar ( o X na tela ) definiremos o valor de rodando para False.
            if evento.type == pygame.QUIT:
                rodando = False

            print evento.type

        # Para cada vez que uma iteração for tratada o jogo precisa
        # apagar o que tinha anteriormente na janela. Para isso a
        # primeira coisa que tratamos em nosso jogo é o fundo e nesse
        # caso pintaremos tudo de preto com a função fill() da tela e
        # passaremos a cor PRETO que foi definida no começo do codigo.
        tela.fill(PRETO)

        # Aqui trataremos todas as modificações nos objetos do jogo.
        #  /* Insira código */

        # Agora pedimos para o pygame desenhar todos os objetos na tela.
        #  /* Insira código */

        # Apos processar todas as modificações e desenhar tudo na tela
        # agora mandamos o pygame mostrar a próxima tela.
        pygame.display.flip()

    # Assim que a variável rodando for False então o jogo sairá
    # e voltara para o escopo da função main(), e assim poderemos
    # executar o comando para sair do jogo.
    pygame.quit()

# Aqui será o início do nosso programa, tudo o que estiver
# aqui será executado primeiro, então, iremos iniciar o nosso
# jogo a partir daqui. Basta chamar a função que trata o jogo.
main()

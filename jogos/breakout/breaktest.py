import pygame
from pygame.locals import *

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

class Ball():
    def __init__(self, screensize):
        self.screensize = screensize
        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)

        self.rect = pygame.Rect(screensize

def main():
    pygame.init()
    tamanhoTela = (640, 480)
    tela = pygame.display.set_mode(tamanhoTela)
    clock = pygame.time.Clock()
    bola = Circulo(50, 60, 80)
    rodando = True

    while rodando:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                
        tela.fill(PRETO)
        
        bola.desenhar(tela)

        pygame.display.flip()

    pygame.quit()

main()

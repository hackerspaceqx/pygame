#importação das bibliotecas
import pygame, sys
from pygame.locals import *

from random import randint

altura = 510
largura = 510

class zona(pygame.sprite.Sprite):
    def __init__(self,posX,posY, tam):
        pygame.sprite.Sprite.__init__(self)
        self.tamanho = tam
        self.posX = posX
        self.posY = posY
        self.lista1 = []
        self.preencherLista()

    def preencherLista(self):
        x = 0
        y = 0
        distancia = 2
        aumento = self.tamanho
        posicaoX = self.posX
        posicaoY = self.posY
        while x < 16:
            while y < 16:
                self.lista1.append(pygame.Rect(posicaoX, posicaoY, self.tamanho, self.tamanho))
                posicaoX = aumento + distancia
                aumento = aumento + self.tamanho + distancia
                y = y + 1
            aumento = self.tamanho
            posicaoY = posicaoY + distancia + aumento
            posicaoX = self.posX
            x = x + 1
            y = 0

    def desenhar(self,superfice,cor):
        for quadrado in self.lista1:
           pygame.draw.rect(superfice, (cor), quadrado)

class snake(pygame.sprite.Sprite):
    def __init__(self, zona):
        pygame.sprite.Sprite.__init__(self)
        self.distancia = 2
        self.tamanho = zona.tamanho
        self.tamanhoCorpo = 3
        self.posX = (altura / 2) - (self.tamanho  - 1)
        self.posY = (largura / 2) - (self.tamanho - 1)
        self.vida = True
        self.direcao = "direita"
        self.corpo = []
        self.criarCorpo()
        self.time = 1
        self.zona = zona
        self.venceu = False

    def criarCorpo(self):
        self.corpo.append(pygame.Rect(self.posX - self.distancia, self.posY - self.distancia, self.tamanho, self.tamanho))
        for i in range(1,self.tamanhoCorpo):
            self.corpo.append(pygame.Rect((self.posX ) - ((i * self.tamanho) + (self.distancia*(i + 1))), self.posY - self.distancia, self.tamanho, self.tamanho))

    def __addCorpo(self):
        self.corpo.append(pygame.Rect((self.corpo[len(self.corpo) - 1].x) , (self.corpo[len(self.corpo) - 1].y), self.tamanho, self.tamanho))

    def mover(self, direcao):
        posIAx = self.corpo[0].x
        posIAy = self.corpo[0].y
        if(self.vida == True and self.venceu == False):
            if (direcao == "esquerda" and (self.direcao != "direita")):
                if(self.corpo[0].left > 0):
                    self.corpo[0].x -= self.distancia + self.tamanho
                else:
                    self.corpo[0].x = largura - self.tamanho
                i = 1
                while i < len(self.corpo):
                    posAx = self.corpo[i].x
                    posAy = self.corpo[i].y
                    self.corpo[i].x = posIAx
                    self.corpo[i].y = posIAy
                    posIAx = posAx
                    posIAy = posAy
                    i = i + 1
                self.direcao = direcao

            if (direcao == "direita" and (self.direcao != "esquerda")):
                if(self.corpo[0].right < largura):
                    self.corpo[0].x += self.distancia + self.tamanho
                else:
                    self.corpo[0].x = 0
                i = 1
                while i < len(self.corpo):
                    posAx = self.corpo[i].x
                    posAy = self.corpo[i].y
                    self.corpo[i].x = posIAx
                    self.corpo[i].y = posIAy
                    posIAx = posAx
                    posIAy = posAy
                    i = i + 1
                self.direcao = direcao

            if (direcao == "cima" and (self.direcao != "baixo")):
                if(self.corpo[0].top > 0):
                    self.corpo[0].y -= self.distancia + self.tamanho
                else:
                    self.corpo[0].y = altura - self.tamanho

                i = 1
                while i < len(self.corpo):
                    posAx = self.corpo[i].x
                    posAy = self.corpo[i].y
                    self.corpo[i].x = posIAx
                    self.corpo[i].y = posIAy
                    posIAx = posAx
                    posIAy = posAy
                    i = i + 1
                self.direcao = direcao

            if (direcao == "baixo" and (self.direcao != "cima")):
                if (self.corpo[0].bottom < altura):
                    self.corpo[0].y += self.distancia + self.tamanho
                else:
                    self.corpo[0].y = 0

                i = 1
                while i < len(self.corpo):
                    posAx = self.corpo[i].x
                    posAy = self.corpo[i].y
                    self.corpo[i].x = posIAx
                    self.corpo[i].y = posIAy
                    posIAx = posAx
                    posIAy = posAy
                    i = i + 1
                self.direcao = direcao

    def update(self, tempo):
        self.colidirCorpo()
        if (self.time == tempo):
            self.mover(self.direcao)
            self.time += 1

    def update2(self):
        self.colidirCorpo()
        self.mover(self.direcao)

    def comerFruta(self,fruta):
        for i in range(0,len(self.corpo)):
            if (fruta.rect.colliderect(self.corpo[i])):
                fruta.gerarFruta()
                self.tamanhoCorpo += 1
                self.__addCorpo()

    def colidirCorpo(self):
        for i in range(1,(len(self.corpo) - 1)):
            if(self.corpo[0].colliderect(self.corpo[i])):
                self.vida = False

    def desenhar(self,janela,corCabeca,corCorpo):
        pygame.draw.rect(janela, corCabeca, self.corpo[0])
        for i in range(1, len(self.corpo)):
            pygame.draw.rect(janela, corCorpo, self.corpo[i])

class fruta(pygame.sprite.Sprite):
    def __init__(self, zona):
        pygame.sprite.Sprite.__init__(self)
        self.distancia = 2
        self.tamanho = zona.tamanho
        self.posX = randint(0, altura) - (self.tamanho)
        self.posY = randint(0,largura) - (self.tamanho)
        self.zona = zona
        self.rect = self.zona.lista1[randint(0, (len(self.zona.lista1) - 1))]

    def gerarFruta(self):
        self.rect = self.zona.lista1[randint(0, (len(self.zona.lista1) - 1))]

    def desenhar(self,superfice,cor):
        pygame.draw.rect(superfice, (cor), self.rect)

def cenario():
    #inicializaçã do pygame
    pygame.init()
    #criar a janela
    janela = pygame.display.set_mode((altura,largura))
    #defini o titulo
    pygame.display.set_caption("Snake")
    cor1 = (0, 140, 60)
    cor2 = (255, 0, 0)
    cor3 = (255, 100, 9)
    black = (0, 0, 0)
    zona1 = zona(0, 0, 30)
    cobra = snake(zona1)
    fruta1 = fruta(zona1)

    #fonte
    fonteJogo = pygame.font.SysFont("Arial",50)
    TextoGameOver = fonteJogo.render("Game Over",0,(255,255,255))
    TextoWins = fonteJogo.render("Jogador Venceu",0,(255,255,255))


    jogo = True
    relogio = pygame.time.Clock()

    #loop infinito
    while True:
        relogio.tick(5)
        janela.fill(black)
        Tempo = pygame.time.get_ticks() / 1000
        #for para leitura dos eventos
        for evento in pygame.event.get():
            #evento para fechar janela
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if jogo == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        cobra.direcao = "esquerda"
#                        cobra.mover("esquerda")
                    if evento.key == K_RIGHT:
                        cobra.direcao = "direita"
#                        cobra.mover("direita")
                    if evento.key == K_UP:
                        cobra.direcao = "cima"
#                        cobra.mover("cima")
                    if evento.key == K_DOWN:
                        cobra.direcao = "baixo"
#                        cobra.mover("baixo")

#        cobra.update(int(Tempo))
        cobra.update2()

        janela.fill(black)
        zona1.desenhar(janela,cor1)

        fruta1.desenhar(janela,black)

        cobra.desenhar(janela,cor2,cor3)

        cobra.comerFruta(fruta1)

        if cobra.vida == False:
            jogo = False
        if jogo == False:
            janela.blit(TextoGameOver,(100,altura/2.5))
        if cobra.tamanhoCorpo == (len(zona1.lista1) - 1):
            janela.blit(TextoWins, (100, altura / 2.5))
            cobra.venceu = True

        pygame.display.update()

cenario()
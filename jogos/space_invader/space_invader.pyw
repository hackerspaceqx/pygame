#importação das bibliotecas
import pygame, sys
from pygame.locals import *
from random import randint

#Variaveis globais
largura = 900
altura = 480
listaInimigos = []

#class para as naves
class naveEspacial(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("_img/nave.jpg")
        self.ImagemExplosao = pygame.image.load("_img/Explosao.jpg")


        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = altura-30

        self.listaDisparo = []
        self.Vida = True
        self.velocidade = 20
        self.vitoria = False

        ##    somTiro = pygame.mixer.Sound("../sons/Intro.wav")
        ##    somTiro.play()
        ##    somExplosao = pygame.mixer.Sound("../sons/Intro.wav")
        ##    somExplosao.play()

    """ Novos metodos """
    def movimentoDireita(self):
        if self.vitoria == False:
            self.rect.right += self.velocidade
            self.__movimento()

    def movimentoEsquerda(self):
        if self.vitoria == False:
            self.rect.left -= self.velocidade
            self.__movimento()

    def __movimento(self):
        if self.vitoria == False:
            if self.Vida == True:
                if self.rect.left <= 0:
                    self.rect.left = 0
                elif self.rect.right > 870:
                    self.rect.right = 840

    def disparar(self,posX,posY):
        if self.vitoria == False:
            tiroNave = tiro(posX, posY, "_img/tiroA.jpg", True)
            self.listaDisparo.append(tiroNave)

    def destruicao(self):
        if self.vitoria == False:
#           self.somExplosao.play()
            self.Vida = False
            self.velocidade = 0
            self.ImagemNave = self.ImagemExplosao

    def desenhar(self,superfice):
        superfice.blit(self.ImagemNave,self.rect)

class tiro(pygame.sprite.Sprite):

    def __init__(self, posX, posY, rota, personagem):
        pygame.sprite.Sprite.__init__(self)

        self.imageTiro = pygame.image.load(rota)
        self.rect = self.imageTiro.get_rect()
        self.rect.top = posY
        self.rect.left = posX
        self.velocidadeTiro = 5

        self.tiroPersonagem = personagem

    def trajetoria(self):
        if self.tiroPersonagem == True:
            self.rect.top = self.rect.top - self.velocidadeTiro
        else:
            self.rect.top = self.rect.top + self.velocidadeTiro

    def desenhar(self, superfice):
        superfice.blit(self.imageTiro, self.rect)

class inimigo(pygame.sprite.Sprite):

    def __init__(self, posX, posY, distancia, imagemUm, imagemDois):
        pygame.sprite.Sprite.__init__(self)

        self.imagemA = pygame.image.load(imagemUm)
        self.imagemB = pygame.image.load(imagemDois)

        self.listaImagemInimigo = [self.imagemA, self.imagemB]
        self.posImagemInimigo = 0

        self.imagemInimigo = self.listaImagemInimigo[self.posImagemInimigo]
        self.rect = self.imagemInimigo.get_rect()

        self.rect.top = posY
        self.rect.left = posX

        self.velocidadeTiro = 1
        self.listaTiros = []
        self.rangeTiro = 5
        self.tempoTroca = 1

        self.velocidade = 1
        self.direita = True
        self.contator = 0
        self.descerMax = self.rect.top + 40

        self.limiteDireita = posX + distancia
        self.limiteEsquerda = posX - distancia

        self.conquista = False

    def desenhar(self, superfice):
        self.imagemInimigo = self.listaImagemInimigo[self.posImagemInimigo]
        superfice.blit(self.imagemInimigo, self.rect)

    def comportamentoInimigo(self, tempoT):
        if self.conquista == False:
            self.__movimentosInimigo()
            self.__ataque()

            if (self.tempoTroca) == tempoT:
                self.posImagemInimigo = self.posImagemInimigo + 1
                self.tempoTroca += 1

                if self.posImagemInimigo > len(self.listaImagemInimigo)-1:
                    self.posImagemInimigo = 0

    def __movimentosInimigo(self):
        if self.contator < 3:
            self.__movimentoLateral()
        else:
            self.__decendo()

    def __movimentoLateral(self):
        if self.direita == True:
            self.rect.left = self.rect.left + self.velocidade
            if self.rect.left > self.limiteDireita:
                self.direita = False
                self.contator += 1
        else:
            self.rect.left = self.rect.left - self.velocidade
            if self.rect.left < self.limiteEsquerda:
                self.direita = True

    def __decendo(self):
        if self.descerMax == self.rect.top:
            self.contator = 0
            self.descerMax = self.rect.top + 40
        else:
            self.rect.top += 1


    def __ataque(self):
        if(randint(0,1000)) < self.rangeTiro:
            self.disparar()

    def disparar(self):
        x,y = self.rect.center
        tiroInimigo = tiro(x, y, "_img/tiroB.jpg", False)
        self.listaTiros.append(tiroInimigo)

def carregarInimigos():
    #invasor = inimigo(100, 100, 100,"../_img/MarcianoA.jpg","../_img/MarcianoB.jpg")
    posx = 100
    for x in range(1, 5):
        invasor = inimigo(posx, 100, 40, "_img/MarcianoA.jpg", "_img/MarcianoB.jpg")
        listaInimigos.append(invasor)
        posx = posx + 200

    posx = 100
    for x in range(1, 5):
        invasor = inimigo(posx, 0, 40, "_img/Marciano2A.jpg", "_img/Marciano2B.jpg")
        listaInimigos.append(invasor)
        posx = posx + 200

    posx = 100
    for x in range(1, 5):
        invasor = inimigo(posx, - 100, 40, "_img/Marciano3A.jpg", "_img/Marciano3B.jpg")
        listaInimigos.append(invasor)
        posx = posx + 200

def deterTodos():
    for inimigo in listaInimigos:
        for tiro in inimigo.listaTiros:
            inimigo.listaTiros.remove(tiro)
        inimigo.conquista = True

def SpaceInvader():
    #inicializaçã do pygame
    pygame.init()
    #criar a janela
    janela = pygame.display.set_mode((largura,altura))
    #defini o titulo
    pygame.display.set_caption("Space Invader")
    #Plano de fundp
    ImagemFundo = pygame.image.load("_img/Fundo.jpg")


    #musica
##    pygame.mixer.music.load('../sons/Intro.wav')
##    pygame.mixer.music.play(3)


    #fonte
    fonteJogo = pygame.font.SysFont("Arial",30)
    TextoGameOver = fonteJogo.render("Game Over",0,(255,0,0))
    TextoWins = fonteJogo.render("Jogodor Venceu",0,(255,0,0))

    #jogador
    jogador = naveEspacial()

    carregarInimigos()

    #cenario
    jogo = True
    relogio = pygame.time.Clock()


    #loop infinito
    while True:
        #movimentacao
        #jogador.movimento()
        #relogio
        relogio.tick(60)
        TempoT = pygame.time.get_ticks()/1000
        #for para leitura dos eventos
        for evento in pygame.event.get():
            #evento para fechar janela
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if jogo == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jogador.movimentoEsquerda()
                    elif evento.key == pygame.K_RIGHT:
                        jogador.movimentoDireita()
                    elif evento.key == pygame.K_s:
                        x,y = jogador.rect.center
                        jogador.disparar(x,y)

        #atulizaca das imagens na tela
        janela.blit(ImagemFundo,(0,0))


        #inicializacao dos objetos
        jogador.desenhar(janela)

        #controle dos tiros
        if len(jogador.listaDisparo) > 0:
            for umTiroNave in jogador.listaDisparo:
                umTiroNave.desenhar(janela)
                umTiroNave.trajetoria()
                if umTiroNave.rect.top < 100:
                    jogador.listaDisparo.remove(umTiroNave)
                else:
                    if len(listaInimigos) == 0:
                        jogador.vitoria = True
                    else:
                        for inimigo in listaInimigos:
                            if umTiroNave.rect.colliderect(inimigo):
                                listaInimigos.remove(inimigo)
                                jogador.listaDisparo.remove(umTiroNave)

        if len(listaInimigos) > 0:
            for invasor in listaInimigos:
                invasor.comportamentoInimigo(int(TempoT))
                invasor.desenhar(janela)

                if invasor.rect.colliderect(jogador.rect):
                    jogador.destruicao()
                    jogo = False
                    deterTodos()

                if len(invasor.listaTiros) > 0:
                    for umTiroInimigo in invasor.listaTiros:
                        umTiroInimigo.desenhar(janela)
                        umTiroInimigo.trajetoria()
                        if umTiroInimigo.rect.colliderect(jogador.rect):
                            jogador.destruicao()
                            jogo = False
                            deterTodos()
                        if umTiroInimigo.rect.top > 900:
                            invasor.listaTiros.remove(umTiroInimigo)
                        else:
                            for tiro in jogador.listaDisparo:
                                if tiro.rect.colliderect(umTiroInimigo.rect):
                                    jogador.listaDisparo.remove(tiro)
                                    invasor.listaTiros.remove(umTiroInimigo)

        #game over
        if jogo == False:
            #pygame.mixer.music.fadeout(3000)
            janela.blit(TextoGameOver,(380,altura/2.3))
        if jogador.vitoria == True:
            janela.blit(TextoWins, (380, altura / 2.3))
#            musicaVitoria = pygame.mixer.music("url")
#            musicaVitoria.play()

        #atualizada da tela
        pygame.display.update()

#MAIN
SpaceInvader()
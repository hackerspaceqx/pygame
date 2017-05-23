#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from dashLine import *
from random import randint
from pygame.locals import *

# Definindo as cores que serão utilizadas em nosso jogo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criamos uma classe para tratar das funções da bola do
# jogo pong.
class Pong():
	def __init__(self, screensize):
		# OBS: Não podemos guardar a tela como parâmetro pois isso
		# geraria conflito com os outros objetos e a referência
		# para esta janela não seria guardada.
		
		# Armazenamos o tamanho da janela dentro do proprio objeto
		# para que não seja preciso passá-la como parâmetro de uma
		# função depois.
		self.screensize = screensize
		
		# Gerando as posições centrais do pong.
		self.centerx = int(screensize[0]*0.5)
		self.centery = int(screensize[1]*0.5)
		
		# Tamanho do raio.
		self.radius = 5

		# Gerando um retângulo externo e invisivel.
		self.rect = pygame.Rect(self.centerx - self.radius,
								self.centery - self.radius,
								self.radius*2, self.radius*2)

		# Definindo a cor.
		self.color = WHITE

		# Lista com direção x e y.
		self.direction = [0,0]

		# Velocidade com qual o pong se move em cada eixo.
		self.speed = [2,4]
		
		# Verifica se o pong batou na esquerda.
		self.hitEdgeLeft = False
		# Verifica se o pong batou na direita.
		self.hitEdgeRight = False

	def render(self, screen):
		# Esta função receberá a tela criada no código principal,
		# a cor definida na criação do objeto, e o retângulo que
		# criamos anteriormente, o zero no final indica que não
		# haverá uma borda nesse objeto.
		pygame.draw.rect(screen, self.color, self.rect, 0)

	def update(self, jogador, computador):
		# Atualiza a posição X e Y andando na direção escolhida
		# com a velocidade atual.
		self.centerx += self.direction[0] * self.speed[0]
		self.centery += self.direction[1] * self.speed[1]

		# Atualiza o novo centro do retângulo de acordo com o
		# calculo feito anteriormente.
		self.rect.center = (self.centerx, self.centery)

		if self.rect.top <= 0:
			self.rect.top = 0
			self.direction[1] *= -1
		if self.rect.bottom >= self.screensize[1] - 1:
			self.rect.bottom = self.screensize[1] - 1
			self.direction[1] *= -1
		if self.rect.left <= 0:
			self.direction[0] *= - 1
			self.hitEdgeLeft = True
		if self.rect.right >= self.screensize[0] - 1:
			self.direction[0] *= - 1
			self.hitEdgeRight = True

		if self.rect.colliderect(jogador.rect) or self.rect.colliderect(computador.rect):
			self.direction[0] *= -1
			self.speed[0] = randint(2,8)

class Paddle():
	def __init__(self, screensize):
		self.screensize = screensize
		self.centerx = screensize[0] - 16
		self.centery = int(screensize[1]*0.5)

		self.color = WHITE
		self.radiusxy = [5, 30]

		self.direction = 0
		self.speed = 6

		self.rect = pygame.Rect(self.centerx - self.radiusxy[0],
								self.centery - self.radiusxy[1],
								self.radiusxy[0]*2, self.radiusxy[1]*2)

	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect, 0)
	def update(self):
		self.centery += self.direction * self.speed
		if self.centery - self.radiusxy[1] <= 0:
			self.centery = self.radiusxy[1]
		elif self.centery + self.radiusxy[1] >= self.screensize[1] - 1:
			self.centery = self.screensize[1] - 1 - self.radiusxy[1]
		self.rect.center = (self.centerx, self.centery)

		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= self.screensize[1] - 1:
			self.rect.bottom = self.screensize[1] - 1

class AIPaddle():
	def __init__(self, screensize):
		self.screensize = screensize
		self.centerx = 16
		self.centery = int(screensize[1]*0.5)

		self.color = WHITE
		self.radiusxy = [5, 30]
		self.speed = 6

		self.rect = pygame.Rect(self.centerx - self.radiusxy[0],
								self.centery - self.radiusxy[1],
								self.radiusxy[0]*2, self.radiusxy[1]*2)

	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect, 0)
	def update(self, pong):
		if self.rect.top > pong.rect.top:
			self.centery -= self.speed
		elif self.rect.bottom < pong.rect.bottom:
			self.centery += self.speed

		self.rect.center = (self.centerx, self.centery)



# Definimos uma função principal que será responsável pela
# execução do jogo
def main():
	# Iniciamos uma instancia do pygame utilizando o método
	# init() dentro do pacote pygame.
	pygame.init()

	# Definimos o título da janela
	pygame.display.set_caption("Pong")

	# Indicamos o tamanho da janela utilizando uma tupla
	# com os tamanhos (largura, altura)
	screensize = (640,480)

	# Iniciamos uma nova janela utilizando o tamanho
	# definido anteriormente
	screen = pygame.display.set_mode(screensize)

	# Para que o jogo rode é necessário ter controle sobre
	# o tempo que se passa no processador, chamados de tick,
	# e para isso utilizamos um objeto próprio do pygame
	# chamado de Clock()
	clock = pygame.time.Clock()

	# Aqui criamos uma instancia de cada objeto necessário
	# para o jogo

	# Barra do jogador
	jogador = Paddle(screensize)

	# Barra do computador
	computador = AIPaddle(screensize)

	# Bola do pong
	pong = Pong(screensize)
	# Definimos uma direção inicial
	pong.direction = [-1,-1]

	# Esta variável serve para que possamos tratar mais
	# facilmente como o jogo é executado
	running = True

	score = 0

	while running:
		# Temos que dizer ao jogo quantos Frames Por Segundo desejamos.
		# Para isso utilizamos a função tick do objeto Clock() que foi
		# instanciado anteriormente.
		clock.tick(60)

		# Precisamos também tratar todos os eventos que ocorrem em nosso
		# jogo, como: fechamento da janelaf, botão apertado, etc.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_UP:
					jogador.direction = -1
				elif event.key == K_DOWN:
					jogador.direction = 1
			if event.type == KEYUP:
				if event.key == K_UP and jogador.direction == -1:
					jogador.direction = 0
				elif event.key == K_DOWN and jogador.direction == 1:
					jogador.direction = 0

		# Após cada iteração do jogo, devemos limpar a tela anterior,
		# se não, o jogo ficaria sendo desenhado por cima do anterior,
		# e não queremos isso.f
		screen.fill(BLACK)

		pong.update(jogador, computador)
		jogador.update()
		computador.update(pong)

		# Função fora do escopo da criação do jogo, ela serve
		# para gerar uma linha "cortada". Usada como:
		# draw_dashed_line(surf, color, start_pos, end_pos, width, dash_length)
		draw_dashed_line(screen, WHITE, (int(screensize[0]*0.5), 10), (int(screensize[0]*0.5), screensize[1]-1), 5, screensize[1]/20)


		# Mandamos um sinal para cada objeto do nosso jogo que possui a
		# função render() que servirá para que eles sejam desenhados na
		# tela e passamos a nossa tela como um parâmetro.
		pong.render(screen)
		jogador.render(screen)
		computador.render(screen)

		# Mandamos o Pygame mostrar tudo o que foi desenhado nesta iteração
		# do jogo.
		pygame.display.flip()

	# Quando o jogo para de ser executado, ou seja, a variável
	# running passar a ter o valor falso, o loop principal do
	# jogo será terminado e assim chamamos o método de fechamento
	# do pygame.
	pygame.quit()

# No início do programa chamamos a função main() para
# que o jogo seja executado.
main()
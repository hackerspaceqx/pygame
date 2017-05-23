#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from dashLine import *
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Pong():
	def __init__(self, screensize):
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

	def update(self):
		# Atualiza a posição X e Y andando na direção escolhida
		# com a velocidade atual.
		self.centerx += self.direction[0] * self.speed[0]
		self.centery += self.direction[1] * self.speed[1]

		# Atualiza o novo centro do retângulo de acordo com o
		# calculo feito anteriormente.
		self.rect.center = (self.centerx, self.centery)

def main():
	pygame.init()
	pygame.display.set_caption("Pong")
	screensize = (640,480)
	screen = pygame.display.set_mode(screensize)
	clock = pygame.time.Clock()

	pong = Pong(screensize)

	running = True

	score = 0

	while running:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill(BLACK)

		# Função fora do escopo da criação do jogo, ela serve
		# para gerar uma linha "cortada". Usada como:
		# draw_dashed_line(surf, color, start_pos, end_pos, width, dash_length)
		draw_dashed_line(screen, WHITE, (int(screensize[0]*0.5), 10), (int(screensize[0]*0.5), screensize[1]-1), 5, screensize[1]/20)

		pong.render(screen)

		pygame.display.flip()

	pygame.quit()


main()
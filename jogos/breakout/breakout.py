import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (100, 200, 100)

class Ball():
    def __init__(self, screensize):
        self.screensize = screensize
        self.centerx = int(screensize[0] * 0.5)
        self.centery = int(screensize[1] * 0.5)

        self.radius = 5

        self.rect = pygame.Rect(self.centerx - self.radius,
                                self.centery - self.radius,
                                self.radius*2, self.radius*2)
        self.direction = [0,0]
        self.speed = [4,4]
    def render(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, self.radius)

class Paddle():
    def __init__(self, screensize):
        self.screensize = screensize
        self.centerx = int(screensize[0] * 0.5)
        self.centery = screensize[1] - 50

        self.rect = pygame.Rect(self.centerx - 25, self.centery - 10, 50, 20)
        self.direction = 0
        self.speed = 10
    def render(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Cell():
    def __init__(self, screensize, x, y, size):
        self.screensize = screensize
        self.x = x
        self.y = y
        self.size = size

        self.rect = pygame.Rect(x, y, size-1, int(size*0.5)-1)
        self.outline = pygame.Rect(x, y, size, int(size*0.5))
    def render(self, screen):
        pygame.draw.rect(screen, BLACK, self.outline, 0)
        pygame.draw.rect(screen, GREEN, self.rect, 0)

def initGrid(screensize, size):
    grid = []
    for j in range(40, size*5+1, int(size*0.5)):
        grid.append(Cell(screensize, 0, j, size))
        for i in range(19, screensize[0], size):
            grid.append(Cell(screensize, i, j, size))
    return grid

def main():
    pygame.init()
    screensize = (640, 480)
    screen = pygame.display.set_mode(screensize)
    clock = pygame.time.Clock()

    # Game Objects
    ball = Ball(screensize)
    paddle = Paddle(screensize)
    #cell = Cell(screensize, 100, 100, 50)
    grid = initGrid(screensize, 20)

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        
        # Updating

        # Drawing
        ball.render(screen)
        paddle.render(screen)
        for cell in grid:
            cell.render(screen)

        pygame.display.flip()

    pygame.quit()

main()

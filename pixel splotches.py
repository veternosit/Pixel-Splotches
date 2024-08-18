import pygame
import sys
import random

pygame.init()

WIDTH = 1000
HEIGHT = 1000
FPS = 0.5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Splotches")
clock = pygame.time.Clock()

colOld = [[[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
           for i in range(int(WIDTH / 10))] for j in range(int(HEIGHT / 10))]

colNew = [[[0, 0, 0] for i in range(int(WIDTH / 10))] for j in range(int(HEIGHT / 10))]

while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for x in range(int(WIDTH / 10)):
        for y in range(int(HEIGHT / 10)):
            s = []
            if x > 0:
                s.append(colOld[y][x - 1])
            if x < int(WIDTH / 10) - 1:
                s.append(colOld[y][x + 1])
            if y > 0:
                s.append(colOld[y - 1][x])
            if y < int(HEIGHT / 10) - 1:
                s.append(colOld[y + 1][x])
            colNew[y][x] = random.choice(s)
            pygame.draw.rect(screen, colNew[y][x], pygame.Rect(10*x, 10*y, 10*x + 10, 10*y + 10))

    colOld = colNew

    pygame.display.update()

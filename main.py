import pygame
from settings import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(screen)

cycle = True
while cycle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cycle = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    player.update(keys)
    player.draw()

    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
    pygame.display.flip()
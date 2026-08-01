import pygame
from settings import *

class Player:
    def __init__(self, sc):
        self.sc = sc
        self.speed = PLAYER_SPEED
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = PLAYER_X
        self.y = PLAYER_Y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        self.rect.topleft = (self.x, self.y)

    def draw(self):
        player = pygame.image.load("walk_down.png")
        player = pygame.transform.scale(player, (self.width, self.height))
        self.sc.blit(player, (self.rect.x, self.rect.y))
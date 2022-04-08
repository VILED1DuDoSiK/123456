import pygame
from space_ship import Space_ship
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, space_shep):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 20)
        self.color = 116, 225, 3
        self.speed = 0.8
        self.rect.centerx = Space_ship(screen).rect.centerx
        self.rect.top = Space_ship(screen).rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
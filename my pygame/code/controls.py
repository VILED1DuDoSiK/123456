import pygame, sys
import bullet
from space_ship import Space_ship
from bullet import Bullet

def events(screen, space_ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                space_ship.mright = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                space_ship.mleft = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, space_ship)
                bullets.add(new_bullet)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                space_ship.mright = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                space_ship.mleft = False

def update(bg_color, screen, space_ship, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    space_ship.output()
    pygame.display.flip()
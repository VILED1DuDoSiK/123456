import pygame, controls
from space_ship import Space_ship
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption(" Alien invasion ")
    bg_color = (0, 0, 0)
    space_ship = Space_ship(screen)
    bullets = Group()

    while True:
        controls.events(screen, space_ship, bullets)
        space_ship.update_Space_ship()
        bullets.update()
        controls.update(bg_color, screen, space_ship, bullets)

run()
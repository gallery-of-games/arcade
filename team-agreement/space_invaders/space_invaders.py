import pygame
import os
import random
import time
pygame.init()
pygame.display.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Space Shooter")

# Load images
RED_SPACE_SHIP = pygame.image.load("assets/pixel_ship_red_small.png")
BLUE_SPACE_SHIP = pygame.image.load("assets/pixel_ship_blue_small.png")
GREEN_SPACE_SHIP = pygame.image.load("assets/pixel_ship_green_small.png")

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load("assets/pixel_ship_yellow.png")

# Lasers
RED_LASER = pygame.image.load("assets/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("assets/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("assets/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("assets/pixel_laser_yellow.png")

# Background image
BG = pygame.image.load("assets/background-black.png")


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.flip()


if __name__ == '__main__':
    main()

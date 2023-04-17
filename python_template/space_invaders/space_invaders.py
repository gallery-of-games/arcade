import pygame
import os
import random
import time
pygame.font.init()
pygame.init()
pygame.display.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Space Shooter")

# Load images
RED_SHIP = pygame.image.load("assets/pixel_ship_red_small.png")
BLUE_SHIP = pygame.image.load("assets/pixel_ship_blue_small.png")
GREEN_SHIP = pygame.image.load("assets/pixel_ship_green_small.png")

# Player ship
YELLOW_SHIP = pygame.image.load("assets/pixel_ship_yellow.png")

# Lasers
RED_LASER = pygame.image.load("assets/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("assets/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("assets/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("assets/pixel_laser_yellow.png")

# Background image
BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        self.y += velocity

    def off_screen(self, height):
        return self.y <= HEIGHT and self.y >= 0

    def collision(self, obj):
        return collide(obj, self)

def collide(obj1, obj2):
    pass

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SHIP, RED_LASER),
        "green": (GREEN_SHIP, GREEN_LASER),
        "blue": (BLUE_SHIP, BLUE_LASER)
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, velocity):
        self.y += velocity

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont('arial', 50)
    lost_font = pygame.font.SysFont('arial', 70)

    enemies = []
    wave_length = 5
    enemy_velocity = 1

    player_velocity = 5

    player = Player(300, 650)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0


    def redraw_window():
        WIN.blit(BG, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (0, 0, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("Game Over", 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 5:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity > 0:
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player.get_width() + player_velocity < WIDTH:
            player.x += player_velocity
        if keys[pygame.K_UP] and player.y - player_velocity > 0:
            player.y -= player_velocity
        if keys[pygame.K_DOWN] and player.y + player.get_height() + player_velocity < HEIGHT:
            player.y += player_velocity

        for enemy in enemies[:]:
            enemy.move(enemy_velocity)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

    pygame.display.flip()


if __name__ == '__main__':
    main()

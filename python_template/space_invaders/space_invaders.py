import pygame
import os
import sys
import random
import time

# Initialize pygame
pygame.font.init()
pygame.init()
pygame.display.init()

# Set up window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


# # TODO: ASSETS FOR PYTEST - TOP
# # Load images
# # Enemy ships
# RED_SHIP = pygame.image.load("python_template/space_invaders/assets/pixel_laser_red.png")
# BLUE_SHIP = pygame.image.load("python_template/space_invaders/assets/pixel_ship_blue_small.png")
# GREEN_SHIP = pygame.image.load("python_template/space_invaders/assets/pixel_ship_green_small.png")
# # Player ship
# YELLOW_SHIP = pygame.image.load("python_template/space_invaders/assets/pixel_ship_yellow.png")
# # Lasers
# # Enemy lasers
# RED_LASER = pygame.image.load("python_template/space_invaders/assets/pixel_laser_red.png")
# GREEN_LASER = pygame.image.load("python_template/space_invaders/assets/pixel_laser_green.png")
# BLUE_LASER = pygame.image.load("python_template/space_invaders/assets/pixel_laser_blue.png")
# # Player laser
# YELLOW_LASER = pygame.image.load("python_template/space_invaders/assets/pixel_laser_yellow.png")
# # Background image
# BG = pygame.transform.scale(pygame.image.load("python_template/space_invaders/assets/background-black.png"), (WIDTH, HEIGHT))
# # TODO: ASSETS FOR PYTEST - BOTTOM



# TODO: ASSETS FOR GAMEPLAY - TOP
# Load images
# Enemy ships
RED_SHIP = pygame.image.load("assets/pixel_ship_red_small.png")
BLUE_SHIP = pygame.image.load("assets/pixel_ship_blue_small.png")
GREEN_SHIP = pygame.image.load("assets/pixel_ship_green_small.png")
# Player ship
YELLOW_SHIP = pygame.image.load("assets/pixel_ship_yellow.png")
# Lasers
# Enemy lasers
RED_LASER = pygame.image.load("assets/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("assets/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("assets/pixel_laser_blue.png")
# Player laser
YELLOW_LASER = pygame.image.load("assets/pixel_laser_yellow.png")
# Background image
BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (WIDTH, HEIGHT))
# TODO: ASSETS FOR GAMEPLAY - BOTTOM


# Dictionary to store scores
high_score = {

}


class Laser:
    """
    Class for lasers shot by a ship

    Attributes:
        x (int): x coordinate of the laser
        y (int): y coordinate of the laser
        img (pygame.Surface): Image of the laser
        mask (pygame.mask.Mask): Mask of the laser

    Methods:
        draw: Draw the laser onto the window
        move: Mode the laser by a given velocity
        off_screen: Check if the laser is off the screen
        collision: Check if the laser has collided with another object
    """
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        """
        Draw the laser onto the window
        """
        window.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        """
        Move the laser by a given velocity
        """
        self.y += velocity

    def off_screen(self, height):
        """
        Check if the laser is off screen
        """
        return not(height >= self.y >= 0)

    def collision(self, obj):
        """
        Check if the laser has collided with another object
        """
        return collide(obj, self)


class Ship:
    """
    Class to represent a ship

    Attributes:
        COOLDOWN (int): The number of frames between each laser shot
        x (int): x coordinate of the ship
        y (int): y coordinate of the ship
        health (int): Health of the ship
        ship_img (pygame.Surface): Image of the ship
        laser_img (pygame.Surface): Image of the laser shot by the ship
        lasers (list): List of laser objects shot by the ship
        cool_down_counter (int): Number of frames since the last laser shot

    Methods:
        get_width: Get the width of the ship
        get_height: Get the height of the ship
        draw: Draw the ship and its lasers onto the window
        move_lasers: Move the lasers shot by the ship a given velocity, and remove lasers that are off screen or have collided with another object
        cooldown: Handle the cooldown between laser shots
        shoot: Shoot a laser from the ship, if the cooldown has expired
    """
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def get_width(self):
        """
        get_width: Get the width of the ship
        """
        return self.ship_img.get_width()

    def get_height(self):
        """
        get_height: Get the height of the ship

        """
        return self.ship_img.get_height()

    def draw(self, window):
        """
        draw: Draw the ship and its lasers onto the window
        """
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, velocity, obj):
        """
        move_lasers: Move the lasers shot by the ship a given velocity, and remove lasers that are off screen or have collided with another object
        """
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        """
        cooldown: Handle the cooldown between laser shots
        """
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        """
        shoot: Shoot a laser from the ship, if the cooldown has expired
        """
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Player(Ship):
    """
    Class represents the player's ship

    Attributes:
        ship_img (pygame.Surface): Image of the player's ship
        laser_img (pygame.Surface): Image of the laser
        mask (pygame.mask.Mask): mask for the player's ship
        max_health (int): maximum health of the player's ship

    Methods:
        __init__(self, x, y, health=100): Initialize a player object with x and y coordinates and an optional health parameter
        move_lasers(self, velocity, objs): Moves the lasers on the screen and removes any lasers that go off the screen or collide with an object
        draw(self, window): Draws the player's ship on the screen
        health_bar(self, window): Draws the health bar for the player's ship on the screen
    """

    # TODO: THIS __init__ IS FOR THE GAME
    # def __init__(self, x, y, health=100):

    # TODO: THIS __init__ IS FOR PRESENTATION
    def __init__(self, x, y, health=50):

    # TODO: THIS __init__ IS FOR TESTING
    # def __init__(self, x, y, health=10):
        """
        __init__(self, x, y, health=100): Initialize a player object with x and y coordinates and an optional health parameter
        """
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, velocity, objs):
        """
        move_lasers(self, velocity, objs): Moves the lasers on the screen and removes any lasers that go off the screen or collide with an object

        """
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        """
        draw(self, window): Draws the player's ship on the screen
        """
        super().draw(window)
        self.health_bar(window)

    def health_bar(self, window):
        """
        health_bar(self, window): Draws the health bar for the player's ship on the screen
        """
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship):
    """
    Class represents an enemy ship

    Attributes:
        ship_img (pygame.Surface): Image of the enemy ship
        laser_img (pygame.Surface): Image of the laser
        mask (pygame.mask.Mask): Mask for the enemy ship

    Methods:
        __init__(self, x, y, color, health=100): Initializes an enemy object with x and y coordinates, a color, and an optional health parameter
        move(self, velocity): Moves the enemy ship down the screen
        shoot(self): Creates a laser object and adds it tp the list of lasers
    """
    COLOR_MAP = {
        "red": (RED_SHIP, RED_LASER),
        "green": (GREEN_SHIP, GREEN_LASER),
        "blue": (BLUE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        """
        __init__(self, x, y, color, health=100): Initializes an enemy object with x and y coordinates, a color, and an optional health parameter
        """
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, velocity):
        """
        move(self, velocity): Moves the enemy ship down the screen
        """
        self.y += velocity

    def shoot(self):
        """
        shoot(self): Creates a laser object and adds it tp the list of lasers
        """
        if self.cool_down_counter == 0:
            laser = Laser(self.x-15, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(object1, object2):
    """
    Determines if two objects collide using their masks

    Parameters:
        object1 (ship): First object to check for collision
        object2 (ship): Second object to check for collision

    Returns:
        bool: True if the objects collide, False otherwise
    """
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) is not None


def main():
    """
    Main function that runs the game

    Variables:
        run (bool): Flag for if the game is running
        FPS (int): Frames per second of the game
        level (int): Current level of the game
        user_input (str): String for user input
        lives (int): Number of lives the player has
        main_font (pygame.font.Font): Font used for text on the screen
        lost_font (pygame.font.Font): Font used for the "Game Over" text
        enemies (list): List of enemy objects
        wave_length (int): Number of enemies in a wave
        enemy_velocity (int): Speed of the enemy ships
        player_velocity (int): Speed of player's ship
        laser_velocity (int): Speed of lasers
        player (Player): player object
        clock (pygame.time.Clock): used for timing
        lost (bool): Flag for if the player has lost
        lost_count (int): Number of frames that have passed since the player lost

    Functions:
        redraw_window(): Redraws the game window
        get_player_name(): Gets the player's name after they lose

    """
    run = True
    FPS = 60
    level = 0
    user_input = ''
    lives = 5
    main_font = pygame.font.Font(None, 50)
    lost_font = pygame.font.Font(None, 70)

    enemies = []
    wave_length = 5
    enemy_velocity = 1

    player_velocity = 5
    laser_velocity = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        """
        redraw_window(): Redraws the game window
        """
        WIN.blit(BG, (0, 0))
        lives_label = main_font.render(f"Invasions Remaining: {lives}", 1, (255, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (0, 0, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("Game Over", 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
            get_player_name()

        pygame.display.update()

    def get_player_name():
        """
        get_player_name(): Gets the player's name after they lose
        """
        text_color = (255, 255, 255)
        get_info_font = pygame.font.Font(None, 50)
        input_rect = pygame.Rect(250, 300, 250, 32)
        active = False
        text = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                        if event.key == pygame.K_RETURN:
                            high_score[str(text).strip()] = level
                            text = ""
                            active = False
                            main_menu()

            pygame.display.update()
            pygame.draw.rect(WIN, (255, 0, 255), input_rect)
            input_text = get_info_font.render(text, True, text_color)
            WIN.blit(input_text, (input_rect.x, input_rect.y))
            pygame.display.flip()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

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
        if keys[pygame.K_DOWN] and player.y + player.get_height() + player_velocity + 15 < HEIGHT:
            player.y += player_velocity
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_velocity)
            enemy.move_lasers(laser_velocity, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_velocity, enemies)

    pygame.display.flip()


def main_menu():
    """
    Displays the main menu of the game, including the game title and high scores table.
    Listens for mouse click to call main() function and begin gameplay.

    Variables:
        title_font (pygame.font.Font): Font used for text on main menu
        run (bool): Flag for if game is running
    """
    title_font = pygame.font.Font(None, 60)
    run = True
    sorted_high_scores = sorted(high_score.items(), key=lambda x: x[1], reverse=True)[:5]

    for key, value in sorted_high_scores:
        with open('assets/player_name_score.txt', 'a+') as file:
            file.write(f'{key}: {value} \n')

    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render(f"Press mouse button to begin", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 50))
        high_score_title = title_font.render(f'High Scores:', False, (255, 255, 255))
        WIN.blit(high_score_title, (WIDTH / 2 - high_score_title.get_width() / 2, 150))

        with open('assets/player_name_score.txt', 'r') as file:
            contents = file.readlines()

            player_data = {

            }
            for line in contents:
                name, score = line.strip().split(": ")
                player_data[name] = int(score)

            sorted_players = sorted(player_data, key=player_data.get, reverse=True)

            high_score_list = 250
            for i, name in enumerate(sorted_players[:5]):
                score = player_data[name]
                show_high_scores = title_font.render(f'{i+1}. {name}: {score}', False, (255, 255, 255))
                WIN.blit(show_high_scores, (WIDTH / 2 - show_high_scores.get_width() / 2, high_score_list))
                high_score_list += 100

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


if __name__ == '__main__':
    """
    Main Gate: Calls main_menu function to run game
    """
    main_menu()
    # pass

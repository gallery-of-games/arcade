import pygame
import sys
import random

class Block(pygame.sprite.Sprite):
    # Most basic block/sprite class that others will inherit from
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))


class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0

    # Handles so the player does not go out of bounds
    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
    # Player movement
    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constrain()


class Ball(Block):
    # Ball needs to know where 2 paddles are so that it can collide with them
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(path, x_pos, y_pos)
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    # Handles movement of the ball
    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()
    # Handles the collision logic
    def collisions(self):
        # Checks collision against top or bottom of screen
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            pygame.mixer.Sound.play(pong_sound)
            self.speed_y *= -1
        # Checks collision of different paddles, and sides of paddles, reversing ball trajectory when hit
        if pygame.sprite.spritecollide(self, self.paddles, False):
            pygame.mixer.Sound.play(pong_sound)
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    # Handles Reset of ball to center
    def reset_ball(self):
        self.ball = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (screen_width/2, screen_height/2)
        pygame.mixer.Sound.play(score_sound)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3

        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time < 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time < 2100:
            countdown_number = 1

        if current_time - self.score_time < 2100:
            self.active = True

        time_counter = game_font.render(str(countdown_number), True, accent_color)
        time_counter_rect = time_counter.get_rect(center = (screen_width/2, screen_height/2 + 50))
        pygame.draw.rect(screen, bg_color, time_counter_rect)
        screen.blit(time_counter, time_counter_rect)


class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed

    def update(self, ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed
        self.constrain()

    def constrain(self):
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= screen_height: self.rect.bottom = screen_height


class GameManager:
    # Handles Game logic
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()
        if self.opponent_score >= 3:
            # need to fix game over method to display a new bg fill
            # self.game_over()


    def draw_score(self):
        player_score = game_font.render(str(self.player_score), True, accent_color)
        opponent_score = game_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft = (screen_width / 2 + 40, screen_height/2))
        opponent_score_rect = opponent_score.get_rect(midright = (screen_width/2 - 40, screen_height/2))

        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)

    def run_game(self):
        # Draws the Game Objects
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        # Updates Game Objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def game_over(self):
        # enter logic that will bring to game over screen
        game_over_text = game_font.render(f"You Lost with {self.player_score} points!", True, accent_color)
        game_over_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(game_over_text, game_over_rect)
        # Save score
        save_score_font = pygame.font.Font("freesansbold.ttf", 32)
        save_score_surface = save_score_font.render("Save Score", True, accent_color)
        save_score_rect = save_score_surface.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(save_score_surface, save_score_rect)
        # Replay?
        replay_font = pygame.font.Font("freesansbold.ttf", 32)
        replay_surface = replay_font.render("Replay", True, accent_color)
        replay_rect = replay_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
        screen.blit(replay_surface, replay_rect)
        # Quit
        quit_font = pygame.font.Font("freesansbold.ttf", 32)
        quit_surface = quit_font.render("Quit", True, accent_color)
        quit_rect = quit_surface.get_rect(center=(screen_width / 2, screen_height / 2 + 100))
        screen.blit(quit_surface, quit_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if save_score_rect.collidepoint(mouse_pos):
                        self.save_score()
                        return
                    if replay_rect.collidepoint(mouse_pos):
                        self.reset_scores()
                        return
                    if quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

    def save_score(self):
        # Save the score to a file
        with open("pong/scores.txt", "a") as file:
            file.write(f"{self.player_score}\n")
        self.reset_scores()

    def reset_scores(self):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group.sprite.reset_ball()

def draw_start_menu():
    screen.fill(bg_color)
    title = game_font.render('Pong', True, light_grey)
    start_button = game_font.render('Hit Space to Start', True, light_grey)
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 +
                               start_button.get_height()/2))
    pygame.display.update()


# General setup, needs init() to initialize a pygame  -------------------------------------------------------------
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# creates a clock so game runs at an constant speed
clock = pygame.time.Clock()


# Main Window, sets up main window width, height and sets it in pygame
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
# changes the name of the window
pygame.display.set_caption('Pong')


# Global Variables
# Colors ---------------------------------------Uses pygame.Color to create and hold color value variables----------------------------------------------------
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
accent_color = (240,255,255)
# Font ------------------------------------------------------------------
game_font = pygame.font.Font('freesansbold.ttf', 32)
# Sound -----------------------------------------------------------------
pong_sound = pygame.mixer.Sound('pong/assets/audio/pong.ogg')
score_sound = pygame.mixer.Sound('pong/assets/audio/score.ogg')
middle_strip = pygame.Rect(screen_width/2 - 2, 0, 4, screen_height)


# Game Objects
player = Player('pong/assets/sprites/Paddle.png', screen_width - 20, screen_height/2, 5)
opponent = Opponent('pong/assets/sprites/Paddle.png', 20, screen_width/2, 5)

# Group can take as many sprites
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

# Group single only accepts single sprite
ball = Ball('pong/assets/sprites/Ball.png', screen_width/2, screen_height/2, 4, 4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite, paddle_group)



while True:
    # Game Input(event) -----------------------------------------------------------------------
    # keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # checks for keydown pressed for player
            # handles the incrementing of the player's speed
            # which in turn handle's the player's y position
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.movement -= player.speed
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.movement += player.speed
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed


    # Visuals -------------------------------------------------------------------------------------
    # must be in top down order
    # .fill will be used for the background color
    screen.fill(bg_color)
    # Uses pygame.draw to draw the assets we need on the screen
    # pygame.draw(surface, color, rect)
    pygame.draw.rect(screen, accent_color, middle_strip)

    game_manager.run_game()

    # Updates the window, in this case, we are updating it at 60 FPS
    pygame.display.flip()
    clock.tick(60)

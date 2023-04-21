import pygame
import os
import random
import sys
from states.state import State
from states.game_over import GameOver

class Pong(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.player = Player(self.game)
        self.opponent = Opponent(self.game)
        self.ball = Ball(self.game, self.player, self.opponent)
        self.game_logic = GameLogic(self.game, self.ball, self.player, self.opponent)

# dont lose me

    def update(self, delta_time, actions):
        self.player.update(delta_time, actions)
        self.opponent.update(self.ball)
        self.ball.update(self.player, self.opponent)
        self.game_logic.update()


    def render(self, display):
        pygame.draw.rect(self.game.screen, self.game.AZURE, self.game.middle_strip)
        pygame.draw.line(self.game.screen, self.game.WHITE, (self.game.SCREEN_WIDTH // 2, 0),
                         (self.game.SCREEN_WIDTH // 2, self.game.SCREEN_HEIGHT), 2)
        display.fill((self.game.BLACK))
        self.player.render(display)
        self.opponent.render(display)
        self.ball.render(display)
        self.game_logic.render(display)
        pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.load_sprites()
        # self.position_x, self.position_y = self.game.GAME_W - 20, self.game.GAME_H/2
        self.rect = self.curr_image.get_rect(center=(self.game.GAME_W - 20, self.game.GAME_H/2))
        self.speed = 1
        self.movement = 0

    def update(self, delta_time, actions):
        direction_y = actions['down'] - actions['up']
        self.rect.y += direction_y * self.speed
        self.screen_constrain()

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.game.GAME_H:
            self.rect.bottom = self.game.GAME_H

    def render(self, display):
        display.blit(self.curr_image, (self.rect.x, self.rect.y))

    def load_sprites(self):
        # Get the directory with the player sprites
        self.sprite_dir = os.path.join(self.game.sprites_dir, "Paddle.png")
        self.curr_image = pygame.image.load(self.sprite_dir)

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, player, opponent):
        super().__init__()
        self.game = game
        self.player = player
        self.opponent = opponent
        self.load_sprites()
        self.rect = self.curr_image.get_rect(center= (self.game.GAME_W/2, self.game.GAME_H/2))
        self.difficulty = 1
        self.speed_x = self.difficulty * random.choice((-1, 1))
        self.speed_y = self.difficulty * random.choice((-1, 1))
        self.active = False
        self.score_time = 0
        self.countdown_number = 3
        self.time_counter = self.game.game_font.render(str(self.countdown_number), True, self.game.AZURE)
        self.time_counter_rect = self.time_counter.get_rect(center=(self.game.GAME_W / 2, self.game.GAME_H / 2 + 50))

    def update(self, player, opponent):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions([player, opponent])
        else:
            self.active = True

    def collisions(self, paddles):
        if self.rect.top <= 0:
            self.speed_y = abs(self.speed_y)
        elif self.rect.bottom >= self.game.GAME_H:
            # pygame.mixer.Sound.play(self.pong_sound)
            self.speed_y = -abs(self.speed_y)
        for paddle in paddles:
            if pygame.sprite.collide_rect(self, paddle):
                if abs(self.rect.right - paddle.rect.left) < 10 and self.speed_x > 0:
                    self.speed_x *= -1
                if abs(self.rect.left - paddle.rect.right) < 10 and self.speed_x < 0:
                    self.speed_x *= -1
                if abs(self.rect.top - paddle.rect.bottom) < 10 and self.speed_y < 0:
                    self.rect.top = paddle.rect.bottom
                    self.speed_y *= -1
                if abs(self.rect.bottom - paddle.rect.top) < 10 and self.speed_y > 0:
                    self.rect.bottom = paddle.rect.top
                    self.speed_y *= -1



    def reset_ball(self):
        self.ball = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (self.game.GAME_W / 2, self.game.GAME_H / 2)
        # self.restart_counter()
        # pygame.mixer.Sound.play(self.score_sound)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        self.countdown_number = 3

        if current_time - self.score_time <= 700:
            self.countdown_number = 3
        if 700 < current_time - self.score_time < 1400:
            self.countdown_number = 2
        if 1400 < current_time - self.score_time < 2100:
            self.countdown_number = 1

        if current_time - self.score_time < 2100:
            self.active = True


        # self.time_counter = self.game.game_font.render(str(self.countdown_number), True, self.game.AZURE)
        # self.time_counter_rect = self.time_counter.get_rect(center=(self.game.GAME_W / 2, self.game.GAME_H / 2 + 50))
        # pygame.draw.rect(self.game.screen, self.game.BLACK, time_counter_rect)
        # self.game.screen.blit(time_counter, time_counter_rect)


    def render(self, display):
        display.blit(self.curr_image, (self.rect.x, self.rect.y))
        # display.blit(self.time_counter, (self.time_counter_rect.x, self.time_counter_rect.y))

    def load_sprites(self):
        # Get the directory with the player sprites
        self.sprite_dir = os.path.join(self.game.sprites_dir, "Ball.png")
        self.curr_image = pygame.image.load(self.sprite_dir)

    def load_sounds(self):
        self.pong_sound_dir = os.path.join(self.game.audio_dir, 'pong.ogg')
        self.pong_sound = pygame.mixer.Sound(self.pong_sound_dir)
        self.pong_sound.set_volume(0.1)
        self.score_sound_dir = os.path.join(self.game.audio_dir, 'score.ogg')
        self.score_sound = pygame.mixer.Sound(self.score_sound_dir)
        self.score_sound.set_volume(0.1)

class Opponent(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.load_sprites()
        self.rect = self.curr_image.get_rect(center=(20, self.game.GAME_W/2))
        self.speed = 5
        self.movement = 0

    def update(self, ball):
        distance = self.rect.centery - ball.rect.centery
        if abs(distance) < 50:
            self.speed = abs(distance) // 5 + 1
        else:
            self.speed = 5
        if self.rect.top < ball.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball.rect.y:
            self.rect.y -= self.speed
        self.screen_constrain()

    def screen_constrain(self):
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= self.game.GAME_H: self.rect.bottom = self.game.GAME_H

    def render(self, display):
        display.blit(self.curr_image, (self.rect.x, self.rect.y))


    def load_sprites(self):
        # Get the directory with the player sprites
        self.sprite_dir = os.path.join(self.game.sprites_dir, "Paddle.png")
        self.curr_image = pygame.image.load(self.sprite_dir)

class GameLogic():
    def __init__(self, game, ball, player, opponent):
        self.game = game
        self.player_score = 0
        self.opponent_score = 0
        self.ball = ball
        self.player = player
        self.opponent = opponent
        self.game_over_flag = False

    def update(self):
            if self.ball.rect.right >= self.game.GAME_W:
                self.opponent_score += 1
                self.ball.reset_ball()
            if self.ball.rect.left <= 0:
                self.player_score += 1
                self.ball.reset_ball()
            if self.opponent_score >= 3:
                self.game_over_flag = True
                self.ball.active = False
                self.game_over()

    def render(self, display):
        player_score = self.game.game_font.render(str(self.player_score), True, self.game.AZURE)
        opponent_score = self.game.game_font.render(str(self.opponent_score), True, self.game.AZURE)

        player_score_rect = player_score.get_rect(midleft=(self.game.GAME_W / 2 + 40, self.game.GAME_H / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(self.game.GAME_W / 2 - 40, self.game.GAME_H / 2))

        display.blit(player_score, (player_score_rect.x, player_score_rect.y))
        display.blit(opponent_score, (opponent_score_rect.x, opponent_score_rect.y))

    def reset_scores(self):
        self.player_score = 0
        self.opponent_score = 0

    def game_over(self):
        saved_score = self.player_score
        self.reset_scores()
        self.GAME_OVER_STATE = GameOver(self.game, saved_score)
        self.GAME_OVER_STATE.enter_state()

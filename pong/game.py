import pygame
import time
import os
from pong.states.game_over import GameOver
from pong.states.pong import Pong
from pong.states.title import Title

class Game():
    """
    Initializes window for game and listens for key press events
    """
    def __init__(self):
        # pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption('Pong')
        self.GAME_W, self.GAME_H = 960, 540
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.middle_strip = pygame.Rect(self.GAME_W / 2 - 2, 0, 4, self.GAME_H)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "save": False, "retry": False,
                        "start": False}
        self.dt, self.prev_time = 0, 0
        self.timer = pygame.time.Clock()
        self.game_font = pygame.font.Font('freesansbold.ttf', 20)
        self.BLACK, self.WHITE, self.GRAY, self.AZURE = (0, 0, 0 ), (255, 255, 255), (200, 200, 200), (240,255,255)

        self.state_stack = []
        self.load_assets()
        self.load_states()

    def game_loop(self):

        while self.playing:
            self.get_dt()
            self.check_events()
            self.update()
            self.render()

    def check_events(self):
        """
        checks all event inputs from player
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_UP:
                    self.actions['up'] = True
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                if event.key == pygame.K_s:
                    self.actions['save'] = True
                if event.key == pygame.K_r:
                    self.actions['retry'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_UP:
                    self.actions['up'] = False
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.game_font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):

        self.state_stack[-1].render(self.game_canvas)
        # Render current state to the screen
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))



    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def load_assets(self):
        self.pong_dir = os.path.join('pong')
        self.assets_dir = os.path.join(self.pong_dir, 'assets')
        self.sprites_dir = os.path.join(self.assets_dir, 'sprites')
        self.audio_dir = os.path.join(self.assets_dir, 'audio')

    def load_states(self):
        # self.game_over = GameOver(self)
        # self.state_stack.append(self.game_over)
        # self.pong_game = Pong(self)
        # self.state_stack.append(self.pong_game)
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)


if __name__ == "__main__":
    pong = Game()
    while pong.running:
        pong.game_loop()
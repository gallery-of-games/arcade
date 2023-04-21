import pygame
import pygame_gui
import os
import sys
from states.state import State

class GameOver(State):
    def __init__(self, game, score):
        self.game = game
        State.__init__(self, game)
        self.score = score
        self.high_scores = {}
        self.MANAGER = pygame_gui.UIManager((self.game.GAME_W, self.game.GAME_H))


    def update(self, delta_time, actions):
        if actions['retry']:
            self.exit_state()
            self.game.reset_keys()
        if actions['save']:
            self.save_score()
            print('saving score')
        if actions['start']:
            self.game.state_stack.pop()
            self.game.state_stack.pop()
            print(self.game.state_stack)
            print('title menu')
        self.game.reset_keys()


    def render(self, display):
        display.fill(self.game.BLACK)
        self.load_scores(display)
        self.game.draw_text(display, f'You Lost With {self.score} points!', self.game.WHITE, self.game.SCREEN_WIDTH / 2, self.game.SCREEN_HEIGHT / 2)
        self.game.draw_text(display, f'Press "s" To Save Score', self.game.WHITE, self.game.SCREEN_WIDTH / 2,
                            self.game.SCREEN_HEIGHT / 2 + 30)
        self.game.draw_text(display, f'Press "r" To Retry', self.game.WHITE, self.game.SCREEN_WIDTH / 2,
                            self.game.SCREEN_HEIGHT / 2 + 60)
        self.game.draw_text(display, f'Press "enter" To Go Back To Title', self.game.WHITE, self.game.SCREEN_WIDTH /
                            2, self.game.SCREEN_HEIGHT / 2 + 90)
        pygame.display.update()


    def load_scores(self, display):
        self.scores_dir = os.path.join(self.game.pong_dir, 'scores.txt')
        with open(self.scores_dir, 'r') as score_f:
            contents = score_f.readlines()
            temp_data = {}
            for line in contents:
                name, score = line.strip().split(': ')
                temp_data[name] = int(score)
            self.sorted_scores = sorted(temp_data, key=temp_data.get, reverse=True)
            self.score_offset = 60
            self.game.draw_text(display, 'High Scores', self.game.WHITE, self.game.GAME_W/2,
                                    self.score_offset - 30 )
            for i, name in enumerate(self.sorted_scores[:5]):
                score = temp_data[name]
                self.game.draw_text(display, f'{i+1}. {name}: {score}', self.game.WHITE, self.game.GAME_W/2,
                                    self.score_offset)
                self.score_offset += 30


    def save_score(self):
        self.text_active = True
        text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((self.game.GAME_W / 2 - 130,
                                                                                    200),
                                                                                   (250,32)),
                                                         manager=self.MANAGER, object_id="#score_entry")
        while self.text_active:
            UI_REFRESH_RATE = self.game.timer.tick(60) / 1000
            self.scores_dir = os.path.join(self.game.pong_dir, 'scores.txt')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#score_entry':
                    print(event.text)
                    self.high_scores[str(event.text).strip()] = self.score
                    sorted_high_scores = sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True)[:5]
                    for key, value in sorted_high_scores:
                        with open(self.scores_dir, 'a+') as file:
                            file.write(f'{key}: {value} \n')
                    pygame.display.update()
                    self.text_active = False
                self.MANAGER.process_events(event)
            self.MANAGER.update(UI_REFRESH_RATE)
            self.MANAGER.draw_ui(self.game.screen)
            pygame.display.update()

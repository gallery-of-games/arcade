from states.state import State
from states.pong import Pong
import pygame

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["start"]:
            new_state = Pong(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill(self.game.BLACK)
        self.game.draw_text(display, "Pong", self.game.WHITE, self.game.GAME_W / 2, self.game.GAME_H / 2)
        self.game.draw_text(display, '>Press Enter To Start<', self.game.WHITE, self.game.GAME_W / 2,
                            self.game.GAME_H / 2 + 30)
        pygame.display.update()



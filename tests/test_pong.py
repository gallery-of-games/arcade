import unittest
from unittest.mock import MagicMock
import pygame
from pong.states.pong import Pong, Player

# Define a mock game object to pass into the state objects
class MockGame:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GAME_W = 780
    GAME_H = 580
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    AZURE = (0, 127, 255)
    sprites_dir = "./sprites"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_font = pygame.font.Font(None, 24)

class TestPong(unittest.TestCase):
    def test_update(self):
        # Create a mock game object and a Pong state object
        game = MockGame()
        pong = Pong(game)

        # Mock the update methods for the player, opponent, ball, and game_logic objects
        pong.player.update = MagicMock()
        pong.opponent.update = MagicMock()
        pong.ball.update = MagicMock()
        pong.game_logic.update = MagicMock()

        # Call the update method for the Pong object and check that the update methods
        # for the player, opponent, ball, and game_logic objects were called
        pong.update(1, {})
        pong.player.update.assert_called_once_with(1, {})
        pong.opponent.update.assert_called_once()
        pong.ball.update.assert_called_once_with(pong.player, pong.opponent)
        pong.game_logic.update.assert_called_once()

    def test_render(self):
        # Create a mock game object and a Pong state object
        game = MockGame()
        pong = Pong(game)

        # Create a mock display surface
        display = pygame.Surface((game.GAME_W, game.GAME_H))

        # Mock the render methods for the player, opponent, ball, and game_logic objects
        pong.player.render = MagicMock()
        pong.opponent.render = MagicMock()
        pong.ball.render = MagicMock()
        pong.game_logic.render = MagicMock()

        # Call the render method for the Pong object and check that the render methods
        # for the player, opponent, ball, and game_logic objects were called
        pong.render(display)
        pong.player.render.assert_called_once_with(display)
        pong.opponent.render.assert_called_once_with(display)
        pong.ball.render.assert_called_once_with(display)
        pong.game_logic.render.assert_called_once_with(display)

class TestPlayer(unittest.TestCase):
    def test_update(self):
        # Create a mock game object and a Player object
        game = MockGame()
        player = Player(game)

        # Call the update method with no actions and check that the position does not change
        initial_position = player.rect.y
        player.update(1, {})
        self.assertEqual(player.rect.y, initial_position)

        # Call the update method with an 'up' action and check that the position moves up
        player.update(1, {'up': True})
        self.assertEqual(player.rect.y, initial_position - player.speed)

        # Call the update method with a 'down' action and check that the position moves down
        player.update(1, {'down': True})
        self.assertEqual(player.rect.y, initial_position)

        # Call the update method with both 'up' and 'down' actions and check that the position does not change
        player.update(1, {'up': True, 'down': True})
        self.assertEqual(player.rect.y, initial_position)


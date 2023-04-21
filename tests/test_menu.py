# import pytest
# import pygame
# import pygame_menu
# from time import sleep
# from menu.menu import start_game, menu
# import unittest.mock as mock
# from unittest.mock import patch, MagicMock
# import pygame_menu.events
# import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"
#
#
# @pytest.fixture
# def surface():
#     pygame.init()
#     return pygame.display.set_mode((640, 480))
#
#
# @pytest.fixture
# def menu(surface):
#     menu = pygame_menu.Menu('Gallery of Games', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
#     menu.add.button('Quit', pygame_menu.events.EXIT)
#     return menu
#
#
# @patch('subprocess.run')
# def test_start_game_uses_correct_game(mock_run):
#     expected_commands = {
#         'Pong': 'python pong/game.py',
#         'Space Invaders': 'python space_invaders/space_invaders.py',
#         'Snake': 'python snake/snake.py',
#         'Hangman (BETA)': 'python hangman/main.py'
#     }
#     for game, expected_command in expected_commands.items():
#         start_game(game)
#         mock_run.assert_called_once_with(expected_command.split(), capture_output=True, text=True)
#         mock_run.reset_mock()
#
#
# @pytest.mark.parametrize("game", ["Pong", "Space Invaders", "Snake", "Hangman"])
# def test_start_game_opens_game_window(game):
#     pygame.init()
#     # assert that the game window has started by checking for the presence of a Pygame surface
#     assert pygame.display.get_surface() is not None
#
#
# def test_menu_closes_on_quit_button():
#     menu = pygame_menu.Menu('Gallery of Games', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
#     menu.add.button('Quit', pygame_menu.events.CLOSE)
#
#     # create a mock event to simulate the Quit button being clicked
#     mock_event = pygame.event.Event(pygame_menu.events.CLOSE, {})
#
#     # call the menu's update method with the mock event to simulate the Quit button being clicked
#     menu.update(mock_event)
#
#     # assert that the menu is closed
#     assert menu.is_enabled() == False
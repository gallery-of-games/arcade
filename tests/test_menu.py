import sys
import pytest
import pygame
import pygame_menu
from menu.menu import start_game
import unittest.mock as mock
import pygame_menu.events


# pygame.init()
# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Gallery of Games")
#
#
# menu = pygame_menu.Menu('Gallery of Games', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
#
# space_invaders_button = menu.add.button('Space Invaders', start_game, 'Space Invaders')
# pong_button = menu.add.button('Pong', start_game, 'Pong')
# snake_button = menu.add.button('Snake', start_game, 'Snake')
# menu.add.button('Quit', pygame_menu.events.EXIT)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     screen.fill((255, 255, 255))  # Fill the screen with white
#     menu.mainloop(screen)
#     pygame.display.flip()  # Update the screen


def test_start_game_uses_correct_game():
    with mock.patch('os.system') as mock_os_system:
        expected_command = start_game('Pong')
        mock_os_system.assert_called_once_with('python pong/game.py')
        assert expected_command == 'python pong/game.py'

        expected_command = start_game('Space Invaders')
        mock_os_system.assert_called_once_with('python space_invaders/space_invaders.py')
        assert expected_command == 'python space_invaders/space_invaders.py'

        expected_command = start_game('Snake')
        mock_os_system.assert_called_once_with('python snake/snake.py')
        assert expected_command == 'python snake/snake.py'


@pytest.mark.parametrize("game", ["Pong", "Space Invaders", "Snake"])
def test_start_game_opens_game_window(game):
    pygame.init()
    # assert that the game window has started by checking for the presence of a Pygame surface
    assert pygame.display.get_surface() is not None
#
#

def test_menu_closes_on_quit_button():
    pygame.init()
    menu = pygame_menu.Menu('Gallery of Games', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

    # define a custom event handler for the Quit button
    def quit_handler():
        print("Quit handler called")
        menu.disable()
        print("Quit button clicked")

    menu.add.button('Quit', quit_handler)

    # create a mock event to simulate the Quit button being clicked
    mock_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': pygame.BUTTON_LEFT})

    # call the menu's update method with the mock event to simulate the Quit button being clicked
    with mock.patch.object(pygame_menu.Menu, 'is_enabled', return_value=True):
        print("Before menu update")
        menu.update(mock_event)
        print("After menu update")

    # assert that the menu is closed
    assert not menu.is_enabled()

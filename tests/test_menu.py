# import pytest
# from unittest.mock import MagicMock
# from menu.menu import start_game
#
#
# @pytest.mark.parametrize("game", ["Pong", "Space Invaders", "Snake"])
# def test_start_game_uses_correct_game(game):
#     start_game(game)
#     # assert that the correct game was started by checking the command executed by os.system()
#     if game == "Pong":
#         expected_command = "python pong/pong.py"
#     elif game == "Space Invaders":
#         expected_command = "python space_invaders/space_invaders.py"
#     else:
#         expected_command = "python snake/snake.py"
#     assert os.system.call_args[0][0] == expected_command
#
#
# @pytest.mark.parametrize("game", ["Pong", "Space Invaders", "Snake"])
# def test_start_game_opens_game_window(game):
#     start_game(game)
#     # assert that the game window has started by checking for the presence of a Pygame surface
#     assert pygame.display.get_surface() is not None
#
#
# def test_menu_closes_on_quit_button():
#     menu = pygame_menu.Menu('Gallery of Games', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
#     menu.add.button('Quit', pygame_menu.events.CLOSE)
#
#     # create a mock event to simulate the Quit button being clicked
#     mock_event = MagicMock()
#     mock_event.type = pygame_menu.events.PYGAME_QUIT
#
#     # call the menu's update method with the mock event to simulate the Quit button being clicked
#     menu.update(mock_event)
#
#     # assert that the menu is closed
#     assert menu.is_enabled() == False
import os
import pygame
import pytest
import random
from hangman.main import display_message


pygame.init()
pygame.font.init()

# def test_sanitize_input():
#     assert sanitize_input("AbC123") == "abc"



def test_draw_text():
    font = pygame.font.SysFont('comicsans', 40)


# def test_draw_hangman():
#     surface = pygame.Surface((640, 480))
#     for i in range(7):
#         draw_hangman(i, surface)



def test_draw_word_completion():
    font = pygame.font.SysFont('comicsans', 60)


def test_draw_guessed_letters():
    font = pygame.font.SysFont('comicsans', 40)


def test_display_message():
    display_message("Game over!")



# def test_update_high_score(tmp_path):
#     # Set up a temporary directory for the test
#     tmp_dir = tmp_path / "hangman"
#     tmp_dir.mkdir()
#     print(tmp_path)
#     # Set the high score to zero and then update it to 10
#     config_file = tmp_dir / "config.txt"
#     config_file.write_text("0")
#     update_high_score(10, config_file)

    # # Check that the high score was updated to 10
    # assert config_file.read_text() == "10"
    #
    # # Update the high score to 5, which should not overwrite the previous score of 10
    # update_high_score(5, config_file)
    #
    # # Check that the high score remains 10
    # assert config_file.read_text() == "10"


# def test_main_loop():
#     # Test that the main game loop runs without errors
#     main_loop()






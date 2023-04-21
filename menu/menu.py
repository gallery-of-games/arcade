import pygame, pygame_menu, os
import subprocess

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gallery of Games")


def start_game(game):
    if game == 'Pong':
        command = 'python pong/game.py'
    elif game == 'Space Invaders':
        command = 'python space_invaders/space_invaders.py'
    elif game == 'Snake':
        command = 'python snake/snake.py'
    elif game == 'Hangman (BETA)':
        command = 'python hangman/main.py'
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if pygame.event.peek(pygame.QUIT):
        pygame.quit()
        quit()
    return result.args


menu = pygame_menu.Menu('Gallery of Games', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

space_invaders_button = menu.add.button('Space Invaders', start_game, 'Space Invaders')
pong_button = menu.add.button('Pong', start_game, 'Pong')
snake_button = menu.add.button('Snake', start_game, 'Snake')
hangman_button = menu.add.button('Hangman (BETA)', start_game, 'Hangman (BETA)')

menu.add.button('Quit', pygame_menu.events.EXIT)


if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((255, 255, 255))  # Fill the screen with white
        menu.mainloop(screen)
        pygame.display.flip()  # Update the screen

import pygame, pygame_menu, os
import subprocess

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Gallery of Games")


def start_game(game):
    if game == 'Pong':
        os.system('python pong/game.py')
    elif game == 'Space Invaders':
        os.system('python space_invaders/space_invaders.py')
    elif game == 'Snake':
        os.system('python snake/snake.py')


menu = pygame_menu.Menu('Gallery of Games', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

space_invaders_button = menu.add.button('Space Invaders', start_game, 'Space Invaders')
pong_button = menu.add.button('Pong', start_game, 'Pong')
snake_button = menu.add.button('Snake', start_game, 'Snake')

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

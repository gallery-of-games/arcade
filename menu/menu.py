import pygame, pygame_menu, os

pygame.init()
screen = pygame.display.set_mode((600, 400))


def start_game(game):
    if game == 'Pong':
        os.system('python3 pong/pong.py')
    elif game == 'Space Invaders':
        os.system('python3 space_invaders/space_invaders.py')

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

name_widget = menu.add.text_input('Name :', default='John Doe')
space_invaders_button = menu.add.button('Space Invaders', start_game, 'Space Invaders')
pong_button = menu.add.button('Pong', start_game, 'Pong')
menu.add.button('Quit', pygame_menu.events.EXIT)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))  # Fill the screen with white
    menu.mainloop(screen)
    pygame.display.flip()  # Update the screen

    name_widget.set_value('New Name')  # set the default value of the Name field to "New Name"
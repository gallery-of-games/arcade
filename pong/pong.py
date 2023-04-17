import pygame
import sys
import random

def ball_animation():
    # gets out of local scope with global key word, can use return statements or class
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    # this will increment the ball's position by the speed we defined by 60 frames per second
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # collide rect can be called on a rect, with another rect as a paremeter and returns boolean
    # based on if the two rect's collided
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # This covers the ball going out of bounds
    # multiplying the speed by -1 will reverse the ball speed
    # This covers the vertical, y axis
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # This covers the Horizontal, x axis, which would mean out of bounds
    if ball.left <= 0:
        player_score += 1
        # gets how long the time has been since game started with get_ticks(), only runs once and stays the same
        score_time = pygame.time.get_ticks()
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()



def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    # this runs every time
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render('3', False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render('2', False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render('1', False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        # randomizes direction
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None



def player_animation():
    # moves the player among the y-axis, vertically
    player.y += player_speed
    # Handles so the player does not go out of bounds
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_bot():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


# General setup, needs init() to initialize a pygame  -------------------------------------------------------------
pygame.init()

# creates a clock so game runs at an constant speed
clock = pygame.time.Clock()

# Sets up main window width, height and sets it in pygame
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
# changes the name of the window
pygame.display.set_caption('Pong')

# Sets up game rectangles
# Rect(xpos, ypos, width_of_rect, height_of_rect)
# origin of window is top left, (0,0) so to go down, increase y
# These are empty rectangles until we use pygame.draw
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Uses pygame.Color to create and hold color value variables
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


# Game variables ----------------------------------------------------------------------------------
# creates variable that holds the speed of the ball and starts in a random direction
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# creates variables that hold the speed of the player
player_speed = 0

# creates variable that holds the speed of the opponent
# adjust this change difficulty
opponent_speed = 7

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

# Score timer
score_time = True

while True:
    # Game Input(event) -----------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checks for keydown pressed for player
        # handles the incrementing of the player's speed
        # which in turn handle's the player's y position
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # Game Logic -------------------------------------------------------------------------------
    ball_animation()
    player_animation()
    opponent_bot()


    # Visuals -------------------------------------------------------------------------------------
    # must be in top down order
    # .fill will be used for the background color
    screen.fill(bg_color)

    # Uses pygame.draw to draw the assets we need on the screen
    # pygame.draw(surface, color, rect)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    # used to draw line in the middle
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Only runs if score_time gets a value, which happens if a player scores
    if score_time:
        ball_restart()

    # New text for surface
    player_text = game_font.render(f'{player_score}', False, light_grey)
    opponent_text = game_font.render(f'{opponent_score}', False, light_grey)
    # Puts one surface on another
    screen.blit(player_text, (660, 470))
    screen.blit(opponent_text, (600, 470))

    # Updates the window, in this case, we are updating it at 60 FPS
    pygame.display.flip()
    clock.tick(60)
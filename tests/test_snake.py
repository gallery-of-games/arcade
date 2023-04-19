import pytest
import pygame
from arcade.snake.snake import SNAKE, FRUIT, MAIN

pygame.init()
screen = pygame.display.set_mode((600, 600))
cell_size = 30
cell_number = 20
apple = pygame.image.load('assets/apple.png').convert_alpha()

def test_snake_initialization():
    snake = SNAKE()
    assert len(snake.body) == 3
    assert snake.direction == pygame.math.Vector2(1, 0)
    assert not snake.new_block

def test_snake_move():
    snake = SNAKE()
    original_body = snake.body[:]
    snake.move_snake()
    assert snake.body[0] == original_body[0] + snake.direction
    assert snake.body[1:] == original_body[:-1]

def test_snake_add_block():
    snake = SNAKE()
    original_length = len(snake.body)
    snake.add_block()
    assert len(snake.body) == original_length + 1
    assert snake.new_block == True

def test_fruit_randomization():
    fruit = FRUIT()
    assert 0 <= fruit.pos.x < cell_number
    assert 0 <= fruit.pos.y < cell_number

def test_main_initialization():
    main = MAIN()
    assert isinstance(main.snake, SNAKE)
    assert isinstance(main.fruit, FRUIT)
    assert main.current_score == 0
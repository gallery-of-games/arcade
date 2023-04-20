import pytest
import pygame
from pygame.math import Vector2
from snake.snake import SNAKE, FRUIT, MAIN


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


def test_main_initialization():
    main = MAIN()
    assert isinstance(main.snake, SNAKE)
    assert isinstance(main.fruit, FRUIT)
    assert main.current_score == 0


def test_FRUIT():
    fruit = FRUIT()
    # Testing the initial state of the fruit
    assert fruit.x >= 0 and fruit.x < 20
    assert fruit.y >= 0 and fruit.y < 20
    assert fruit.pos == Vector2(fruit.x, fruit.y)



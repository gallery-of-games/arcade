import pytest
import pygame, sys
from unittest.mock import MagicMock
from pygame.math import Vector2
from snake.snake import SNAKE, FRUIT, MAIN


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))


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


# Test for update_head_graphics function
def test_update_head_graphics():
    snake = SNAKE()
    snake.body[0] = pygame.math.Vector2(0, 0)
    snake.body[1] = pygame.math.Vector2(1, 0)
    snake.update_head_graphics()
    assert snake.head == snake.head_left

    snake.body[1] = pygame.math.Vector2(-1, 0)
    snake.update_head_graphics()
    assert snake.head == snake.head_right

    snake.body[1] = pygame.math.Vector2(0, 1)
    snake.update_head_graphics()
    assert snake.head == snake.head_up

    snake.body[1] = pygame.math.Vector2(0, -1)
    snake.update_head_graphics()
    assert snake.head == snake.head_down


# Test for update_tail_graphics function
def test_update_tail_graphics():
    snake = SNAKE()
    snake.body[-1] = pygame.math.Vector2(0, 0)
    snake.body[-2] = pygame.math.Vector2(1, 0)
    snake.update_tail_graphics()
    assert snake.tail == snake.tail_left

    snake.body[-2] = pygame.math.Vector2(-1, 0)
    snake.update_tail_graphics()
    assert snake.tail == snake.tail_right

    snake.body[-2] = pygame.math.Vector2(0, 1)
    snake.update_tail_graphics()
    assert snake.tail == snake.tail_up

    snake.body[-2] = pygame.math.Vector2(0, -1)
    snake.update_tail_graphics()
    assert snake.tail == snake.tail_down


# Test for move_snake function
def test_move_snake():
    snake = SNAKE()
    snake.direction = pygame.math.Vector2(1, 0)

    # Test when a new block is added
    snake.new_block = True
    snake.move_snake()
    assert snake.body == [pygame.math.Vector2(6, 10), pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]

    # Test when a new block is not added
    snake.new_block = False
    snake.move_snake()
    assert snake.body == [pygame.math.Vector2(7, 10), pygame.math.Vector2(6, 10), pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10)]


# Test for add_block function
def test_add_block():
    snake = SNAKE()
    assert snake.new_block == False
    snake.add_block()
    assert snake.new_block == True


# Test for reset function
def test_reset():
    snake = SNAKE()
    snake.body[0] = pygame.math.Vector2(0, 0)
    snake.body[1] = pygame.math.Vector2(1, 0)
    snake.body[2] = pygame.math.Vector2(2, 0)

    snake.reset()
    assert snake.body == [pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]


# Test for FRUIT class
def test_fruit():
    fruit = FRUIT()
    assert isinstance(fruit.pos, pygame.math.Vector2)
    assert fruit.pos.x >= 0 and fruit.pos.x < cell_number


@pytest.fixture
def main():
    return MAIN()


def test_check_collision_snake(main):
    main.snake.body = [(0, 0), (1, 1), (1, 0)]
    main.check_collision()
    assert main.game_over() == None


def test_init(main):
    assert isinstance(main.snake, SNAKE)
    assert isinstance(main.fruit, FRUIT)
    assert main.current_score == 0


def test_update(main):
    main.update()
    assert isinstance(main.current_score, int)



class TestFRUIT:
    def test_randomize(self):
        fruit = FRUIT()
        fruit.randomize()
        assert 0 <= fruit.x < cell_number
        assert 0 <= fruit.y < cell_number
        assert isinstance(fruit.pos, Vector2)

class TestSnake:
    def test_add_block(self):
        snake = SNAKE()
        assert not snake.new_block
        snake.add_block()
        assert snake.new_block

    def test_reset(self):
        snake = SNAKE()
        snake.body = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        snake.reset()
        assert snake.body == [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]


def test_move_snake_add_block():
    game = MAIN()
    game.snake.add_block()
    game.snake.move_snake()
    assert len(game.snake.body) == 4


def test_move_snake_no_add_block():
    game = MAIN()
    game.snake.move_snake()
    assert len(game.snake.body) == 3


def test_move_snake_direction():
    game = MAIN()
    game.snake.direction = Vector2(1, 0)
    game.snake.move_snake()
    assert game.snake.body[0] == Vector2(6, 10)


def test_move_snake_body_copy():
    game = MAIN()
    game.snake.move_snake()
    assert game.snake.body == [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]

def test_check_collision_with_fruit():
    main = MAIN()
    main.snake.body = [Vector2(5, 5)]
    main.fruit.pos = Vector2(5, 5)
    main.check_collision()
    assert main.snake.new_block == True
    assert main.current_score == 1

def test_check_collision_with_snake():
    main = MAIN()
    main.snake.body = [Vector2(5, 5), Vector2(6, 5), Vector2(6, 6)]
    main.fruit.pos = Vector2(6, 5)
    main.check_collision()
    assert main.fruit.pos != Vector2(6, 5)


# new tests



import pytest
import pygame
import sys
import os
from unittest.mock import mock_open, patch
from space_invaders.space_invaders import Player, Enemy, Laser, Ship, main, collide


# @pytest.mark.skip
def test_enemy_attributes():
    enemy = Enemy(0, 0, 'red')
    assert enemy.health == 100
    assert enemy.ship_img is not None
    assert enemy.laser_img is not None
    assert enemy.lasers == []
    assert enemy.cool_down_counter == 0


# @pytest.mark.skip
def test_enemy_movement():
    enemy = Enemy(0, 0, 'red')
    enemy.move(5)
    assert enemy.y == 5


# @pytest.mark.skip
def test_laser_movement():
    laser = Laser(0, 0, pygame.Surface((10, 10)))
    laser.move(5)
    assert laser.y == 5


# @pytest.mark.skip
def test_ship_laser_shoot():
    player = Player(0, 0)
    player.shoot()
    assert len(player.lasers) == 1


@pytest.mark.skip
def tes_ship_health_damage():
    player = Player(0, 0)
    enemy = Enemy(0, 50, 'red')
    player.lasers.append(0, 0, pygame.Surface((10, 10)))
    assert enemy.health == 100
    player.move_lasers(-5, enemy)
    assert enemy.health == 90


# @pytest.mark.skip
def test_laser_off_screen():
    laser = Laser(0, -10, pygame.Surface((10, 10)))
    assert laser.off_screen(750) is True
    laser = Laser(0, 850, pygame.Surface((10, 10)))
    assert laser.off_screen(750) is True


# @pytest.mark.skip
def test_laser_collision():
    object1 = Player(0, 0)
    object2 = Enemy(0, 0, 'red')
    laser = Laser(0, 0, pygame.Surface((10, 10)))
    assert laser.collision(object1) is False
    assert laser.collision(object2) is False


# @pytest.mark.skip
def test_ship_cooldown():
    player = Player(0, 0)
    player.shoot()
    assert player.cool_down_counter == 1
    player.shoot()
    assert player.cool_down_counter == 1
    player.cool_down_counter = 1
    player.shoot()
    assert player.cool_down_counter == 1


# @pytest.mark.skip
def test_ship_move_lasers():
    player = Player(0, 0)
    enemy = Enemy(0, 50, 'red')
    player.lasers.append(Laser(0, 0, pygame.Surface((10, 10))))
    player.move_lasers(-5, enemy)
    assert len(player.lasers) == 0
    assert enemy.health == 100


# @pytest.mark.skip
def test_high_score_dict():
    high_score = {"player1": 100}
    assert high_score["player1"] == 100
    assert len(high_score) == 1


def test_enemy_move():
    # Ensure that the enemy object moves correctly
    enemy = Enemy(300, 630, "red")
    assert enemy.x == 300
    assert enemy.y == 630
    enemy.move(-1)
    assert enemy.y == 629


# @pytest.mark.skip
def test_collide():
    # Ensure that the collide function detects collisions correctly
    player = Player(300, 630)
    enemy = Enemy(300, 600, "red")
    assert collide(player, enemy) == False
    enemy.y = 610
    assert collide(player, enemy) == True


# @pytest.mark.skip
def test_high_scores_are_sorted():
    high_score = {"Player 1": 500, "Player 2": 1000, "Player 3": 750}
    with patch('builtins.open', mock_open(read_data='')) as mock_file:
        sorted_high_scores = sorted(high_score.items(), key=lambda x: x[1], reverse=True)[:2]
        assert sorted_high_scores == [("Player 2", 1000), ("Player 3", 750)]


# @pytest.mark.skip
def test_player_data_is_parsed_correctly():
    contents = ["Player 1: 500 \n", "Player 2: 1000 \n", "Player 3: 750 \n"]
    with patch('builtins.open', mock_open(read_data='\n'.join(contents))):
        player_data = {}
        for line in contents:
            name, score = line.strip().split(": ")
            player_data[name] = int(score)
        assert player_data == {"Player 1": 500, "Player 2": 1000, "Player 3": 750}


# @pytest.mark.skip
def test_high_scores_file_exists():
    assert os.path.isfile('space_invaders/assets/player_name_score.txt')


@pytest.mark.skip
def test_high_scores_file_writable():
    with open('space_invaders/assets/player_name_score.txt', 'a+') as file:
        file.write('test: 0\n')
    with open('space_invaders/assets/player_name_score.txt', 'r') as file:
        contents = file.read()
    assert 'test: 0\n' in contents

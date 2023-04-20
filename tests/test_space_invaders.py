import pytest
import pygame
from space_invaders import Player, Enemy, Laser


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


# @pytest.mark.skip
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


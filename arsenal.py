"""
    Project name: Alien Invation Game
    Author:Adhanet Gebretensay
    Purpose:To manage active bullets, firing limit, update position, and clean up off-screen bullets.
    Date:10/20/2026

"""




import pygame
from alien import Alien
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class Arsenal:
    """ A class to manage all bullets fired by a ship"""

    def __init__(self,game:'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom<= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False


    
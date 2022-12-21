# Строки 3,4 предотвращают проблему круговой зависимости
# При тайп-хинтинге
from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship(Sprite):
  """Класс для управления кораблём"""
  
  def __init__(self, ai_game: AlienInvasion) -> None:
    """Инициализирует корабль и задаёт его начальную позицию"""
    super().__init__()
    
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    self.settings = ai_game.settings
    
    # Загружает изображение корабля и получает прямоугольник
    self.image = pygame.image.load("images/ship.bmp")
    self.rect = self.image.get_rect()
    
    # Размещение корабля в центре внизу
    self.center_ship()
    
    # Флаги перемещения
    self.moving_right = False
    self.moving_left = False
    
  def update(self):
    """Обновляет позицию корабля с учётом флага"""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed
      
    self.rect.x = self.x
    
  def blitme(self):
    """Рисует корабль в текущей позиции"""
    self.screen.blit(self.image, self.rect)
    
  def center_ship(self):
    """Размещает корабль в центре нижней стороны"""
    self.rect.midbottom = self.screen_rect.midbottom
    self.x = float(self.rect.x)
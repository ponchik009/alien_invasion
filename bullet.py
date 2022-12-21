# Строки 3,4 предотвращают проблему круговой зависимости
# При тайп-хинтинге
from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
  """Класс для управления снарядами, выпущенными кораблём"""
  
  def __init__(self, ai_game: AlienInvasion):
    """Создаёт объект снарядов в текущей позиции корабля"""
    super().__init__()
    
    self.ai = ai_game
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color
    
    # Создание снаряда в позиции (0, 0) и назначение правильной позиции
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop
    
    # Позиция снаряда хранится в вещественном формате
    self.y = float(self.rect.y)
    
  def update(self):
    """Перемещает снаряд вверх по экрану"""
    # Обновление позиции снаряда в вещественном формате
    self.y -= self.settings.bullet_speed
    # Обновление позиции у прямоугольника
    self.rect.y = self.y
    
  def draw_bullet(self):
    """Вывод снаряда на экран"""
    pygame.draw.rect(self.screen, self.color, self.rect)